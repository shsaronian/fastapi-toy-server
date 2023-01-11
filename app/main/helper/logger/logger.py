import logging
import logging.handlers


from app.main.helper.logger.request_formatter import RequestFormatter


class Logger:
    GENERAL = 'GENERAL'

    __general_formatter = '[%(levelname)s] [%(asctime)s] [process_pid:%(process)d] %(message)s'
    __without_request_id_formatter = '[%(levelname)s] [%(asctime)s] [thread:%(thread)d] [%(name)s] %(message)s'
    __formatter = '[%(levelname)s] [%(asctime)s] [thread:%(thread)d] [request_id:%(request_id)s] [%(name)s]\n\t%(message)s'

    __name_to_level = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL
    }

    __loggers = {}
    __is_initialized: bool = False

    @staticmethod
    def initialize(level: str, log_to_console: bool):
        Logger.__is_initialized = True
        # Disable other module's loggers
        logging.getLogger('asyncio').setLevel(50)
        logging.getLogger('uvicorn.error').disabled = True
        logging.getLogger('uvicorn.access').disabled = True
        logger_format = RequestFormatter(formatter=Logger.__formatter,
                                         general_formatter=Logger.__general_formatter,
                                         general_name=[Logger.GENERAL],
                                         without_request_id_formatter=Logger.__without_request_id_formatter,
                                         without_request_id_name=[
                                             'httpx._client'])
        handlers = []
        if log_to_console:
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(logger_format)
            handlers.append(stream_handler)

        logging.basicConfig(level=Logger.__check_level(level), handlers=handlers)

    @staticmethod
    def get_logger(name: str):
        if not Logger.__is_initialized:
            raise NotImplementedError("Logger has not been initialized yet, call `initialize` method first")
        if name in Logger.__loggers:
            return Logger.__loggers[name]
        logger: Logger = Logger(logging.getLogger(name))
        Logger.__loggers[name] = logger
        return logger

    def __init__(self, logger: logging.Logger):
        self.__logger: logging.Logger = logger

    def debug(self, message: str) -> None:
        self.__logger.debug(message)

    def info(self, message: str) -> None:
        self.__logger.info(message)

    def warning(self, message: str) -> None:
        self.__logger.warning(message)

    def error(self, message: str) -> None:
        self.__logger.error(message)

    def exception(self, message: str) -> None:
        self.__logger.exception(message)

    def critical(self, message: str) -> None:
        self.__logger.critical(message)

    def __add_handler(self, handler: logging.Handler) -> None:
        self.__logger.addHandler(handler)

    def __set_level(self, level: int) -> None:
        self.__logger.setLevel(level)

    @staticmethod
    def __check_level(level: str) -> int:
        if str(level) == level:
            if level in Logger.__name_to_level:
                return Logger.__name_to_level[level]
            else:
                raise ValueError("Logger level is not valid: %r" % level)
        else:
            raise TypeError("Logger level must be a valid string: %r" % level)
