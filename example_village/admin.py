from django.contrib import admin

from example_village.models import VillageAuthor, VillageGenre, VillageBook


# Register your models here.
@admin.register(VillageAuthor)
class VillageAuthorAdmin(admin.ModelAdmin):
    """
    Admin model for VillageAuthor
    """

    list_display = (
        "first_name",
        "last_name",
        "birth_date",
    )


@admin.register(VillageGenre)
class VillageGenreAdmin(admin.ModelAdmin):
    """
    Admin model for VillageGenre
    """

    list_display = (
        "code",
        "designation",
        "help_text",
    )


@admin.register(VillageBook)
class VillageBookAdmin(admin.ModelAdmin):
    """
    Admin model for VillageBook
    """

    pass
