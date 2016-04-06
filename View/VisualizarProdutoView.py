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


class Ui_VisualizarProduto(object):
    def setupUi(self, VisualizarProduto):
        VisualizarProduto.setObjectName(_fromUtf8("VisualizarProduto"))
        VisualizarProduto.resize(801, 529)
        VisualizarProduto.move(550, 250)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../Icons/mdpi.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        VisualizarProduto.setWindowIcon(icon)
        self.tblProduto = QtGui.QTableWidget(VisualizarProduto)
        self.tblProduto.setGeometry(QtCore.QRect(0, 0, 801, 529))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblProduto.sizePolicy().hasHeightForWidth())
        self.tblProduto.setSizePolicy(sizePolicy)
        self.tblProduto.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tblProduto.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tblProduto.setObjectName(_fromUtf8("tblProduto"))
        self.tblProduto.setColumnCount(5)
        self.tblProduto.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tblProduto.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblProduto.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tblProduto.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tblProduto.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tblProduto.setHorizontalHeaderItem(4, item)
        self.tblProduto.horizontalHeader().setVisible(True)
        self.tblProduto.horizontalHeader().setDefaultSectionSize(160)
        self.tblProduto.verticalHeader().setVisible(False)

        self.retranslateUi(VisualizarProduto)
        QtCore.QMetaObject.connectSlotsByName(VisualizarProduto)

    def retranslateUi(self, VisualizarProduto):
        VisualizarProduto.setWindowTitle(_translate("VisualizarProduto", "Visualizar Produto", None))
        item = self.tblProduto.horizontalHeaderItem(0)
        item.setText(_translate("VisualizarProduto", "Id", None))
        item = self.tblProduto.horizontalHeaderItem(1)
        item.setText(_translate("VisualizarProduto", "Nome", None))
        item = self.tblProduto.horizontalHeaderItem(2)
        item.setText(_translate("VisualizarProduto", "Descrição", None))
        item = self.tblProduto.horizontalHeaderItem(3)
        item.setText(_translate("VisualizarProduto", "Valor", None))
        item = self.tblProduto.horizontalHeaderItem(4)
        item.setText(_translate("VisualizarProduto", "Fornecedor", None))

