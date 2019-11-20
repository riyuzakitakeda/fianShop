# Generated by Django 2.2.7 on 2019-11-20 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0005_auto_20191116_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='kontak_deskripsi',
            field=models.TextField(default=0, max_length=5000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artwork',
            name='deskripsi',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile',
            field=models.TextField(max_length=2000),
        ),
    ]
