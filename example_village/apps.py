from django.apps import AppConfig

from django.utils.translation import gettext_lazy as _


class ExampleDjangoDesignSystemConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"  # type: ignore
    name = "example_design_system"
    verbose_name = _("Example design_system")
