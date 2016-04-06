# -*- coding: utf-8 -*-

from View import VisualizarTransportadoraView
from DAO import TransportadoraDAO
from PyQt4 import QtGui


class VisualizarTransportadora(QtGui.QMainWindow, VisualizarTransportadoraView.Ui_VisualizarTransportadora):
    def __init__(self, parent=None):
        super(VisualizarTransportadora, self).__init__(parent)
        self.setupUi(self)

        self.row_count = 0

        self.fill_transportadoras()

    def add_item(self, transportadora):
        row = self.row_count
        self.row_count += 1
        self.tblTransportadora.setRowCount(self.row_count)

        item = QtGui.QTableWidgetItem()
        self.tblTransportadora.setVerticalHeaderItem(row, item)

        item = QtGui.QTableWidgetItem()
        self.tblTransportadora.setItem(row, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tblTransportadora.setItem(row, 1, item)

        item = self.tblTransportadora.item(row, 0)
        item.setText(str(transportadora.id))
        item = self.tblTransportadora.item(row, 1)
        item.setText(transportadora.nome)

    def fill_transportadoras(self):
        transportadoras = TransportadoraDAO.list()

        for transportadora in transportadoras:
            self.add_item(transportadora)

