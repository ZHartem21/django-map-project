from adminsortable2.admin import SortableAdminMixin, SortableTabularInline, SortableAdminBase
from django.contrib import admin
from django.utils import safestring

from .models import Image, Place

# Register your models here.

class ImageInline(SortableTabularInline, admin.TabularInline):
    model = Image

    readonly_fields = ['preview_image']

    def preview_image(self, obj):
        return safestring.mark_safe('<img src="{url}" width="200" height="200" />'.format(
            url = obj.image_file.url,
        )
    )

@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = ['preview_image']

    def preview_image(self, obj):
        return safestring.mark_safe('<img src="{url}" width="200" height="200" />'.format(
            url = obj.image_file.url,
        )
    )
