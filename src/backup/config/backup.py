# flake8: noqa F501
"""Backup Settings"""

from masonite.utils.location import base_path

"""
|--------------------------------------------------------------------------
| Masonite Backup
|--------------------------------------------------------------------------
|
| This is the configuration file for the Masonite Backup package.
|
"""

FILENAME = "backup"  # The filename of the backup file. (without the extension)
DIRECTORY = "backup"  # storage/backup
SOURCE = {
    "root": base_path(),
    "excludes": [
        ".git",
        "storage",
        "venv",
        "node_modules",
        "__pycache__",
    ],
}
