# -*- coding: utf-8 -*-


class Telefone(object):

    def __init__(self, id=None, ddd='', numero='', referencia=''):
        self.id = id
        self.ddd = ddd
        self.numero = numero
        self.referencia = referencia

    def from_db(self, columns, row):
        id = row[columns.index('id')]
        ddd = row[columns.index('ddd')]
        numero = row[columns.index('numero')]
        referencia = row[columns.index('referencia')]

        self.id = id
        self.ddd = ddd
        self.numero = numero
        self.referencia = referencia

    def __str__(self):
        pattern = "\nId Telefone: {0}" \
                  "\nDDD: {1}" \
                  "\nNúmero: {2}" \
                  "\nReferência: {3}"

        parameters = [self.id, self.ddd, self.numero, self.referencia]

        return pattern.format(*parameters)

    def __repr__(self):
        return self.__str__() + '\n'


