from django.db import models


class Artwork(models.Model):
    judul = models.CharField(max_length=100)
    video_url = models.CharField(max_length=1000)
    image_url = models.CharField(max_length=1000)
    deskripsi = models.TextField(max_length=2000)


class Home(models.Model):
    home_judul = models.CharField(max_length=225)
    home_image_url = models.CharField(max_length=1000)
    home_video_url = models.CharField(max_length=1000)


class Profile(models.Model):
    profile = models.TextField(max_length=2000)


class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    kontak_deskripsi = models.TextField(max_length=5000)
    link_maps = models.CharField(max_length=1000)