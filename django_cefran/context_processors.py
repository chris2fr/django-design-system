from django_cefran.models import DjangoCefranConfig
from django.utils.translation import get_language
import os


def site_config(request):
    # Tries to return the site config object in the current language first.
    config = DjangoCefranConfig.objects.filter(language=get_language()).first()

    # Failing that, it returns the first site config object
    if not config:
        config = DjangoCefranConfig.objects.first()

    return {"SITE_CONFIG": config}

def urlangs(request):
    return{"URLANGS": [
        {
            'code': 'en',
            'name_local': 'English',
            'name': 'English',
            'bidi': False,
            'name_translated': 'English',
            'url': '/en/' if not os.getenv("URLANG_EN") else os.getenv("URLANG_EN"),
        },
        {
            'code': 'fr',
            'name_local': 'French',
            'name': 'Français',
            'bidi': False,
            'name_translated': 'Français',
            'url': '/' if not os.getenv("URLANG_FR") else os.getenv("URLANG_FR"),
        },
    ]}