from config import Config


DATABASE_CONFIG = {
    "connections": {"default": Config.DATABASE_URI},
    "apps": {
        "models": {
            "models": Config.APPS_MODELS,
            "default_connection": "default",
        }
    },
}


__all__ = [
    "DATABASE_CONFIG"
]
