from django.contrib import admin

from .models import Folder, Source, Profile, Tag

admin.site.register(Folder)
admin.site.register(Source)
admin.site.register(Profile)
admin.site.register(Tag)

