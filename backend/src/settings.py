from config import Config


APPS_MODELS = [
    "src.models",
    "aerich.models"
]


DATABASE_CONFIG = {
    "connections": {"default": Config.DATABASE_URI},
    "apps": {
        "models": {
            "models": APPS_MODELS,
            "default_connection": "default",
        }
    },
}


__all__ = [
    "DATABASE_CONFIG"
]
