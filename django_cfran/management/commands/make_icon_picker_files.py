from django.core.management.base import BaseCommand
import json
import os


class Command(BaseCommand):
    help = "Add some initial sample data for the example app."

    def handle(self, *args, **options):
        # Note: the command should be able to be run several times without creating
        # duplicate objects.
        icons_root = "fastoche/static/fastoche/dist/icons/"
        icons_folders = os.listdir(icons_root)
        icons_folders.sort()

        json_root = (
            "fastoche/static/django-fastoche/icon-picker/assets/icons-libraries/"
        )

        all_folders = []

        for folder in icons_folders:
            icons_dict = {
                "prefix": "fastoche-icon-",
                "version": "1.11.2",
                "icons": [],
            }

            files = os.listdir(os.path.join(icons_root, folder))
            files_without_extensions = [
                f.split(".")[0].replace("fastoche--", "") for f in files
            ]
            files_without_extensions.sort()

            fastoche_folder = f"fastoche-{folder}"
            fastoche_folder_json = fastoche_folder + ".json"
            icons_dict["icons"] = files_without_extensions
            icons_dict["icon-style"] = fastoche_folder
            icons_dict["list-label"] = f"fastoche {folder.title()}"

            all_folders.append(fastoche_folder_json)

            json_file = os.path.join(json_root, fastoche_folder_json)
            with open(json_file, "w") as fp:
                json.dump(icons_dict, fp)

        print("Folders created or updated: ", all_folders)
