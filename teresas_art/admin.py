from django.contrib import admin

# Register your models here.
from .models import Year, Artwork, Info

class ArtworkAdmin(admin.ModelAdmin):
	list_display = ('name', 'medium', 'year', 'image', 'uploaded')

class InfoAdmin(admin.ModelAdmin):
	list_display = ('cv', 'about')

admin.site.register(Artwork, ArtworkAdmin)
admin.site.register(Year)
admin.site.register(Info, InfoAdmin)