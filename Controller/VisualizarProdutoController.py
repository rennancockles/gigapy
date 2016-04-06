# -*- coding: utf-8 -*-

from View import VisualizarProdutoView
from DAO import ProdutoDAO
from PyQt4 import QtGui


class VisualizarProduto(QtGui.QMainWindow, VisualizarProdutoView.Ui_VisualizarProduto):
    def __init__(self, parent=None):
        super(VisualizarProduto, self).__init__(parent)
        self.setupUi(self)

        self.row_count = 0

        self.fill_produtos()

    def add_item(self, produto):
        row = self.row_count
        self.row_count += 1
        self.tblProduto.setRowCount(self.row_count)

        item = QtGui.QTableWidgetItem()
        self.tblProduto.setVerticalHeaderItem(row, item)

        item = QtGui.QTableWidgetItem()
        self.tblProduto.setItem(row, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tblProduto.setItem(row, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tblProduto.setItem(row, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tblProduto.setItem(row, 3, item)

        item = self.tblProduto.item(row, 0)
        item.setText(str(produto.id))
        item = self.tblProduto.item(row, 1)
        item.setText(produto.nome)
        item = self.tblProduto.item(row, 2)
        item.setText(produto.descricao)
        item = self.tblProduto.item(row, 3)
        item.setText(produto.fornecedor.nome)

    def fill_produtos(self):
        produtos = ProdutoDAO.list()

        for produto in produtos:
            self.add_item(produto)
