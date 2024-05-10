from django.core.management.base import BaseCommand

from django_webfastoche.models import WebfastocheConfig, WebfastocheSocialMedia
from example_webfastoche.models import WebfastocheGenre


class Command(BaseCommand):
    help = "Add some initial sample data for the example app."

    def handle(self, *args, **options):
        # Note: the command should be able to be run several times without creating
        # duplicate objects.
        config, _created = WebfastocheConfig.objects.get_or_create(
            language="fr",
            defaults={
                "header_brand": "Django WebFastoche",
                "header_brand_html": "Django<br />WebFastoche",
                "footer_brand": "Django WebFastoche",
                "footer_brand_html": "Django<br />WebFastoche",
                "site_title": "Django-Webfastoche",
                "site_tagline": "Intégration du système de design WebFaciel sur la base de celui de l’État pour les sites utilisant Django",
                "footer_description": '<a href="https://github.com/chris2fr/django-webfastoche" \r\ntarget="_blank" rel="noreferrer noopener">Dépôt Github</a>',
                "mourning": False,
                "accessibility_status": "NOT",
                "newsletter_description": """Nous n’avons pas de lettre d’information mais vous pouvez trouver
                les dernières publications sur cette page.""",
                "newsletter_url": "https://github.com/chris2fr/django-webfastoche/releases",
            },
        )

        WebfastocheSocialMedia.objects.get_or_create(
            site_config=config,
            title="Mastodon",
            url="https://social.numerique.gouv.fr/explore",
            icon_class="webfastoche-btn--mastodon",
        )

        WebfastocheGenre.objects.get_or_create(code="SF", designation="Science-Fiction")
        WebfastocheGenre.objects.get_or_create(
            code="FTSQUE",
            designation="Fantastique",
            help_text="Intrusion du surnaturel dans un cadre réaliste",
        )
        WebfastocheGenre.objects.get_or_create(
            code="FTSY",
            designation="Fantasy",
            help_text="Élaboration d’un univers distinct du monde réel",
        )
