# Generated by Django 4.1.7 on 2023-03-26 18:14

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_postimages_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='header_img',
            field=models.ImageField(blank=True, null=True, upload_to=blog.models.post_images_path),
        ),
    ]
