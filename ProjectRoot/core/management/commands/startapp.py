from django.core.management.commands.startapp import Command as StartAppCommand
from ..helper import Utile


class Command(StartAppCommand):
    """
    Custom Django Management Command to Extend the StartApp Command.

    This command overrides the default Django `startapp` command to include
    additional functionality that automatically creates a specific file
    during the application creation process.

    Usage:
        To use this command, run the following in your terminal:

            python manage.py <command_name> <app_name> [options]

        Replace <command_name> with the name of this custom command and
        <app_name> with the desired name of the new Django application.

    Attributes:
        help (str): A description of the command's purpose.

    Methods:
        handle(*args, **kwargs):
            Executes the command to create a new Django application and
            perform additional tasks, such as creating a file.

        __init__():
            Initializes the command and sets up any necessary attributes.

    Notes:
        - This command requires the `Utile` class from the `helper` module
          for its additional functionalities.
        - Ensure that the `Utile.custom_method_to_added_file_with_start_app`
          method and `Utile.create_file` are implemented correctly to avoid
          errors during execution.

    Examples:
        To create a new app called "mynewapp" and automatically create
        an additional file, use the following command:

            python manage.py startapp mynewapp
    """

    help = "Custom startapp command that automatically creates a file"

    def __init__(self):
        super().__init__()
        self.object = StartAppCommand()

    def handle(self, *args, **kwargs):
        # ---------------------------------------------------
        # Don't mashup this order: Ensure correct sequence
        # ---------------------------------------------------

        # Here all your basic processing
        app_name, app_dir, urls_file_path = (
            Utile.custom_method_to_added_file_with_start_app(**kwargs)
        )

        # ---------------------------------------------------
        # After processing, run this line so StartAppCommand
        # class performs the necessary task
        # ---------------------------------------------------
        super().handle(**kwargs)  # This line creates the <app_folder> and <files>.

        # ---------------------------------------------------
        # After the processing, perform other tasks, like
        # creating a file
        # ---------------------------------------------------
        Utile.create_file(app_name, app_dir, urls_file_path, self.object)
