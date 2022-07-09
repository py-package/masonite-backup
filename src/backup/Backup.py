import pathlib
import shutil
import tempfile
from unittest.mock import patch
from masonite.configuration import config
from shutil import make_archive
from datetime import datetime
from masonite.utils.location import base_path


class Backup:
    def __init__(self, application) -> None:
        self.app = application
        self.backup_config = config("backup")

    def accept(self, path):
        for pattern in self.backup_config.get("source").get("excludes"):
            if pattern in path:
                return False
        return True

    def database(self):
        """
        Backup the database.
        """
        pass

    def files(self):
        """
        Backup the files.
        """
        filename = (
            self.backup_config.get("filename", "backup")
            + "-"
            + str(datetime.timestamp(datetime.now()))
        )

        output_dir = base_path("storage/backup")

        if not pathlib.Path(output_dir).exists():
            pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)

        path_to_archive = pathlib.Path(output_dir).joinpath(filename)

        with tempfile.TemporaryDirectory() as tmp:
            shutil.copytree(
                self.backup_config.get("source").get("root"),
                pathlib.Path(tmp).joinpath("temporary_backup"),
                ignore=shutil.ignore_patterns(*self.backup_config.get("source").get("excludes")),
            )

            with patch("os.path.isfile", side_effect=self.accept):
                make_archive(path_to_archive, "zip", tmp)
