class ConfigurationManager:
    _instance = None

    def __init__(self):
        self._settings = self._load_settings()

    @staticmethod
    def get_instance():
        if ConfigurationManager._instance is None:
            ConfigurationManager._instance = ConfigurationManager()
        return ConfigurationManager._instance

    def get_setting(self, key):
        return self._settings.get(key)

    def _load_settings(self):
        return {
            "server_address": "127.0.0.1",
            "port": 8080,
            "max_connections": 100
        }


config_manager1 = ConfigurationManager.get_instance()
config_manager2 = ConfigurationManager.get_instance()


print(config_manager1 is config_manager2)


print(config_manager1.get_setting("server_address"))
print(config_manager2.get_setting("port"))
