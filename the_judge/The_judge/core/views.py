import base64
import json
import os
import torch
import torch.nn as nn
from django.utils.decorators import method_decorator
from django.views import View
from torchvision import models
from torchvision import transforms
from PIL import Image
from django.shortcuts import render
from django.conf import settings
from .forms import ImageUploadForm
from django.contrib.auth.decorators import login_required
from .models import Result
import io


def CNN_Model(pretrained=True):
    if torch.cuda.is_available():
        device = torch.device("cuda:0")
    else:
        device = torch.device("cpu")
    model = models.densenet121(pretrained=pretrained)
    num_filters = model.classifier.in_features
    model.classifier = nn.Linear(num_filters, 2)
    model = model.to(device)
    return model


MODEL_PATH = os.path.join(settings.STATIC_ROOT, "Pneumonia-normal-differentiator.pth")
model_final = CNN_Model(pretrained=False)
model_final.to(torch.device('cpu'))
model_final.load_state_dict(torch.load(MODEL_PATH, map_location='cpu'))
model_final.eval()
json_path = os.path.join(settings.STATIC_ROOT, "classes.json")
imagenet_mapping = json.load(open(json_path))
mean_nums = [0.485, 0.456, 0.406]
std_nums = [0.229, 0.224, 0.225]


def transform_image(image_bytes):
    my_transforms = transforms.Compose([
        transforms.Resize((64, 64)),
        transforms.ToTensor(),
        transforms.Normalize(mean=mean_nums, std=std_nums)
    ])
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    return my_transforms(image).unsqueeze(0)


def get_prediction(image_bytes):
    tensor = transform_image(image_bytes)
    outputs = model_final.forward(tensor)
    _, y_hat = outputs.max(1)
    predicted_idx = str(y_hat.item())
    class_name, human_label = imagenet_mapping[predicted_idx]
    return human_label


class MainPage(View):
    @method_decorator(login_required)
    def post(self, request):
        image_url = None
        predicted_label = None
        pre = "Not a valid image!"
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            image_bytes = image.file.read()
            encoded_img = base64.b64encode(image_bytes).decode('ascii')
            image_url = 'data:%s;base64,%s' % ('image/jpeg', encoded_img)
            try:
                predicted_label = get_prediction(image_bytes)
                Result.objects.create(res=predicted_label)
                user = request.user
                user.save()
            except RuntimeError as re:
                print(re)
        context = {
            'image_url': image_url,
            'form': form,
            'predicted_label': predicted_label,
            'pre': pre,
        }
        return render(request, 'index.html', context)

    @method_decorator(login_required)
    def get(self, request):
        form = ImageUploadForm()
        image_url = None
        predicted_label = None
        predicted_label_covid = None
        pre = "Not a valid image!"
        context = {
            'image_url': image_url,
            'form': form,
            'predicted_label': predicted_label,
            'predicted_label_covid': predicted_label_covid,
            'pre': pre,
        }
        return render(request, 'index.html', context)
