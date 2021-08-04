# Generated by Django 3.2.5 on 2021-08-02 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('law', '0015_alter_iletisimmodel_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='iletisimbilgilermodel',
            name='facebook',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='iletisimbilgilermodel',
            name='instagram',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='iletisimbilgilermodel',
            name='linkedin',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='iletisimbilgilermodel',
            name='twitter',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='iletisimmodel',
            name='message',
            field=models.TextField(verbose_name='Mesaj'),
        ),
        migrations.AlterField(
            model_name='iletisimmodel',
            name='phone',
            field=models.CharField(max_length=11, verbose_name='Telefon'),
        ),
        migrations.AlterField(
            model_name='iletisimmodel',
            name='subject',
            field=models.CharField(max_length=250, verbose_name='Konu'),
        ),
    ]