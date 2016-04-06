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


class Ui_NovoProduto(object):
    def setupUi(self, NovoProduto):
        NovoProduto.setObjectName(_fromUtf8("NovoProduto"))
        NovoProduto.resize(400, 246)
        NovoProduto.move(550, 250)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../Icons/mdpi.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NovoProduto.setWindowIcon(icon)
        self.btnCancelar = QtGui.QPushButton(NovoProduto)
        self.btnCancelar.setGeometry(QtCore.QRect(150, 210, 101, 27))
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.tbNome = QtGui.QPlainTextEdit(NovoProduto)
        self.tbNome.setGeometry(QtCore.QRect(100, 10, 291, 31))
        self.tbNome.setObjectName(_fromUtf8("tbNome"))
        self.label_7 = QtGui.QLabel(NovoProduto)
        self.label_7.setGeometry(QtCore.QRect(40, 20, 51, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.btnSalvar = QtGui.QPushButton(NovoProduto)
        self.btnSalvar.setGeometry(QtCore.QRect(280, 210, 101, 27))
        self.btnSalvar.setObjectName(_fromUtf8("btnSalvar"))
        self.tbDescricao = QtGui.QPlainTextEdit(NovoProduto)
        self.tbDescricao.setGeometry(QtCore.QRect(100, 60, 291, 31))
        self.tbDescricao.setObjectName(_fromUtf8("tbDescricao"))
        self.label_8 = QtGui.QLabel(NovoProduto)
        self.label_8.setGeometry(QtCore.QRect(20, 70, 71, 20))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.cbFornecedor = QtGui.QComboBox(NovoProduto)
        self.cbFornecedor.setGeometry(QtCore.QRect(100, 160, 291, 31))
        self.cbFornecedor.setObjectName(_fromUtf8("cbFornecedor"))
        self.label_2 = QtGui.QLabel(NovoProduto)
        self.label_2.setGeometry(QtCore.QRect(10, 170, 91, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tbValor = QtGui.QPlainTextEdit(NovoProduto)
        self.tbValor.setGeometry(QtCore.QRect(260, 110, 131, 31))
        self.tbValor.setObjectName(_fromUtf8("tbValor"))
        self.label_9 = QtGui.QLabel(NovoProduto)
        self.label_9.setGeometry(QtCore.QRect(210, 120, 41, 20))
        self.label_9.setObjectName(_fromUtf8("label_9"))

        self.retranslateUi(NovoProduto)
        QtCore.QMetaObject.connectSlotsByName(NovoProduto)

    def retranslateUi(self, NovoProduto):
        NovoProduto.setWindowTitle(_translate("NovoProduto", "Novo Produto", None))
        self.btnCancelar.setText(_translate("NovoProduto", "Cancelar", None))
        self.label_7.setText(_translate("NovoProduto", "Nome:", None))
        self.btnSalvar.setText(_translate("NovoProduto", "Salvar", None))
        self.label_8.setText(_translate("NovoProduto", "Descrição:", None))
        self.label_2.setText(_translate("NovoProduto", "Fornecedor:", None))
        self.label_9.setText(_translate("NovoProduto", "Valor:", None))

