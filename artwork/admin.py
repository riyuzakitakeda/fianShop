from django.contrib import admin
from .models import Artwork, Home, Profile, Contact


class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('judul', 'video_url', 'image_url')


class HomeAdmin(admin.ModelAdmin):
    list_display = ('home_judul', 'home_image_url', 'home_video_url')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone', 'name', 'email')


admin.site.register(Artwork, ArtworkAdmin)
admin.site.register(Home, HomeAdmin)
admin.site.register(Profile)
admin.site.register(Contact, ContactAdmin)
