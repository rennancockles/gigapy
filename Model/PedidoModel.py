# -*- coding: utf-8 -*-

from datetime import datetime


class Pedido(object):

    def __init__(self, id=None, nota_fiscal='', valor_frete=0, desconto=0.0, valor_total=0.0, transportadora=None):
        self.id = id
        self.datahora = datetime.now()
        self.nota_fiscal = nota_fiscal
        self.valor_frete = valor_frete
        self.desconto = desconto
        self.valor_total = valor_total
        self.itens = []
        self.transportadora = transportadora

    def from_db(self, columns, row):
        id = row[columns.index('id')]
        datahora = row[columns.index('datahora')]
        nota_fiscal = row[columns.index('nota_fiscal')]
        valor_frete = row[columns.index('valor_frete')]
        desconto = row[columns.index('desconto')]
        valor_total = row[columns.index('valor_total')]

        self.id = id
        self.datahora = datahora
        self.nota_fiscal = nota_fiscal
        self.valor_frete = valor_frete
        self.desconto = desconto
        self.valor_total = valor_total

    def add_itens(self, itens):
        if type(itens) == list:
            for item in itens:
                self.itens.append(item)
        else:
            self.itens.append(itens)

    def add_transportadora(self, transportadora):
        self.transportadora = transportadora

    def __str__(self):
        pattern = "\nId Pedido: {0}" \
                  "\nData: {1}" \
                  "\nNota Fiscal: {2}" \
                  "\nValor do Frete: {3}" \
                  "\nDesconto: {4}" \
                  "\nValor Total: {5}" \
                  "\n{6}" \
                  "{7}"

        parameters = [self.id, self.datahora, self.nota_fiscal, self.valor_frete, self.desconto, self.valor_total, self.itens, self.transportadora]

        return pattern.format(*parameters)

