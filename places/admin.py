from django.contrib import admin
from .models import Place, Image
from django.utils import safestring

# Register your models here.

class ImageInline(admin.TabularInline):
    model = Image

    readonly_fields = ['preview_image']

    def preview_image(self, obj):
        return safestring.mark_safe('<img src="{url}" width="200" height="200" />'.format(
            url = obj.image_file.url,
            )
    )

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ['preview_image']

    def preview_image(self, obj):
        return safestring.mark_safe('<img src="{url}" width="200" height="200" />'.format(
            url = obj.image_file.url,
            )
    )
