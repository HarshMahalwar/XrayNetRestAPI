# Generated by Django 2.2.12 on 2022-10-08 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0002_auto_20221008_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]