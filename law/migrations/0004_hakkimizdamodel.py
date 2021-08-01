# Generated by Django 3.2.5 on 2021-07-31 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('law', '0003_iletisimmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='HakkimizdaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('yazi', models.TextField()),
                ('image', models.ImageField(upload_to='hakkimizda_images')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Hakkımızda',
                'verbose_name_plural': 'Hakkımızda',
                'db_table': 'HakkimizdaModel',
            },
        ),
    ]
