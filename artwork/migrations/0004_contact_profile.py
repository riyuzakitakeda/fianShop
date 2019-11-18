# Generated by Django 2.2.7 on 2019-11-16 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0003_artwork_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.IntegerField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('link_maps', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.CharField(max_length=2000)),
            ],
        ),
    ]