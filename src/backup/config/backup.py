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

FILENAME = "backup"
DIRECTORY = "backup"
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
