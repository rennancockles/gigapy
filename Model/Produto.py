# -*- coding: utf-8 -*-


class Produto(object):

    def __init__(self, id=None, nome='', descricao='', fornecedor=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.fornecedor = fornecedor

    def from_db(self, columns, row):
        id = row[columns.index('id')]
        nome = row[columns.index('nome')]
        descricao = row[columns.index('descricao')]

        self.id = id
        self.nome = nome
        self.descricao = descricao

    def add_fornecedor(self, fornecedor):
        self.fornecedor = fornecedor

    def __str__(self):
        pattern = "\nId Produto: {0}" \
                  "\nNome: {1}" \
                  "\nDescrição: {2}" \
                  "{3}"

        parameters = [self.id, self.nome, self.descricao, self.fornecedor]

        return pattern.format(*parameters)
