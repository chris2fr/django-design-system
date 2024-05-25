from django.core.management.base import BaseCommand

from django_cefran.models import CefranConfig, CefranSocialMedia
from example_cefran.models import CefranGenre


class Command(BaseCommand):
    help = "Add some initial sample data for the example app."

    def handle(self, *args, **options):
        # Note: the command should be able to be run several times without creating
        # duplicate objects.
        config, _created = CefranConfig.objects.get_or_create(
            language="fr",
            defaults={
                "header_brand": "Django Cefran",
                "header_brand_html": "Django<br />Cefran",
                "footer_brand": "Django Cefran",
                "footer_brand_html": "Django<br />Cefran",
                "site_title": "Django-Cefran",
                "site_tagline": "Intégration du système de design WebFaciel sur la base de celui de l’État pour les sites utilisant Django",
                "footer_description": '<a href="https://github.com/chris2fr/django-cefran" \r\ntarget="_blank" rel="noreferrer noopener">Dépôt Github</a>',
                "mourning": False,
                "accessibility_status": "NOT",
                "newsletter_description": """Nous n’avons pas de lettre d’information mais vous pouvez trouver
                les dernières publications sur cette page.""",
                "newsletter_url": "https://github.com/chris2fr/django_cefran/releases",
            },
        )

        CefranSocialMedia.objects.get_or_create(
            site_config=config,
            title="Mastodon",
            url="https://social.numerique.gouv.fr/explore",
            icon_class="cefran-btn--mastodon",
        )

        CefranGenre.objects.get_or_create(code="SF", designation="Science-Fiction")
        CefranGenre.objects.get_or_create(
            code="FTSQUE",
            designation="Fantastique",
            help_text="Intrusion du surnaturel dans un cadre réaliste",
        )
        CefranGenre.objects.get_or_create(
            code="FTSY",
            designation="Fantasy",
            help_text="Élaboration d’un univers distinct du monde réel",
        )
