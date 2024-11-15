from pathlib import Path

from django import forms
from django.forms import Form
from django.forms.renderers import DjangoTemplates, get_default_renderer
from django.utils.functional import cached_property

from django_design_system.utils import design_system_input_class_attr

from django_design_system.constants import COLOR_CHOICES_ILLUSTRATION



class DesignSystemDjangoTemplates(DjangoTemplates):
    @cached_property
    def engine(self):
        return self.backend(
            {
                "APP_DIRS": True,
                "DIRS": [
                    Path(__file__).resolve().parent / self.backend.app_dirname,
                    Path(forms.__path__[0]).resolve() / "templates",
                ],
                "NAME": "djangoforms",
                "OPTIONS": {},
            }
        )


class DesignSystemBaseForm(Form):
    """
    A base form that adds the necessary class on relevant fields
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            design_system_input_class_attr(visible)

    @property
    def default_renderer(self):
        from django.conf import settings, global_settings

        return (
            DesignSystemDjangoTemplates  # Settings wasn't modified
            if settings.FORM_RENDERER == global_settings.FORM_RENDERER
            else get_default_renderer()
        )

    def set_autofocus_on_first_error(self):
        """
        Sets the autofocus on the first field with an error message.
        Not included in the __init__ by default because it can cause some side effects on
        non-standard fields/forms.
        """
        for field in self.errors.keys():
            self.fields[field].widget.attrs.update({"autofocus": ""})
            break


class ColorForm(DesignSystemBaseForm):
    color = forms.ChoiceField(
        label="Choisissez une couleur",
        required=False,
        choices=[("", "----")] + COLOR_CHOICES_ILLUSTRATION,
    )
