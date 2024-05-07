from django.apps import AppConfig

from django.utils.translation import gettext_lazy as _


class ExampleDsfacileConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"  # type: ignore
    name = "example_dsfacile"
    verbose_name = _("Example DSFacile")
