# Generated by Django 4.1.7 on 2023-03-25 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_post_images_remove_postimages_post_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postimages',
            name='image_fk',
        ),
        migrations.AddField(
            model_name='postimages',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
            preserve_default=False,
        ),
    ]