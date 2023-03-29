# Generated by Django 4.1.7 on 2023-03-25 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_postimages_image_fk_postimages_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimages',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='blog.post'),
        ),
    ]