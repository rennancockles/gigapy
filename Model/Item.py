# -*- coding: utf-8 -*-

from . import Produto


class Item(object):

    def __init__(self):
        self.id = None
        self.quantidade = ''
        self.valor = ''
        self.produto = None

