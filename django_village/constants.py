from django.utils.translation import gettext_lazy as _

# List of languages for which the interface translation is currently available
DJANGO_DESIGN_SYSTEM_LANGUAGES = [
    ("en", _("English")),
    ("fr", _("French")),
]

# Color palettes, per https://www.systeme-de-design.gouv.fr/elements-d-interface/fondamentaux-de-l-identite-de-l-etat/couleurs-palette/

COLOR_CHOICES_PRIMARY = [
    ("design-system-primary", _("Couleur principale")),
    ("design-system-secondary", _("Couleur secondaire")),
]

COLOR_CHOICES_NEUTRAL = [
    ("grey", _("Grey")),
]

COLOR_CHOICES_SYSTEM = [
    ("info", _("Info")),
    ("success", _("Success")),
    ("warning", _("Warning")),
    ("error", _("Error")),
]

COLOR_CHOICES_ILLUSTRATION = [
    ("design-system-color3", "Couleur 3"),
    ("design-system-color4", "Couleur 4"),
    ("design-system-color5", "Couleur 5"),
    ("design-system-color6", "Couleur 6"),
    ("design-system-color7", "Couleur 7"),
    ("design-system-color8", "Couleur 8"),
    ("design-system-color9", "Couleur 9"),
    ("design-system-color10", "Couleur 10"),
    ("design-system-color11", "Couleur 11"),
    ("design-system-color12", "Couleur 12"),
    ("design-system-color13", "Couleur 13"),
    ("design-system-color14", "Couleur 14"),
    ("design-system-color15", "Couleur 15"),
    ("design-system-color16", "Couleur 16"),
    ("design-system-color17", "Couleur 17"),
    ("design-system-color18", "Couleur 18"),
    ("design-system-color19", "Couleur 19"),
    ("design-system-color20", "Couleur 20"),
]

COLOR_CHOICES = [
    (_("Primary colors"), COLOR_CHOICES_PRIMARY),
    (_("Neutral colors"), COLOR_CHOICES_NEUTRAL),
    (_("Illustration colors"), COLOR_CHOICES_ILLUSTRATION),
]

COLOR_CHOICES_WITH_SYSTEM = [
    (_("Primary colors"), COLOR_CHOICES_PRIMARY),
    (_("Neutral colors"), COLOR_CHOICES_NEUTRAL),
    (_("System colors"), COLOR_CHOICES_SYSTEM),
    (_("Illustration colors"), COLOR_CHOICES_ILLUSTRATION),
]
