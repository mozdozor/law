# Generated by Django 3.2.5 on 2021-08-01 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('law', '0008_nedenbizmodeli'),
    ]

    operations = [
        migrations.AddField(
            model_name='nedenbizmodeli',
            name='image',
            field=models.ImageField(default='', upload_to='nedenbiz_image'),
        ),
    ]