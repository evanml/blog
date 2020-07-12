# Generated by Django 3.0.8 on 2020-07-12 16:46

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
