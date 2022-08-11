import os
from masonite.commands import Command


class BackupRunCommand(Command):
    """
    Start the backup process.

    backup:run
        {--filename : Backup filename}
        {--only-db : Backup database only}
        {--only-files : Backup files only}
    """

    def __init__(self, application):
        super().__init__()
        self.app = application
        self.database_file_path = None
        self.assets_file_path = None

    def handle(self):
        backup = self.app.make("backup")

        if not self.validate_options():
            return

        self.info("============ Backup starting ============")

        if self.option("only-db"):
            self.database_file_path = backup.database()
        elif self.option("only-files"):
            self.assets_file_path = backup.files()
        else:
            self.info("Backuping database...")
            self.database_file_path = backup.database()
            self.info("Backuping files...")
            self.assets_file_path = backup.files()

            # delete the database file
            os.remove(self.database_file_path)
            self.database_file_path = None

        backup.email()
        self.info("============ Backup complete ============")

    def validate_options(self):
        if self.option("only-db") and self.option("only-files"):
            self.error("You can only pass either files or database backup option.")
            return False
        return True
