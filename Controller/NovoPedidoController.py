# -*- coding: utf-8 -*-

from View import NovoPedidoView
from DAO import ProdutoDAO, TransportadoraDAO
from Model.PedidoModel import Pedido as PedidoModel
from Model.ItemModel import Item
from PyQt4 import QtGui


class NovoPedido(QtGui.QMainWindow, NovoPedidoView.Ui_NovoPedido):
    def __init__(self, parent=None):
        super(NovoPedido, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.produtos = []

        self.row_count = 0

        self.desconto = 0.00
        self.frete = 0.00
        self.total = 0.00
        self.itens = []

        self.fill_item_combo()
        self.fill_transportadora_combo()
        self.lbTotal.setText(str(self.total))
        self.change_value()

        self.cbItem.currentIndexChanged.connect(self.change_value)

        self.btnCancelar.clicked.connect(self.close_view)
        self.btnSalvar.clicked.connect(self.salvar_pedido)
        self.btnAdd.clicked.connect(self.add_item)
        self.btnRemove.clicked.connect(self.remove_item)
        self.btnCalcular.clicked.connect(self.calcular_total)

    def close_view(self):
        self.close()

    def salvar_pedido(self):
        self.atualizar_total()

        if self.tblItem.rowCount() == 0:
            QtGui.QMessageBox.warning(self, "Erro", "Nenhum item adicionado!")
            return

        nota_fiscal = self.tbNota.toPlainText()
        frete = self.frete
        desconto = self.desconto
        total = self.total
        transportadora = TransportadoraDAO.find_by_name(self.cbTransportadora.currentText())[0]

        if nota_fiscal == '' or frete == '' or desconto == '' or total == '' or transportadora == '':
            QtGui.QMessageBox.warning(self, "Erro", "Preencha os campos corretamente!")
            return

        pedido = PedidoModel(id=self.parent.pedidoId, nota_fiscal=nota_fiscal, valor_frete=int(frete), desconto=desconto, valor_total=total, transportadora=transportadora)
        self.parent.pedidoId += 1

        pedido.add_itens(self.itens)

        self.parent.pedidos.append(pedido)
        self.parent.add_item(pedido)
        self.close_view()

    def fill_item_combo(self):
        items = ProdutoDAO.list()
        self.produtos = items

        for item in items:
            self.cbItem.addItem(item.nome)

    def fill_transportadora_combo(self):
        items = TransportadoraDAO.list()

        for item in items:
            self.cbTransportadora.addItem(item.nome)

    def add_item(self):
        valor = self.lbValor.text()
        qtd = self.tbQtd.toPlainText()

        if qtd == '' or valor == '':
            QtGui.QMessageBox.warning(self, "Erro", "Preencha os campos corretamente!")
            return

        parsed_qtd = self.parse_qtd(qtd)
        parsed_valor = self.parse_valor(valor)

        if parsed_qtd is None or parsed_valor is None:
            return

        newProduto = ProdutoDAO.find_by_name(self.cbItem.currentText())[0]
        newItem = Item(id=self.parent.itemId, quantidade=parsed_qtd, valor=parsed_valor, produto=newProduto)
        self.itens.append(newItem)
        self.parent.itemId += 1

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

        item = self.tblItem.item(row, 0)
        item.setText(self.cbItem.currentText())
        item = self.tblItem.item(row, 1)
        item.setText(qtd)
        item = self.tblItem.item(row, 2)
        item.setText(str(parsed_valor * parsed_qtd))

        self.tbQtd.clear()

        self.total += (parsed_valor * parsed_qtd)
        self.lbTotal.setText(str(self.total))

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

    def atualizar_total(self):
        desconto = self.tbDesconto.toPlainText()
        frete = self.tbFrete.toPlainText()
        parsed_desconto = 0
        parsed_frete = 0

        if desconto != '':
            parsed_desconto = self.parse_valor(desconto)

        if frete != '':
            parsed_frete = self.parse_valor(frete)

        if parsed_desconto is None or parsed_frete is None:
            return

        self.desconto = parsed_desconto
        self.frete = parsed_frete

        self.total -= self.desconto
        self.total += self.frete

        self.lbTotal.setText(str(self.total))

    def remove_item(self):
        row = self.tblItem.currentRow()
        self.row_count -= 1
        self.itens.pop(row)

        valor = self.tblItem.item(row, 2).text()

        parsed_valor = self.parse_valor(valor)

        if parsed_valor is None:
            return

        self.total -= parsed_valor
        self.lbTotal.setText(str(self.total))
        self.tblItem.removeRow(row)

    def calcular_total(self):
        desconto = self.tbDesconto.toPlainText()
        frete = self.tbFrete.toPlainText()
        print frete
        parsed_desconto = 0
        parsed_frete = 0

        if desconto != '':
            parsed_desconto = self.parse_valor(desconto)

        if frete != '':
            parsed_frete = self.parse_valor(frete)
            print parsed_frete

        if parsed_desconto is None or parsed_frete is None:
            return

        total = self.total - parsed_desconto + parsed_frete

        self.lbTotal.setText(str(total))

    def change_value(self):
        produto = self.produtos[self.cbItem.currentIndex()]
        valor = produto.valor
        self.lbValor.setText(str(valor))
