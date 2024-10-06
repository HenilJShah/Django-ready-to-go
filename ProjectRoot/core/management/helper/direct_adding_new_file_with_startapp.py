import os

from django.core.management.base import CommandError


class Utile:

    @staticmethod
    def custom_method_to_added_file_with_start_app(**kwargs):
        # Get the app name from the first argument
        if not kwargs.get("name"):
            raise CommandError("You must provide an app name.")
        app_name = kwargs.get("name")

        # Define the path for the new urls.py file
        app_dir = os.path.join(os.getcwd(), app_name)
        urls_file_path = os.path.join(app_dir, "urls.py")

        return app_name, app_dir, urls_file_path

    @staticmethod
    def create_file(app_name, app_dir, urls_file_path, object):
        # Check if the app was successfully created and create the urls.py file
        try:
            if os.path.exists(app_dir):
                print(app_dir, urls_file_path)
                # Create the urls.py file with some boilerplate code
                with open(urls_file_path, "w") as urls_file:
                    urls_file.write(
                        "from django.urls import path\n\n"
                        "urlpatterns = [\n"
                        "    # Add your URL patterns here\n"
                        "]\n"
                    )
                object.stdout.write(
                    object.style.SUCCESS(
                        f'Successfully created urls.py for app "{app_name}".'
                    )
                )
        except Exception as e:
            print(f'Failed to create the app "{e}".')
