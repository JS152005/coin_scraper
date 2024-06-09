#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys

def main():
    """Run administrative tasks."""
    # Set the DJANGO_SETTINGS_MODULE environment variable
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coin_scraper.settings')

    try:
        # Import the execute_from_command_line function from Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Raise an error if Django is not installed or not available on the PYTHONPATH
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Check if the project settings are valid
    try:
        import coin_scraper.settings
    except ImportError as exc:
        print("Error: Unable to import project settings.")
        print("Make sure the settings module is correct and the project is properly configured.")
        sys.exit(1)

    # Execute the command-line utility
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()