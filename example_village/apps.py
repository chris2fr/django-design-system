from django.apps import AppConfig

from django.utils.translation import gettext_lazy as _


class ExampleDjangoVillageConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"  # type: ignore
    name = "example_village"
    verbose_name = _("Example village")
