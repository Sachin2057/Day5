from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass


class FileLogger(Logger):
    def log(self, message):
        with open('log.txt', 'a') as file:
            file.write(message + '\n')


class ConsoleLogger(Logger):
    def log(self, message):
        print(message)


class DatabaseLogger(Logger):
    def log(self, message):
        pass


class LoggerFactory:
    @staticmethod
    def get_logger(logger_type):
        if logger_type == 'file':
            return FileLogger()
        elif logger_type == 'console':
            return ConsoleLogger()
        elif logger_type == 'database':
            return DatabaseLogger()
        else:
            raise ValueError("Invalid logger type")


if __name__ == "__main__":
    file_logger = LoggerFactory.get_logger('file')
    console_logger = LoggerFactory.get_logger('console')
    database_logger = LoggerFactory.get_logger('database')
    file_logger.log("This is a log message written to a file")
    console_logger.log("This is a log message printed to the console")
    database_logger.log("This is a log message saved to a database")
