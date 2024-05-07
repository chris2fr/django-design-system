from django.contrib import admin

from example_dsfacile.models import DsfacileAuthor, DsfacileGenre, DsfacileBook


# Register your models here.
@admin.register(DsfacileAuthor)
class DsfacileAuthorAdmin(admin.ModelAdmin):
    """
    Admin model for DsfacileAuthor
    """

    list_display = (
        "first_name",
        "last_name",
        "birth_date",
    )


@admin.register(DsfacileGenre)
class DsfacileGenreAdmin(admin.ModelAdmin):
    """
    Admin model for DsfacileGenre
    """

    list_display = (
        "code",
        "designation",
        "help_text",
    )


@admin.register(DsfacileBook)
class DsfacileBookAdmin(admin.ModelAdmin):
    """
    Admin model for DsfacileBook
    """

    pass
