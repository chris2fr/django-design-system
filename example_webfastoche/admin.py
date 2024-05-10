from django.contrib import admin

from example_webfastoche.models import WebfastocheAuthor, WebfastocheGenre, WebfastocheBook


# Register your models here.
@admin.register(WebfastocheAuthor)
class WebfastocheAuthorAdmin(admin.ModelAdmin):
    """
    Admin model for WebfastocheAuthor
    """

    list_display = (
        "first_name",
        "last_name",
        "birth_date",
    )


@admin.register(WebfastocheGenre)
class WebfastocheGenreAdmin(admin.ModelAdmin):
    """
    Admin model for WebfastocheGenre
    """

    list_display = (
        "code",
        "designation",
        "help_text",
    )


@admin.register(WebfastocheBook)
class WebfastocheBookAdmin(admin.ModelAdmin):
    """
    Admin model for WebfastocheBook
    """

    pass
