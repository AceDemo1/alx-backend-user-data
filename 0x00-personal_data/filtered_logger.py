#!/usr/bin/env python3
"""returns the log message obfuscated"""
import re
import logging
import os
from typing import List
from mysql.connector import MySQLConnection

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """format"""
        record.msg = filter_datum(self.fields,
                                  self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """logger"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream = logging.StreamHandler()
    fomatter = RedactingFormatter(PII_FIELDS)
    stream.setFormatter(fomatter)
    logger.addHandler(stream)
    return logger


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    for i in fields:
        message = re.sub(f'{i}=.*?{separator}',
                         f'{i}={redaction}{separator}', message)
    return message


def get_db() -> MySQLConnection:
    """database"""
    usr = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    paswd = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db = os.getenv('PERSONAL_DATA_DB_NAME')
    con = MySQLConnection(user=usr, password=paswd, host=host, database=db)
    return con


def main() -> None:
    """main func"""
    con = get_db()
    logger = get_logger()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM users;')
    headings = cursor.column_names
    for i in cursor:
        msg = ''.join(f'{k}={v};' for k, v in zip(headings, i))
        logger.info(msg)
    cursor.close()
    con.close()


if __name__ == '__main__':
    main()
