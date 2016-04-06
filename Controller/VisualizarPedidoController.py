# -*- coding: utf-8 -*-

from View import VisualizarPedidoView
from PyQt4 import QtGui


class VisualizarPedido(QtGui.QMainWindow, VisualizarPedidoView.Ui_VisualizarPedido):
    def __init__(self, parent=None, pedido=None):
        super(VisualizarPedido, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.pedido = pedido

        self.row_count = 0

        self.lbNota.setText(pedido.nota_fiscal)
        self.lbData.setText(str(pedido.datahora))
        self.lbTotal.setText(str(pedido.valor_total))
        self.lbDesconto.setText(str(pedido.desconto))
        self.lbFrete.setText(str(pedido.valor_frete))
        self.lbTransportadora.setText(str(pedido.transportadora.nome))

        self.fill_tblitem()

        self.btnSair.clicked.connect(self.close_view)

    def close_view(self):
        self.close()

    def fill_tblitem(self):
        for item in self.pedido.itens:
            self.add_item(item)

    def add_item(self, addedItem):
        row = self.row_count
        self.row_count += 1
        self.tblItem.setRowCount(self.row_count)

        item = QtGui.QTableWidgetItem()
        self.tblItem.setVerticalHeaderItem(row, item)

        item = QtGui.QTableWidgetItem()
        self.tblItem.setItem(row, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tblItem.setItem(row, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tblItem.setItem(row, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tblItem.setItem(row, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tblItem.setItem(row, 4, item)
        item = QtGui.QTableWidgetItem()
        self.tblItem.setItem(row, 5, item)

        item = self.tblItem.item(row, 0)
        item.setText(addedItem.produto.nome)
        item = self.tblItem.item(row, 1)
        item.setText(addedItem.produto.descricao)
        item = self.tblItem.item(row, 2)
        item.setText(str(addedItem.produto.valor))
        item = self.tblItem.item(row, 3)
        item.setText(addedItem.produto.fornecedor.nome)
        item = self.tblItem.item(row, 4)
        item.setText(str(addedItem.quantidade))
        item = self.tblItem.item(row, 5)
        item.setText(str(addedItem.valor))

    def parse_qtd(self, string):
        try:
            i = int(string)
            return i
        except:
            QtGui.QMessageBox.warning(self, "Erro", "Quantidade deve ser do tipo inteiro!".format(string))
            return

    def parse_valor(self, string):
        try:
            i = float(string.replace(',', '.'))
            return i
        except:
            QtGui.QMessageBox.warning(self, "Erro", "Valor deve ser do tipo float!".format(string))
            return
