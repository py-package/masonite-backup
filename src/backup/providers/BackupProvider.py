"""A BackupProvider Service Provider."""

from masonite.packages import PackageProvider
from ..Backup import Backup
from ..commands import BackupRunCommand


class BackupProvider(PackageProvider):
    def configure(self):
        """Register objects into the Service Container."""
        (self.root("backup").name("backup").config("config/backup.py", publish=True))

    def register(self):
        super().register()

        self.application.bind("backup", Backup(application=self.application))
        self.application.make("commands").add(BackupRunCommand(application=self.application))

    def boot(self):
        """Boots services required by the container."""
        pass
