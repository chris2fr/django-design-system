from django.core.management.base import BaseCommand

import json
from bs4 import BeautifulSoup
from pathlib import Path
import os


class Command(BaseCommand):
    help = "Exports the whole site as a single JSON file."

    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    # BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
    # STATIC_ROOT = os.path.join(BASE_DIR, "docs/django_cfran")
    STATIC_ROOT = Path("docs", "django_cfran")

    def handle(self, *args, **options):
        # Path where django-distill puts the documentation
        output = []

        if not self.STATIC_ROOT.is_dir():
            raise FileNotFoundError(
                "The django-distill export directory {} was not found.".format(self.STATIC_ROOT)
            )

        for file in self.STATIC_ROOT.rglob("*.html"):
            result = self.get_page_content(file)
            if result:
                output.append(result)

        # Export to both the static dump and the regular app
        os.makedirs(self.STATIC_ROOT / "static/json", 0o755, True)
        with open(self.STATIC_ROOT / "static/json/search_data.json", "w") as data_file:
            json.dump(output, data_file, indent=4, sort_keys=True)

        with open("example_cfran/static/json/search_data.json", "w") as data_file:
            json.dump(output, data_file, indent=4, sort_keys=True)

    def get_page_content(self, file: str):
        filename = str(file).split("/")[-2]
        if filename == "django-cfran":
            filename = "homepage"

        if filename != "search":
            soup = BeautifulSoup(open(file), "lxml")
            title = soup.title.string.replace(
                "— Système de Design de l’État", ""
            ).strip()
            main = soup.find("main")

            if "Non implémenté" not in title:
                return {
                    "filename": filename,
                    "path": str(file)[4:],
                    "title": title,
                    "text": " ".join(main.get_text().split()),
                }
