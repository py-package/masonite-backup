from masonite.foundation import response_handler
from masonite.storage import StorageCapsule
from masonite.auth import Sign
from masonite.environment import LoadEnvironment
from masonite.utils.structures import load
from masonite.utils.location import base_path
from masonite.middleware import (
    SessionMiddleware,
    EncryptCookies,
    LoadUserMiddleware,
    MaintenanceModeMiddleware,
)
from masonite.routes import Route
from masonite.configuration.Configuration import Configuration
from masonite.configuration import config

from tests.integrations.app.middlewares import VerifyCsrfToken, AuthenticationMiddleware


class Kernel:

    http_middleware = [MaintenanceModeMiddleware, EncryptCookies]

    route_middleware = {
        "web": [SessionMiddleware, LoadUserMiddleware, VerifyCsrfToken],
        "auth": [AuthenticationMiddleware],
    }

    def __init__(self, app):
        self.application = app

    def register(self):
        # Register routes
        self.load_environment()
        self.register_configurations()
        self.register_middleware()
        self.register_routes()
        self.register_database()
        self.register_templates()
        self.register_storage()

    def load_environment(self):
        LoadEnvironment()

    def register_configurations(self):
        # load configuration
        self.application.bind("config.location", "tests/integrations/config")
        configuration = Configuration(self.application)
        configuration.load()
        self.application.bind("config", configuration)
        key = config("application.key")
        self.application.bind("key", key)
        self.application.bind("sign", Sign(key))
        # set locations
        self.application.bind("resources.location", "tests/integrations/resources/")
        self.application.bind("controllers.location", "tests/integrations/app/controllers")
        self.application.bind("jobs.location", "tests/integrations/app/jobs")
        self.application.bind("providers.location", "tests/integrations/app/providers")
        self.application.bind("mailables.location", "tests/integrations/app/mailables")
        self.application.bind("listeners.location", "tests/integrations/app/listeners")
        self.application.bind("validation.location", "tests/integrations/app/validation")
        self.application.bind("notifications.location", "tests/integrations/app/notifications")
        self.application.bind("events.location", "tests/integrations/app/events")
        self.application.bind("tasks.location", "tests/integrations/app/tasks")
        self.application.bind("models.location", "tests/integrations/app/models")
        self.application.bind("observers.location", "tests/integrations/app/models/observers")
        self.application.bind("policies.location", "tests/integrations/app/policies")
        self.application.bind("commands.location", "tests/integrations/app/commands")
        self.application.bind("middlewares.location", "tests/integrations/app/middlewares")

        self.application.bind("server.runner", "masonite.commands.ServeCommand.main")

    def register_middleware(self):
        self.application.make("middleware").add(self.route_middleware).add(self.http_middleware)

    def register_routes(self):
        Route.set_controller_locations(self.application.make("controllers.location"))
        self.application.bind("routes.location", "tests/integrations/routes/web")
        self.application.make("router").add(
            Route.group(
                load(self.application.make("routes.location"), "ROUTES"), middleware=["web"]
            )
        )

    def register_database(self):
        from masoniteorm.query import QueryBuilder

        self.application.bind(
            "builder",
            QueryBuilder(connection_details=config("database.databases")),
        )

        self.application.bind("migrations.location", "tests/integrations/databases/migrations")
        self.application.bind("seeds.location", "tests/integrations/databases/seeds")

        self.application.bind("resolver", config("database.db"))

    def register_templates(self):
        self.application.bind("views.location", "tests/integrations/templates/")

    def register_storage(self):
        storage = StorageCapsule()
        storage.add_storage_assets(config("filesystem.staticfiles"))
        self.application.bind("storage_capsule", storage)

        self.application.set_response_handler(response_handler)
        self.application.use_storage_path(base_path("storage"))
