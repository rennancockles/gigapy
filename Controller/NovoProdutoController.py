# -*- coding: utf-8 -*-

from View import NovoProdutoView
from DAO import ProdutoDAO, FornecedorDAO
from Model.ProdutoModel import Produto
from PyQt4 import QtGui


class NovoProduto(QtGui.QMainWindow, NovoProdutoView.Ui_NovoProduto):
    def __init__(self, parent=None):
        super(NovoProduto, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.fill_fornecedor()

        self.btnCancelar.clicked.connect(self.close_view)
        self.btnSalvar.clicked.connect(self.salvar)

    def close_view(self):
        self.close()

    def salvar(self):
        nome = self.tbNome.toPlainText()
        descricao = self.tbDescricao.toPlainText()
        valor = self.tbValor.toPlainText()
        fornecedor = FornecedorDAO.find_by_name(self.cbFornecedor.currentText())[0]

        if nome == '' or descricao == '' or valor == '':
            QtGui.QMessageBox.warning(self, "Erro", "Preencha os campos corretamente!")
            return

        parsed_valor = self.parse_valor(valor)

        if parsed_valor is None:
            return

        produto = Produto(nome=nome, descricao=descricao, valor=parsed_valor, fornecedor=fornecedor)
        ProdutoDAO.insert(produto)

        self.close_view()

    def fill_fornecedor(self):
        items = FornecedorDAO.list()

        for item in items:
            self.cbFornecedor.addItem(item.nome)

    def parse_valor(self, string):
        try:
            i = float(string.replace(',', '.'))
            return i
        except:
            QtGui.QMessageBox.warning(self, "Erro", "Valor deve ser do tipo float!".format(string))
            return
