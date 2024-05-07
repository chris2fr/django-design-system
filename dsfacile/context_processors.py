from dsfacile.models import dsfacileConfig
from django.utils.translation import get_language


def site_config(request):
    # Tries to return the site config object in the current language first.
    config = dsfacileConfig.objects.filter(language=get_language()).first()

    # Failing that, it returns the first site config object
    if not config:
        config = dsfacileConfig.objects.first()

    return {"SITE_CONFIG": config}
