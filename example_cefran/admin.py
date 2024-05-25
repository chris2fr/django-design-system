from django.contrib import admin

from example_cefran.models import CefranAuthor, CefranGenre, CefranBook


# Register your models here.
@admin.register(CefranAuthor)
class CefranAuthorAdmin(admin.ModelAdmin):
    """
    Admin model for CefranAuthor
    """

    list_display = (
        "first_name",
        "last_name",
        "birth_date",
    )


@admin.register(CefranGenre)
class CefranGenreAdmin(admin.ModelAdmin):
    """
    Admin model for CefranGenre
    """

    list_display = (
        "code",
        "designation",
        "help_text",
    )


@admin.register(CefranBook)
class CefranBookAdmin(admin.ModelAdmin):
    """
    Admin model for CefranBook
    """

    pass
