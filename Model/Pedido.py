# -*- coding: utf-8 -*-

from . import Item, Transportadora


class Pedido(object):

    def __init__(self):
        self.id = None
        self.datahora = None
        self.nota_fiscal = ''
        self.valor_frete = None
        self.desconto = None
        self.valor_total = None
        self.itens = []
        self.transportadora = None

