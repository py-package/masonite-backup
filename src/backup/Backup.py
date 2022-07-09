# flake8: noqa F501
import pathlib
import shutil
import tempfile
from unittest.mock import patch
from masonite.configuration import config
from shutil import make_archive
from datetime import datetime
from masonite.utils.location import base_path
import subprocess
import gzip


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

        db_config = config("database.databases")
        default = db_config.get("default")
        connection = db_config.get(default)
        driver = connection.get("driver")

        db_file_path = base_path(
            "{}.gz".format("database-" + str(datetime.timestamp(datetime.now())))
        )

        if driver == "sqlite":
            pass
        elif driver == "mysql":
            command_str = f"mysqldump -u {connection.get('user')} -p{connection.get('password')} {connection.get('database')}"

        elif driver == "postgres":
            command_str = f"pg_dump -U{connection.get('user')} -h{connection.get('host')} -p{connection.get('port')} -d{connection.get('database')}"

        elif driver == "mssql":
            command_str = f"sqlcmd -S{connection.get('host')} -U{connection.get('user')} -P{connection.get('port')} -d{connection.get('database')}"

        elif driver == "sqlserver":
            command_str = f"sqlcmd -S{connection.get('host')} -U{connection.get('user')} -P{connection.get('port')} -d{connection.get('database')}"

        elif driver == "oracle":
            command_str = f"sqlplus -S{connection.get('user')}/{connection.get('password')}@{connection.get('host')}:{connection.get('port')}/{connection.get('database')}"

        if command_str:
            with gzip.open(db_file_path, "wb") as f:
                popen = subprocess.Popen(
                    [command_str],
                    stdout=subprocess.PIPE,
                    shell=True,
                    universal_newlines=True,
                )
                for stdout_line in iter(popen.stdout.readline, ""):
                    f.write(stdout_line.encode("utf-8"))
                popen.stdout.close()
                popen.wait()
        return db_file_path

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
                pathlib.Path(tmp).joinpath("backup"),
                ignore=shutil.ignore_patterns(*self.backup_config.get("source").get("excludes")),
            )

            with patch("os.path.isfile", side_effect=self.accept):
                make_archive(path_to_archive, "zip", tmp)
        return path_to_archive
