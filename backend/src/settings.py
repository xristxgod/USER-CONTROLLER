from config import Config


TORTOISE_ORM = {
    "connections": {"default": Config.DATABASE_URI},
    "apps": {
        "models": {
            "models": Config.APPS_MODELS,
            "default_connection": "default",
        }
    },
}
