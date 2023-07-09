from adminsortable2.admin import SortableAdminMixin, SortableTabularInline, SortableAdminBase
from django.contrib import admin
from django.utils import html

from .models import Image, Place


class ImagePreviewMixin:
    def preview(self, image):
        image_url = image.image_file.url

        return html.format_html('<img src="{}" height={} />', image_url, height=200)


class ImageInline(SortableTabularInline, admin.TabularInline, ImagePreviewMixin):
    model = Image
    readonly_fields = ['preview']



@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    fields = ('title', 'description_short', 'description_long', 'lat', 'lon')
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin, ImagePreviewMixin):
    readonly_fields = ['preview']