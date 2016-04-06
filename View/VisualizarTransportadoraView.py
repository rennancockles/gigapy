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


class Ui_VisualizarTransportadora(object):
    def setupUi(self, VisualizarTransportadora):
        VisualizarTransportadora.setObjectName(_fromUtf8("VisualizarTransportadora"))
        VisualizarTransportadora.resize(403, 300)
        VisualizarTransportadora.move(550, 250)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../Icons/mdpi.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        VisualizarTransportadora.setWindowIcon(icon)
        self.tblTransportadora = QtGui.QTableWidget(VisualizarTransportadora)
        self.tblTransportadora.setGeometry(QtCore.QRect(0, 0, 401, 300))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblTransportadora.sizePolicy().hasHeightForWidth())
        self.tblTransportadora.setSizePolicy(sizePolicy)
        self.tblTransportadora.setMaximumSize(QtCore.QSize(541, 300))
        self.tblTransportadora.setAutoFillBackground(False)
        self.tblTransportadora.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tblTransportadora.setFrameShadow(QtGui.QFrame.Sunken)
        self.tblTransportadora.setLineWidth(1)
        self.tblTransportadora.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tblTransportadora.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tblTransportadora.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tblTransportadora.setShowGrid(True)
        self.tblTransportadora.setGridStyle(QtCore.Qt.SolidLine)
        self.tblTransportadora.setWordWrap(True)
        self.tblTransportadora.setCornerButtonEnabled(True)
        self.tblTransportadora.setObjectName(_fromUtf8("tblTransportadora"))
        self.tblTransportadora.setColumnCount(2)
        self.tblTransportadora.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tblTransportadora.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblTransportadora.setHorizontalHeaderItem(1, item)
        self.tblTransportadora.horizontalHeader().setVisible(True)
        self.tblTransportadora.horizontalHeader().setCascadingSectionResizes(False)
        self.tblTransportadora.horizontalHeader().setDefaultSectionSize(200)
        self.tblTransportadora.horizontalHeader().setSortIndicatorShown(False)
        self.tblTransportadora.horizontalHeader().setStretchLastSection(False)
        self.tblTransportadora.verticalHeader().setVisible(False)
        self.tblTransportadora.verticalHeader().setHighlightSections(True)

        self.retranslateUi(VisualizarTransportadora)
        QtCore.QMetaObject.connectSlotsByName(VisualizarTransportadora)

    def retranslateUi(self, VisualizarTransportadora):
        VisualizarTransportadora.setWindowTitle(_translate("VisualizarTransportadora", "Visualizar Transportadora", None))
        self.tblTransportadora.setSortingEnabled(False)
        item = self.tblTransportadora.horizontalHeaderItem(0)
        item.setText(_translate("VisualizarTransportadora", "Id", None))
        item = self.tblTransportadora.horizontalHeaderItem(1)
        item.setText(_translate("VisualizarTransportadora", "Nome", None))

