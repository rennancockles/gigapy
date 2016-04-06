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


class Ui_NovaTransportadora(object):
    def setupUi(self, NovaTransportadora):
        NovaTransportadora.setObjectName(_fromUtf8("NovaTransportadora"))
        NovaTransportadora.resize(400, 173)
        NovaTransportadora.move(550, 250)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../Icons/mdpi.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NovaTransportadora.setWindowIcon(icon)
        self.btnCancelar = QtGui.QPushButton(NovaTransportadora)
        self.btnCancelar.setGeometry(QtCore.QRect(150, 130, 101, 27))
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.btnSalvar = QtGui.QPushButton(NovaTransportadora)
        self.btnSalvar.setGeometry(QtCore.QRect(280, 130, 101, 27))
        self.btnSalvar.setObjectName(_fromUtf8("btnSalvar"))
        self.tbNome = QtGui.QPlainTextEdit(NovaTransportadora)
        self.tbNome.setGeometry(QtCore.QRect(80, 40, 291, 31))
        self.tbNome.setObjectName(_fromUtf8("tbNome"))
        self.label_7 = QtGui.QLabel(NovaTransportadora)
        self.label_7.setGeometry(QtCore.QRect(20, 50, 51, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))

        self.retranslateUi(NovaTransportadora)
        QtCore.QMetaObject.connectSlotsByName(NovaTransportadora)

    def retranslateUi(self, NovaTransportadora):
        NovaTransportadora.setWindowTitle(_translate("NovaTransportadora", "Nova Transportadora", None))
        self.btnCancelar.setText(_translate("NovaTransportadora", "Cancelar", None))
        self.btnSalvar.setText(_translate("NovaTransportadora", "Salvar", None))
        self.label_7.setText(_translate("NovaTransportadora", "Nome:", None))

