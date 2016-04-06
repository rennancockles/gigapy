# -*- coding: utf-8 -*-


class Transportadora(object):

    def __init__(self, id=None, nome=''):
        self.id = id
        self.nome = nome

    def from_db(self, columns, row):
        id = row[columns.index('id')]
        nome = row[columns.index('nome')]

        self.id = id
        self.nome = nome

    def __str__(self):
        pattern = "\nId Transportadora: {0}" \
                  "\nNome: {1}"

        parameters = [self.id, self.nome]

        return pattern.format(*parameters)

