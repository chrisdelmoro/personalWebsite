# Generated by Django 4.1.7 on 2023-03-26 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_postimages_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]