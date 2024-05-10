from django.core.management.base import BaseCommand
import json
import os


class Command(BaseCommand):
    help = "Add some initial sample data for the example app."

    def handle(self, *args, **options):
        # Note: the command should be able to be run several times without creating
        # duplicate objects.
        icons_root = "webfastoche/static/webfastoche/dist/icons/"
        icons_folders = os.listdir(icons_root)
        icons_folders.sort()

        json_root = (
            "webfastoche/static/django-webfastoche/icon-picker/assets/icons-libraries/"
        )

        all_folders = []

        for folder in icons_folders:
            icons_dict = {
                "prefix": "webfastoche-icon-",
                "version": "1.11.2",
                "icons": [],
            }

            files = os.listdir(os.path.join(icons_root, folder))
            files_without_extensions = [
                f.split(".")[0].replace("webfastoche--", "") for f in files
            ]
            files_without_extensions.sort()

            webfastoche_folder = f"webfastoche-{folder}"
            webfastoche_folder_json = webfastoche_folder + ".json"
            icons_dict["icons"] = files_without_extensions
            icons_dict["icon-style"] = webfastoche_folder
            icons_dict["list-label"] = f"webfastoche {folder.title()}"

            all_folders.append(webfastoche_folder_json)

            json_file = os.path.join(json_root, webfastoche_folder_json)
            with open(json_file, "w") as fp:
                json.dump(icons_dict, fp)

        print("Folders created or updated: ", all_folders)
