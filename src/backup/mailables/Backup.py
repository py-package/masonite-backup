# flake8: noqa F501
from masonite.mail import Mailable
from masonite.configuration import config
from masonite.environment import env


class Backup(Mailable):
    def build(self):
        backup_config = config("backup")
        email = backup_config.get("email_backup_to")

        if not email:
            raise Exception("No email address found in backup config.")

        return (
            self.to(email)
            .subject(backup_config.get("email_subject"))
            .from_(env("MAIL_FROM"))
            .html(
                """
                <div>
                    <h2 style="margin-bottom: 24px">Backup Complete</h2>
                    <p style="margin-bottom: 24px">
                    Your backup has been completed and is now available for download.<br />Please, find the file attached here within.
                    </p><br />
                    <i>Thanks,<br /> <strong>Masonite Backup</strong></i>
                </div>
            """
            )
        )
