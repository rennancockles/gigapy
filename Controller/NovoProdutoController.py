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
        if self.tbNome.toPlainText() == '':
            return

        nome = self.tbNome.toPlainText()
        desc = self.tbDescricao.toPlainText()
        fornecedor = FornecedorDAO.find_by_name(self.cbFornecedor.currentText())[0]

        produto = Produto(nome=nome, descricao=desc, fornecedor=fornecedor)
        ProdutoDAO.insert(produto)

        self.close_view()

    def fill_fornecedor(self):
        items = FornecedorDAO.list()

        for item in items:
            self.cbFornecedor.addItem(item.nome)
