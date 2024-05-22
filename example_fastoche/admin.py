from django.contrib import admin

from example_fastoche.models import FastocheAuthor, FastocheGenre, FastocheBook


# Register your models here.
@admin.register(FastocheAuthor)
class FastocheAuthorAdmin(admin.ModelAdmin):
    """
    Admin model for FastocheAuthor
    """

    list_display = (
        "first_name",
        "last_name",
        "birth_date",
    )


@admin.register(FastocheGenre)
class FastocheGenreAdmin(admin.ModelAdmin):
    """
    Admin model for FastocheGenre
    """

    list_display = (
        "code",
        "designation",
        "help_text",
    )


@admin.register(FastocheBook)
class FastocheBookAdmin(admin.ModelAdmin):
    """
    Admin model for FastocheBook
    """

    pass
