# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_VisualizarPedido(object):
    def setupUi(self, VisualizarPedido):
        VisualizarPedido.setObjectName(_fromUtf8("VisualizarPedido"))
        VisualizarPedido.resize(959, 354)
        VisualizarPedido.move(550, 250)
        self.tblItem = QtGui.QTableWidget(VisualizarPedido)
        self.tblItem.setGeometry(QtCore.QRect(10, 50, 941, 192))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblItem.sizePolicy().hasHeightForWidth())
        self.tblItem.setSizePolicy(sizePolicy)
        self.tblItem.setMaximumSize(QtCore.QSize(1000, 192))
        self.tblItem.setAutoFillBackground(False)
        self.tblItem.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tblItem.setFrameShadow(QtGui.QFrame.Sunken)
        self.tblItem.setLineWidth(1)
        self.tblItem.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tblItem.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tblItem.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tblItem.setShowGrid(True)
        self.tblItem.setGridStyle(QtCore.Qt.SolidLine)
        self.tblItem.setWordWrap(True)
        self.tblItem.setCornerButtonEnabled(True)
        self.tblItem.setObjectName(_fromUtf8("tblItem"))
        self.tblItem.setColumnCount(6)
        self.tblItem.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tblItem.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblItem.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tblItem.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tblItem.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tblItem.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tblItem.setHorizontalHeaderItem(5, item)
        self.tblItem.horizontalHeader().setVisible(True)
        self.tblItem.horizontalHeader().setCascadingSectionResizes(False)
        self.tblItem.horizontalHeader().setDefaultSectionSize(156)
        self.tblItem.horizontalHeader().setSortIndicatorShown(False)
        self.tblItem.horizontalHeader().setStretchLastSection(False)
        self.tblItem.verticalHeader().setVisible(False)
        self.tblItem.verticalHeader().setHighlightSections(True)
        self.notaFiscalLabel = QtGui.QLabel(VisualizarPedido)
        self.notaFiscalLabel.setGeometry(QtCore.QRect(10, 20, 81, 17))
        self.notaFiscalLabel.setObjectName(_fromUtf8("notaFiscalLabel"))
        self.lbTotal = QtGui.QLabel(VisualizarPedido)
        self.lbTotal.setGeometry(QtCore.QRect(570, 310, 91, 17))
        self.lbTotal.setText(_fromUtf8(""))
        self.lbTotal.setObjectName(_fromUtf8("lbTotal"))
        self.label_5 = QtGui.QLabel(VisualizarPedido)
        self.label_5.setGeometry(QtCore.QRect(520, 310, 41, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(VisualizarPedido)
        self.label_6.setGeometry(QtCore.QRect(490, 280, 66, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.btnSair = QtGui.QPushButton(VisualizarPedido)
        self.btnSair.setGeometry(QtCore.QRect(840, 310, 101, 27))
        self.btnSair.setObjectName(_fromUtf8("btnSair"))
        self.label_4 = QtGui.QLabel(VisualizarPedido)
        self.label_4.setGeometry(QtCore.QRect(480, 250, 81, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_2 = QtGui.QLabel(VisualizarPedido)
        self.label_2.setGeometry(QtCore.QRect(20, 250, 111, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lbNota = QtGui.QLabel(VisualizarPedido)
        self.lbNota.setGeometry(QtCore.QRect(100, 20, 291, 17))
        self.lbNota.setText(_fromUtf8(""))
        self.lbNota.setObjectName(_fromUtf8("lbNota"))
        self.lbTransportadora = QtGui.QLabel(VisualizarPedido)
        self.lbTransportadora.setGeometry(QtCore.QRect(140, 250, 191, 17))
        self.lbTransportadora.setText(_fromUtf8(""))
        self.lbTransportadora.setObjectName(_fromUtf8("lbTransportadora"))
        self.label_3 = QtGui.QLabel(VisualizarPedido)
        self.label_3.setGeometry(QtCore.QRect(430, 20, 41, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lbData = QtGui.QLabel(VisualizarPedido)
        self.lbData.setGeometry(QtCore.QRect(480, 20, 191, 17))
        self.lbData.setText(_fromUtf8(""))
        self.lbData.setObjectName(_fromUtf8("lbData"))
        self.lbFrete = QtGui.QLabel(VisualizarPedido)
        self.lbFrete.setGeometry(QtCore.QRect(570, 250, 81, 17))
        self.lbFrete.setText(_fromUtf8(""))
        self.lbFrete.setObjectName(_fromUtf8("lbFrete"))
        self.lbDesconto = QtGui.QLabel(VisualizarPedido)
        self.lbDesconto.setGeometry(QtCore.QRect(570, 280, 66, 17))
        self.lbDesconto.setText(_fromUtf8(""))
        self.lbDesconto.setObjectName(_fromUtf8("lbDesconto"))

        self.retranslateUi(VisualizarPedido)
        QtCore.QMetaObject.connectSlotsByName(VisualizarPedido)

    def retranslateUi(self, VisualizarPedido):
        VisualizarPedido.setWindowTitle(_translate("VisualizarPedido", "Visualizar Pedido", None))
        self.tblItem.setSortingEnabled(False)
        item = self.tblItem.horizontalHeaderItem(0)
        item.setText(_translate("VisualizarPedido", "Produto", None))
        item = self.tblItem.horizontalHeaderItem(1)
        item.setText(_translate("VisualizarPedido", "Descrição", None))
        item = self.tblItem.horizontalHeaderItem(2)
        item.setText(_translate("VisualizarPedido", "Valor do Produto", None))
        item = self.tblItem.horizontalHeaderItem(3)
        item.setText(_translate("VisualizarPedido", "Fornecedor", None))
        item = self.tblItem.horizontalHeaderItem(4)
        item.setText(_translate("VisualizarPedido", "Quantidade", None))
        item = self.tblItem.horizontalHeaderItem(5)
        item.setText(_translate("VisualizarPedido", "Valor", None))
        self.notaFiscalLabel.setText(_translate("VisualizarPedido", "Nota Fiscal:", None))
        self.label_5.setText(_translate("VisualizarPedido", "Total:", None))
        self.label_6.setText(_translate("VisualizarPedido", "Desconto:", None))
        self.btnSair.setText(_translate("VisualizarPedido", "Sair", None))
        self.label_4.setText(_translate("VisualizarPedido", "Valor Frete:", None))
        self.label_2.setText(_translate("VisualizarPedido", "Transportadora:", None))
        self.label_3.setText(_translate("VisualizarPedido", "Data:", None))

