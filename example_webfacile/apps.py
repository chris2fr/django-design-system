from django.apps import AppConfig

from django.utils.translation import gettext_lazy as _


class ExampleWebfastocheConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"  # type: ignore
    name = "example_webfastoche"
    verbose_name = _("Example webfastoche")
