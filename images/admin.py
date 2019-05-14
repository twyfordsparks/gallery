from django.contrib import admin
from .models import Editor, Images, tags,Category,Location


class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Editor)
admin.site.register(Images,ImageAdmin)
admin.site.register(tags)
admin.site.register(Category)
admin.site.register(Location)
