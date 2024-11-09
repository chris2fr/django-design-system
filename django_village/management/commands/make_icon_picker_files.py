from django.core.management.base import BaseCommand
import json
import os


class Command(BaseCommand):
    help = "Add some initial sample data for the example app."

    def handle(self, *args, **options):
        # Note: the command should be able to be run several times without creating
        # duplicate objects.
        icons_root = "django_django_design_system/static/design-system/dist/icons/"
        icons_folders = os.listdir(icons_root)
        icons_folders.sort()

        json_root = (
            "django_design_system/static/django_design_system/icon-picker/assets/icons-libraries/"
        )

        all_folders = []

        for folder in icons_folders:
            icons_dict = {
                "prefix": "design-system-icon-",
                "version": "1.11.2",
                "icons": [],
            }

            files = os.listdir(os.path.join(icons_root, folder))
            files_without_extensions = [
                f.split(".")[0].replace("design-system--", "") for f in files
            ]
            files_without_extensions.sort()

            design_system_folder = f"design-system-{folder}"
            design_system_folder_json = design_system_folder + ".json"
            icons_dict["icons"] = files_without_extensions
            icons_dict["icon-style"] = design_system_folder
            icons_dict["list-label"] = f"design_system {folder.title()}"

            all_folders.append(design_system_folder_json)

            json_file = os.path.join(json_root, design_system_folder_json)
            with open(json_file, "w") as fp:
                json.dump(icons_dict, fp)

        print("Folders created or updated: ", all_folders)
