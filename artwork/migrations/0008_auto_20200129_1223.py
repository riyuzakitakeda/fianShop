# Generated by Django 2.2.7 on 2020-01-29 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0007_auto_20191121_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='image10_url',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artwork',
            name='image4_url',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artwork',
            name='image5_url',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artwork',
            name='image6_url',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artwork',
            name='image7_url',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artwork',
            name='image8_url',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artwork',
            name='image9_url',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
    ]
