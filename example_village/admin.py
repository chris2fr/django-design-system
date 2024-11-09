from django.contrib import admin

from example_design_system.models import DesignSystemAuthor, DesignSystemGenre, DesignSystemBook


# Register your models here.
@admin.register(DesignSystemAuthor)
class DesignSystemAuthorAdmin(admin.ModelAdmin):
    """
    Admin model for DesignSystemAuthor
    """

    list_display = (
        "first_name",
        "last_name",
        "birth_date",
    )


@admin.register(DesignSystemGenre)
class DesignSystemGenreAdmin(admin.ModelAdmin):
    """
    Admin model for DesignSystemGenre
    """

    list_display = (
        "code",
        "designation",
        "help_text",
    )


@admin.register(DesignSystemBook)
class DesignSystemBookAdmin(admin.ModelAdmin):
    """
    Admin model for DesignSystemBook
    """

    pass
