# Generated by Django 4.0.3 on 2022-03-27 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_rename_photo_image_photo_pic_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='photo_pic',
            new_name='image',
        ),
    ]
