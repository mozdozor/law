# Generated by Django 3.2.5 on 2021-08-01 06:54

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('law', '0012_hakkimizdamodel_image_single'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hakkimizdamodel',
            name='yazi',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
