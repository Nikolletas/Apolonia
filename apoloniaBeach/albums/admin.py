from django.contrib import admin

from apoloniaBeach.albums.models import Album

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('photo', 'photo_type', 'description', 'published_by', 'upload_date', 'apartment', 'price', 'price_per_night', 'currency')
    search_fields = ('description', 'apartment')
    list_filter = ('currency', 'apartment')
    ordering = ('apartment',)

    # Позволява редактиране на всички полета
    fieldsets = (
        (None, {
            'fields': ('photo', 'description', 'price', 'price_per_night', 'apartment', 'currency')
        }),
    )
