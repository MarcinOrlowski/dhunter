# coding=utf8

"""

 dhunter

 Fast, content based duplicate file detector with cache and more!
 Copyright ©2018-2020 Marcin Orlowski <mail [@] MarcinOrlowski.com>

 https://github.com/MarcinOrlowski/dhunter

"""

import sqlite3
import typing
from abc import abstractmethod


class DbBase(object):

    def __init__(self, db_file_name: str):
        self._db = None
        self._db_file_name = db_file_name

    def __del__(self) -> None:
        self.db_disconnect()

    # ------------------------------------------------------------------------------------------------------------

    def db_connect(self):
        if self._db is None:
            self._db = sqlite3.connect(self._db_file_name)
            # self.db.isolation_level = 'EXCLUSIVE'
            # self.db.execute('BEGIN EXCLUSIVE')
            self._db.row_factory = sqlite3.Row

    def db_disconnect(self) -> None:
        if self._db is not None:
            self._db.commit()

            self._db.close()
            self._db = None

    # ------------------------------------------------------------------------------------------------------------

    # @property
    # def db(self) -> sqlite3.Connection:
    #     return self.__db
    #
    # @db.setter
    # def db(self, val: sqlite3.Connection or None) -> None:
    #     self.__db = val

    @abstractmethod
    def create_tables(self) -> None:
        raise NotImplementedError

    def _create_tables(self, queries: typing.List[str]) -> None:
        self.db_connect()
        _ = [self._db.cursor().execute(query) for query in queries]

    # ------------------------------------------------------------------------------------------------------------

    def insert(self, item):
        raise NotImplementedError

    def replace(self):
        raise NotImplementedError

    def remove(self):
        raise NotImplementedError
