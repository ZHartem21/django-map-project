from adminsortable2.admin import SortableAdminMixin, SortableTabularInline, SortableAdminBase
from django.contrib import admin
from django.utils import safestring 
from django.utils import html

from .models import Image, Place


def get_preview_image(image):
    return html.format_html(
        '<img src="{}" width="200" height="200" />', image.image_file.url
    )


class ImageInline(SortableTabularInline, admin.TabularInline):
    model = Image

    readonly_fields = ['preview_image']

    def preview_image(self, image):
        return get_preview_image(image)


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    fields = ('title', 'description_short', 'description_long', 'lat', 'lon')
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = ['preview_image']

    def preview_image(self, image):
        return get_preview_image(image)
