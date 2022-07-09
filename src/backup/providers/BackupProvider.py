"""A BackupProvider Service Provider."""

from masonite.packages import PackageProvider


class BackupProvider(PackageProvider):

    def configure(self):
        """Register objects into the Service Container."""
        (
            self.root("backup")
            .name("backup")
            .config("config/backup.py", publish=True)
        )

    def register(self):
        super().register()

    def boot(self):
        """Boots services required by the container."""
        pass
