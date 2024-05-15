from django.contrib import admin

from example_cfran.models import CfranAuthor, CfranGenre, CfranBook


# Register your models here.
@admin.register(CfranAuthor)
class CfranAuthorAdmin(admin.ModelAdmin):
    """
    Admin model for CfranAuthor
    """

    list_display = (
        "first_name",
        "last_name",
        "birth_date",
    )


@admin.register(CfranGenre)
class CfranGenreAdmin(admin.ModelAdmin):
    """
    Admin model for CfranGenre
    """

    list_display = (
        "code",
        "designation",
        "help_text",
    )


@admin.register(CfranBook)
class CfranBookAdmin(admin.ModelAdmin):
    """
    Admin model for CfranBook
    """

    pass
