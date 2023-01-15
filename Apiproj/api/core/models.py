from django.db import models


class results(models.Model):
    objects = None
    full_name = models.CharField(max_length=50)
    desc = models.TextField(default="")
    result_xray = models.CharField(max_length=100)
    result_pneumonia = models.CharField(max_length=100)
    result_covid = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    class Meta:
        ordering = ('-created',)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.created)