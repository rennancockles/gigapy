# -*- coding: utf-8 -*-


class Email(object):

    def __init__(self, id=None, email='', referencia=''):
        self.id = id
        self.email = email
        self.referencia = referencia

    def from_db(self, columns, row):
        id = row[columns.index('id')]
        email = row[columns.index('email')]
        referencia = row[columns.index('referencia')]

        self.id = id
        self.email = email
        self.referencia = referencia

    def __str__(self):
        pattern = "\nId Email: {0}" \
                  "\nEmail: {1}" \
                  "\nReferência: {2}"

        parameters = [self.id, self.email, self.referencia]

        return pattern.format(*parameters)

    def __repr__(self):
        return self.__str__() + '\n'

