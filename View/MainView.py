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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.move(500, 200)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../Icons/mdpi.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, 9, 801, 531))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tblPedido = QtGui.QTableWidget(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblPedido.sizePolicy().hasHeightForWidth())
        self.tblPedido.setSizePolicy(sizePolicy)
        self.tblPedido.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tblPedido.setObjectName(_fromUtf8("tblPedido"))
        self.tblPedido.setColumnCount(6)
        self.tblPedido.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tblPedido.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblPedido.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tblPedido.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tblPedido.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tblPedido.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tblPedido.setHorizontalHeaderItem(5, item)
        self.tblPedido.horizontalHeader().setVisible(True)
        self.tblPedido.horizontalHeader().setDefaultSectionSize(133)
        self.tblPedido.verticalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.tblPedido)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuCadastros = QtGui.QMenu(self.menubar)
        self.menuCadastros.setObjectName(_fromUtf8("menuCadastros"))
        self.menuProduto = QtGui.QMenu(self.menuCadastros)
        self.menuProduto.setObjectName(_fromUtf8("menuProduto"))
        self.menuTransportadora = QtGui.QMenu(self.menuCadastros)
        self.menuTransportadora.setObjectName(_fromUtf8("menuTransportadora"))
        self.menuFornecedor = QtGui.QMenu(self.menuCadastros)
        self.menuFornecedor.setObjectName(_fromUtf8("menuFornecedor"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionProduto = QtGui.QAction(MainWindow)
        self.actionProduto.setObjectName(_fromUtf8("actionProduto"))
        self.actionFornecedor = QtGui.QAction(MainWindow)
        self.actionFornecedor.setObjectName(_fromUtf8("actionFornecedor"))
        self.actionNovoPedido = QtGui.QAction(MainWindow)
        self.actionNovoPedido.setObjectName(_fromUtf8("actionNovoPedido"))
        self.actionNovoProduto = QtGui.QAction(MainWindow)
        self.actionNovoProduto.setObjectName(_fromUtf8("actionNovoProduto"))
        self.actionVisualizarProduto = QtGui.QAction(MainWindow)
        self.actionVisualizarProduto.setObjectName(_fromUtf8("actionVisualizarProduto"))
        self.actionNovoTransportadora = QtGui.QAction(MainWindow)
        self.actionNovoTransportadora.setObjectName(_fromUtf8("actionNovoTransportadora"))
        self.actionVisualizarTransportadora = QtGui.QAction(MainWindow)
        self.actionVisualizarTransportadora.setObjectName(_fromUtf8("actionVisualizarTransportadora"))
        self.actionNovoFornecedor = QtGui.QAction(MainWindow)
        self.actionNovoFornecedor.setObjectName(_fromUtf8("actionNovoFornecedor"))
        self.actionVisualizarFornecedor = QtGui.QAction(MainWindow)
        self.actionVisualizarFornecedor.setObjectName(_fromUtf8("actionVisualizarFornecedor"))
        self.actionRemoverPedido = QtGui.QAction(MainWindow)
        self.actionRemoverPedido.setObjectName(_fromUtf8("actionRemoverPedido"))
        self.menuProduto.addAction(self.actionNovoProduto)
        self.menuProduto.addAction(self.actionVisualizarProduto)
        self.menuTransportadora.addAction(self.actionNovoTransportadora)
        self.menuTransportadora.addAction(self.actionVisualizarTransportadora)
        self.menuFornecedor.addAction(self.actionNovoFornecedor)
        self.menuFornecedor.addAction(self.actionVisualizarFornecedor)
        self.menuCadastros.addAction(self.menuProduto.menuAction())
        self.menuCadastros.addAction(self.menuFornecedor.menuAction())
        self.menuCadastros.addAction(self.menuTransportadora.menuAction())
        self.menubar.addAction(self.menuCadastros.menuAction())
        self.toolBar.addAction(self.actionNovoPedido)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRemoverPedido)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Giga", None))
        item = self.tblPedido.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id", None))
        item = self.tblPedido.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Data/Hora", None))
        item = self.tblPedido.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nota Fiscal", None))
        item = self.tblPedido.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Valor do Frete", None))
        item = self.tblPedido.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Desconto", None))
        item = self.tblPedido.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Valor Total", None))
        self.menuCadastros.setTitle(_translate("MainWindow", "Cadastros", None))
        self.menuProduto.setTitle(_translate("MainWindow", "Produto", None))
        self.menuTransportadora.setTitle(_translate("MainWindow", "Transportadora", None))
        self.menuFornecedor.setTitle(_translate("MainWindow", "Fornecedor", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionProduto.setText(_translate("MainWindow", "Produto", None))
        self.actionFornecedor.setText(_translate("MainWindow", "View", None))
        self.actionNovoPedido.setText(_translate("MainWindow", "Novo Pedido", None))
        self.actionNovoPedido.setToolTip(_translate("MainWindow", "Cria um novo pedido", None))
        self.actionNovoPedido.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.actionNovoProduto.setText(_translate("MainWindow", "Novo", None))
        self.actionVisualizarProduto.setText(_translate("MainWindow", "Visualizar", None))
        self.actionNovoTransportadora.setText(_translate("MainWindow", "Novo", None))
        self.actionVisualizarTransportadora.setText(_translate("MainWindow", "Visualizar", None))
        self.actionNovoFornecedor.setText(_translate("MainWindow", "Novo", None))
        self.actionVisualizarFornecedor.setText(_translate("MainWindow", "Visualizar", None))
        self.actionRemoverPedido.setText(_translate("MainWindow", "Remover Pedido", None))
        self.actionRemoverPedido.setShortcut(_translate("MainWindow", "Del", None))

