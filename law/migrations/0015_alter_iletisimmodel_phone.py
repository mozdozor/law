# Generated by Django 3.2.5 on 2021-08-02 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('law', '0014_iletisimmodel_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iletisimmodel',
            name='phone',
            field=models.CharField(max_length=11),
        ),
    ]