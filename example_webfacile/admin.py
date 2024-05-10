from django.contrib import admin

from example_webfacile.models import WebfacileAuthor, WebfacileGenre, WebfacileBook


# Register your models here.
@admin.register(WebfacileAuthor)
class WebfacileAuthorAdmin(admin.ModelAdmin):
    """
    Admin model for WebfacileAuthor
    """

    list_display = (
        "first_name",
        "last_name",
        "birth_date",
    )


@admin.register(WebfacileGenre)
class WebfacileGenreAdmin(admin.ModelAdmin):
    """
    Admin model for WebfacileGenre
    """

    list_display = (
        "code",
        "designation",
        "help_text",
    )


@admin.register(WebfacileBook)
class WebfacileBookAdmin(admin.ModelAdmin):
    """
    Admin model for WebfacileBook
    """

    pass
