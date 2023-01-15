from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import View

from .forms import RegistrationForm, UserEditForm
from .models import UserBase
# from core.views import user_result
from django.utils.decorators import method_decorator


class Dashboard(View):
    @method_decorator(login_required)
    def get(self, request):
        user = UserBase.objects.get(user_name=request.user)
        # results = user_result(request)
        length = user.ReportCount
        print(length)
        return render(request,
                      'dashboard.html',
                      {'section': 'profile', 'user_': user, 'length': length})


class EditDetails(View):
    @method_decorator(login_required)
    def post(self, request):
        user_form = UserEditForm(instance=request.user, data=request.POST)

        if user_form.is_valid():
            user_form.save()
        return render(request,
                      'edit_details.html', {'user_form': user_form})

    @method_decorator(login_required)
    def get(self, request):
        user_form = UserEditForm(instance=request.user)
        return render(request,
                      'edit_details.html', {'user_form': user_form})


class DeleteUser(View):
    @method_decorator(login_required)
    def get(self, request):
        user = UserBase.objects.get(user_name=request.user)
        user.is_active = False
        user.save()
        logout(request)
        return redirect('/')


class AccountRegister(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('account:dashboard')
        registerForm = RegistrationForm()
        return render(request, 'register.html', {'form': registerForm})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('account:dashboard')
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('/')
        return render(request, 'register.html', {'form': registerForm})
