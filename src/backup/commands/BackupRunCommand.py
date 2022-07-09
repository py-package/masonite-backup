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

    def handle(self):
        if not self.validate_options():
            return
        
        self.info("Starting backup...")

        if self.option("only-db"):
            self.app.make("backup").database()
        elif self.option("only-files"):
            self.app.make("backup").files()

        self.info("Backup complete...")

    def validate_options(self):
        if self.option("only-db") and self.option("only-files"):
            self.error("You can only pass either files or database backup option.")
            return False
        return True
