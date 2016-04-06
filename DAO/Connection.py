# -*- coding: utf-8 -*-

import MySQLdb


class Connection(object):

    def __init__(self):

        self.db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                                  user="root",  # your username
                                  passwd="123",  # your password
                                  db="gigapy")  # name of the data base

        self.cursor = self.db.cursor()

    def close_connection(self):
        self.cursor.close()
        self.db.close()

conn = Connection()
