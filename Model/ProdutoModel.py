# -*- coding: utf-8 -*-


class Produto(object):

    def __init__(self, id=None, nome='', descricao='', valor=0.0, fornecedor=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.fornecedor = fornecedor

    def from_db(self, columns, row):
        id = row[columns.index('id')]
        nome = row[columns.index('nome')]
        valor = row[columns.index('valor')]
        descricao = row[columns.index('descricao')]

        self.id = id
        self.nome = nome
        self.valor = valor
        self.descricao = descricao

    def add_fornecedor(self, fornecedor):
        self.fornecedor = fornecedor

    def __str__(self):
        pattern = "\nId Produto: {0}" \
                  "\nNome: {1}" \
                  "\nValor: {2}" \
                  "\nDescrição: {3}" \
                  "{4}"

        parameters = [self.id, self.nome, self.descricao, self.valor, self.fornecedor]

        return pattern.format(*parameters)
