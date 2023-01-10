import re
from logging import LogRecord
from logging.handlers import WatchedFileHandler, TimedRotatingFileHandler, RotatingFileHandler


class TimedAndSizeRotatingFileHandler(WatchedFileHandler, TimedRotatingFileHandler, RotatingFileHandler):

    def __init__(self,
                 filename: str,
                 mode='a',
                 when='h',
                 utc=False,
                 maxBytes=0,
                 backupCount=0,
                 interval=1,
                 encoding=None,
                 delay=False) -> None:
        WatchedFileHandler.__init__(self, filename=filename, mode=mode)
        RotatingFileHandler.__init__(self, filename=filename, mode=mode, maxBytes=maxBytes)
        TimedRotatingFileHandler.__init__(self,
                                          filename=filename,
                                          when=when,
                                          interval=interval,
                                          backupCount=backupCount,
                                          encoding=encoding,
                                          delay=delay,
                                          utc=utc)
        self.suffix = "%Y-%m-%d_%H-%M-%S"
        self.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}(\.\w+)?$", re.ASCII)

    def shouldRollover(self, record):
        return TimedRotatingFileHandler.shouldRollover(self, record) or RotatingFileHandler.shouldRollover(self, record)

    def doRollover(self) -> None:
        TimedRotatingFileHandler.doRollover(self)

    def emit(self, record: LogRecord) -> None:
        WatchedFileHandler.reopenIfNeeded(self)
        TimedRotatingFileHandler.emit(self, record)
