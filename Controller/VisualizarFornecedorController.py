# -*- coding: utf-8 -*-

from View import VisualizarFornecedorView
from DAO import TelefoneDAO, EmailDAO, FornecedorDAO
from Controller import NovoPedidoController, VisualizarPedidoController, NovaTransportadoraController, NovoProdutoController, NovoFornecedorController
from PyQt4 import QtGui, QtCore


class VisualizarFornecedor(QtGui.QMainWindow, VisualizarFornecedorView.Ui_VisualizarFornecedor):
    def __init__(self, parent=None):
        super(VisualizarFornecedor, self).__init__(parent)
        self.setupUi(self)

        self.fornecedores = []

        self.row_count = 0
        self.telefone_row_count = 0
        self.email_row_count = 0
        self.fill_fornecedores()

        self.tblFornecedor.itemClicked.connect(self.fill_fornecedor_data)

    def add_item(self, fornecedor):
        row = self.row_count
        self.row_count += 1
        self.tblFornecedor.setRowCount(self.row_count)

        item = QtGui.QTableWidgetItem()
        self.tblFornecedor.setVerticalHeaderItem(row, item)

        item = QtGui.QTableWidgetItem()
        self.tblFornecedor.setItem(row, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tblFornecedor.setItem(row, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tblFornecedor.setItem(row, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tblFornecedor.setItem(row, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tblFornecedor.setItem(row, 4, item)
        item = QtGui.QTableWidgetItem()
        self.tblFornecedor.setItem(row, 5, item)
        item = QtGui.QTableWidgetItem()
        self.tblFornecedor.setItem(row, 6, item)

        item = self.tblFornecedor.item(row, 0)
        item.setText(str(fornecedor.id))
        item = self.tblFornecedor.item(row, 1)
        item.setText(fornecedor.nome)
        item = self.tblFornecedor.item(row, 2)
        item.setText(fornecedor.descricao)
        item = self.tblFornecedor.item(row, 3)
        item.setText(fornecedor.cidade)
        item = self.tblFornecedor.item(row, 4)
        item.setText(fornecedor.endereco)
        item = self.tblFornecedor.item(row, 5)
        item.setText(fornecedor.bairro)
        item = self.tblFornecedor.item(row, 6)
        item.setText(str(fornecedor.numero))

    def add_telefone(self, telefone):
        row = self.telefone_row_count
        self.telefone_row_count += 1
        self.tblTelefone.setRowCount(self.telefone_row_count)

        item = QtGui.QTableWidgetItem()
        self.tblTelefone.setVerticalHeaderItem(row, item)

        item = QtGui.QTableWidgetItem()
        self.tblTelefone.setItem(row, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tblTelefone.setItem(row, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tblTelefone.setItem(row, 2, item)

        item = self.tblTelefone.item(row, 0)
        item.setText(telefone.ddd)
        item = self.tblTelefone.item(row, 1)
        item.setText(telefone.numero)
        item = self.tblTelefone.item(row, 2)
        item.setText(telefone.referencia)

    def add_email(self, email):
        row = self.email_row_count
        self.email_row_count += 1
        self.tblEmail.setRowCount(self.email_row_count)

        item = QtGui.QTableWidgetItem()
        self.tblEmail.setVerticalHeaderItem(row, item)

        item = QtGui.QTableWidgetItem()
        self.tblEmail.setItem(row, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tblEmail.setItem(row, 1, item)

        item = self.tblEmail.item(row, 0)
        item.setText(email.email)
        item = self.tblEmail.item(row, 1)
        item.setText(email.referencia)

    def visualizar_pedido(self):
        pedidoId = self.tblFornecedor.item(self.tblFornecedor.currentRow(), 0).text()
        visualizarPedido = VisualizarPedidoController.VisualizarPedido(self, self.pedidos[int(pedidoId)])
        visualizarPedido.show()

    def fill_fornecedores(self):
        fornecedores = FornecedorDAO.list()
        self.fornecedores = fornecedores

        for fornecedor in fornecedores:
            self.add_item(fornecedor)

    def fill_fornecedor_data(self):
        self.telefone_row_count = 0
        self.email_row_count = 0

        fornecedor = self.fornecedores[self.tblFornecedor.currentRow()]
        telefones = TelefoneDAO.find_by_fornecedor(fornecedor)
        emails = EmailDAO.find_by_fornecedor(fornecedor)

        for telefone in telefones:
            self.add_telefone(telefone)

        for email in emails:
            self.add_email(email)
