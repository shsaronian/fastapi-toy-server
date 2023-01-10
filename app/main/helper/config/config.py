import configparser
import ast
import os


class Config:
    CONFIG_FILE_NAME = 'server-config.ini'
    CONFIG_READ_ONLY_FILE_PATH = 'app/assets/resources/server-config-read-only.ini'

    __server_config: dict = {}
    __is_initialized: bool = False

    @staticmethod
    def get(key: str):
        if Config.__is_initialized:
            if key.lower() in Config.__server_config:
                return Config.__server_config[key.lower()]
            else:
                raise AttributeError(f'Key {key} not found.')
        else:
            raise NotImplementedError('Config not initialized!')

    @staticmethod
    def initialize(file_path: str):
        config_file_path = os.path.join(file_path, Config.CONFIG_FILE_NAME)
        Config.__is_initialized = True
        if os.path.exists(config_file_path):
            server_config = Config.__config_to_dict(config_file_path)
            server_config_read_only = Config.__config_to_dict(Config.CONFIG_READ_ONLY_FILE_PATH)
            Config.__server_config = Config.__replace(server_config_read_only, server_config)
        else:
            Config.__server_config = Config.__config_to_dict(Config.CONFIG_READ_ONLY_FILE_PATH)

    @staticmethod
    def __config_to_dict(config_file: str):
        config_dict = {}
        config = configparser.ConfigParser()
        config.read(config_file)
        for section in config.sections():
            for key in config[section]:
                new_key = section.lower() + '.' + key.lower()
                config_dict[new_key] = ast.literal_eval(config[section][key])
        return config_dict

    @staticmethod
    def __replace(source: dict, destination: dict) -> dict:
        for key in source.keys():
            if key in destination.keys():
                source[key] = destination[key]
        return source
