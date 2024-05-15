from django.apps import AppConfig

from django.utils.translation import gettext_lazy as _


class ExampleCfranConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"  # type: ignore
    name = "example_cfran"
    verbose_name = _("Example cfran")
