import os

from fastapi import FastAPI

from . import __version__
from .helper.config.config import Config
from .helper.logger.logger import Logger

server_name = "FastAPI Toy Server"
config_env_name = "FAST_API_TOY_SERVER_ENV"
fast_api_env = "FAST_API_ENV"


def init_config():
    Config.initialize(os.environ[config_env_name])


def init_logger():
    Logger.initialize(Config.get('Logger.level'),
                      Config.get('Logger.path'),
                      Config.get('Logger.maxFileSize'),
                      Config.get('Logger.logToConsole'),
                      Config.get('Logger.logToFile'))
    __logger: Logger = Logger.get_logger(Logger.GENERAL)
    __logger.info("Logger initialized")
    if os.path.exists(os.path.join(os.environ[config_env_name], Config.CONFIG_FILE_NAME)):
        __logger.info(f"Loading configs from path: {os.environ[config_env_name]}")
    else:
        __logger.warning(f"Config file not found!, loading base configs from : {Config.CONFIG_READ_ONLY_FILE_PATH}")
    __logger.info(f"Starting {server_name}")


def is_debug():
    env = os.getenv(fast_api_env)
    if env is None or env == "":
        raise Exception(f"{fast_api_env} is not set, please set it to `production` or `development`")
    if env.lower() == 'development':
        return True
    elif env.lower() == "production":
        return False
    else:
        raise Exception(f"{fast_api_env} must be `production` or `development`")


def create_app() -> FastAPI:
    app = FastAPI(title=server_name, version=__version__, debug=is_debug())
    Logger.get_logger(Logger.GENERAL).info(f"Server started successfully")
    return app
