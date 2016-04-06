# -*- coding: utf-8 -*-

from View import NovaTransportadoraView
from DAO import TransportadoraDAO
from Model.TransportadoraModel import Transportadora
from PyQt4 import QtGui


class NovaTransportadora(QtGui.QMainWindow, NovaTransportadoraView.Ui_NovaTransportadora):
    def __init__(self, parent=None):
        super(NovaTransportadora, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.btnCancelar.clicked.connect(self.close_view)
        self.btnSalvar.clicked.connect(self.salvar)
        self.btnSalvar.clicked.connect(self.salvar)

    def close_view(self):
        self.close()

    def salvar(self):
        if self.tbNome.toPlainText() == '':
            return

        nome = self.tbNome.toPlainText()
        transportadora = Transportadora(nome=nome)
        TransportadoraDAO.insert(transportadora)
        self.close_view()
