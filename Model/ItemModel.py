# -*- coding: utf-8 -*-


class Item(object):

    def __init__(self, id=None, quantidade=0.0, valor=0.0, produto=None):
        self.id = id
        self.quantidade = quantidade
        self.valor = valor
        self.produto = produto

    def from_db(self, columns, row):
        id = row[columns.index('id')]
        quantidade = row[columns.index('quantidade')]
        valor = row[columns.index('valor')]

        self.id = id
        self.quantidade = quantidade
        self.valor = valor

    def add_produto(self, produto):
        self.produto = produto

    def __str__(self):
        pattern = "\nId Item: {0}" \
                  "\nQuantidade: {1}" \
                  "\nValor: {2}" \
                  "{3}"

        parameters = [self.id, self.quantidade, self.valor, self.produto]

        return pattern.format(*parameters)

    def __repr__(self):
        return self.__str__() + '\n'


