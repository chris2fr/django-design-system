from django_cfran.models import CfranConfig
from django.utils.translation import get_language


def site_config(request):
    # Tries to return the site config object in the current language first.
    config = CfranConfig.objects.filter(language=get_language()).first()

    # Failing that, it returns the first site config object
    if not config:
        config = CfranConfig.objects.first()

    return {"SITE_CONFIG": config}
