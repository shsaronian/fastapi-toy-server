import time

from app.main.helper.logger.logger import Logger

__logger: Logger = Logger.get_logger(__name__)


def time_logger(name: str):
    def decorator(function):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = function(*args, **kwargs)
            total_time = int((time.time() - start) * 1000)
            __logger.debug(f"{name} execution took: {total_time}ms")
            return result

        return wrapper

    return decorator
