# Generated by Django 3.2.5 on 2021-08-02 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('law', '0013_alter_hakkimizdamodel_yazi'),
    ]

    operations = [
        migrations.AddField(
            model_name='iletisimmodel',
            name='phone',
            field=models.CharField(default='', max_length=11),
        ),
    ]