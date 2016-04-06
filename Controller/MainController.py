# -*- coding: utf-8 -*-

from View import MainView
from Controller import NovoPedidoController, VisualizarPedidoController, NovaTransportadoraController, NovoProdutoController, NovoFornecedorController
from PyQt4 import QtGui, QtCore


class Main(QtGui.QMainWindow, MainView.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.row_count = 0
        self.itemId = 0
        self.pedidoId = 0
        self.pedidos = []

        self.actionNovoPedido.triggered.connect(self.novoPedido)
        self.actionNovoTransportadora.triggered.connect(self.novaTransportadora)
        self.actionNovoFornecedor.triggered.connect(self.novoFornecedor)
        self.actionNovoProduto.triggered.connect(self.novoProduto)

        self.tblPedido.itemDoubleClicked.connect(self.visualizar_pedido)
        self.update()

    def novoPedido(self):
        novoPedido = NovoPedidoController.NovoPedido(self)
        novoPedido.show()

    def novoProduto(self):
        novoProduto = NovoProdutoController.NovoProduto(self)
        novoProduto.show()

    def novaTransportadora(self):
        novaTransportadora = NovaTransportadoraController.NovaTransportadora(self)
        novaTransportadora.show()

    def novoFornecedor(self):
        novoFornecedor = NovoFornecedorController.NovoFornecedor(self)
        novoFornecedor.show()

    def add_item(self, pedido):
        row = self.row_count
        self.row_count += 1
        self.tblPedido.setRowCount(self.row_count)

        item = QtGui.QTableWidgetItem()
        self.tblPedido.setVerticalHeaderItem(row, item)

        item = QtGui.QTableWidgetItem()
        self.tblPedido.setItem(row, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tblPedido.setItem(row, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tblPedido.setItem(row, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tblPedido.setItem(row, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tblPedido.setItem(row, 4, item)
        item = QtGui.QTableWidgetItem()
        self.tblPedido.setItem(row, 5, item)

        item = self.tblPedido.item(row, 0)
        item.setText(str(pedido.id))
        item = self.tblPedido.item(row, 1)
        item.setText(str(pedido.datahora))
        item = self.tblPedido.item(row, 2)
        item.setText(pedido.nota_fiscal)
        item = self.tblPedido.item(row, 3)
        item.setText(str(pedido.valor_frete))
        item = self.tblPedido.item(row, 4)
        item.setText(str(pedido.desconto))
        item = self.tblPedido.item(row, 5)
        item.setText(str(pedido.valor_total))

    def visualizar_pedido(self):
        pedidoId = self.tblPedido.item(self.tblPedido.currentRow(), 0).text()
        visualizarPedido = VisualizarPedidoController.VisualizarPedido(self, self.pedidos[int(pedidoId)])
        visualizarPedido.show()



