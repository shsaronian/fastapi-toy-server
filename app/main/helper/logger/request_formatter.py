import logging
from logging import LogRecord

from app.main.util.request_vars import g, has_request_context


class RequestFormatter(logging.Formatter):

    def __init__(self, formatter: str, general_formatter: str, general_name: [str], without_request_id_formatter: str, without_request_id_name: [str]) -> None:
        super().__init__(formatter)
        self.__formatter = formatter
        self.__general_formatter = general_formatter
        self.__general_name = general_name
        self.__without_request_id_formatter = without_request_id_formatter
        self.__without_request_id_name = without_request_id_name

    def format(self, record: LogRecord) -> str:
        if record.name in self.__general_name:
            self._fmt = self.__general_formatter
            self._style._fmt = self.__general_formatter
        elif record.name in self.__without_request_id_name:
            self._fmt = self.__without_request_id_formatter
            self._style._fmt = self.__without_request_id_formatter
        else:
            self._fmt = self.__formatter
            self._style._fmt = self.__formatter
        if has_request_context():
            record.request_id = g.get()
        else:
            record.request_id = None

        return super().format(record)
