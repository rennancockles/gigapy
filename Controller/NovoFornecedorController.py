# -*- coding: utf-8 -*-

from View import NovoFornecedorView
from DAO import FornecedorDAO
from Model.TelefoneModel import Telefone
from Model.EmailModel import Email
from Model.FornecedorModel import Fornecedor
from PyQt4 import QtGui


class NovoFornecedor(QtGui.QMainWindow, NovoFornecedorView.Ui_NovoFornecedor):
    def __init__(self, parent=None):
        super(NovoFornecedor, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.telefoneId = 0
        self.telefone_row_count = 0
        self.telefones = []

        self.emailId = 0
        self.email_row_count = 0
        self.emails = []

        self.btnCancelar.clicked.connect(self.close_view)
        self.btnSalvar.clicked.connect(self.salvar)
        self.btnTelefoneAdd.clicked.connect(self.add_telefone)
        self.btnTelefoneRemove.clicked.connect(self.remove_telefone)
        self.btnEmailAdd.clicked.connect(self.add_email)
        self.btnEmailRemove.clicked.connect(self.remove_email)

    def close_view(self):
        self.close()

    def salvar(self):
        nome = self.tbNome.toPlainText()
        desc = self.tbDescricao.toPlainText()
        cidade = self.tbCidade.toPlainText()
        endereco = self.tbEndereco.toPlainText()
        bairro = self.tbBairro.toPlainText()
        numero = self.tbNumero.toPlainText()

        if nome == '' or desc == '' or cidade == '' or endereco == '' or bairro == '' or numero == '':
            QtGui.QMessageBox.warning(self, "Erro", "Preencha os campos corretamente!")
            return

        parsed_num = self.parse_numero(numero)

        if parsed_num is None:
            return

        fornecedor = Fornecedor(nome=nome, descricao=desc, cidade=cidade, endereco=endereco, bairro=bairro, numero=numero)
        fornecedor.add_emails(self.emails)
        fornecedor.add_telefones(self.telefones)

        FornecedorDAO.insert(fornecedor)
        print fornecedor

        self.close_view()

    def add_telefone(self):
        ddd = self.verify_ddd(self.tbTelefoneDDD.toPlainText())
        numero = self.verify_telefone(self.tbTelefoneNumero.toPlainText())
        referencia = self.tbTelefoneReferencia.toPlainText()

        if numero is None or ddd is None:
            return

        if ddd == '' or numero == '' or referencia == '':
            QtGui.QMessageBox.warning(self, "Erro", "Preencha os campos corretamente!")
            return

        telefone = Telefone(ddd=ddd, numero=numero, referencia=referencia)

        self.telefones.append(telefone)
        self.telefoneId += 1

        row = self.telefone_row_count
        self.telefone_row_count += 1
        self.tblTelefone.setRowCount(self.telefone_row_count)

        item = QtGui.QTableWidgetItem()
        self.tblTelefone.setVerticalHeaderItem(row, item)

        item = QtGui.QTableWidgetItem()
        self.tblTelefone.setItem(row, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tblTelefone.setItem(row, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tblTelefone.setItem(row, 2, item)

        item = self.tblTelefone.item(row, 0)
        item.setText(telefone.ddd)
        item = self.tblTelefone.item(row, 1)
        item.setText(telefone.numero)
        item = self.tblTelefone.item(row, 2)
        item.setText(telefone.referencia)

        self.tbTelefoneDDD.clear()
        self.tbTelefoneNumero.clear()
        self.tbTelefoneReferencia.clear()

    def remove_telefone(self):
        row = self.tblTelefone.currentRow()
        self.telefone_row_count -= 1
        self.telefones.pop(row)

        self.tblTelefone.removeRow(row)

    def add_email(self):
        email = self.verify_email(self.tbEmail.toPlainText())
        referencia = self.tbEmailReferencia.toPlainText()

        if email is None:
            return

        if email == '' or referencia == '':
            QtGui.QMessageBox.warning(self, "Erro", "Preencha os campos corretamente!")
            return

        email = Email(email=email, referencia=referencia)

        self.emails.append(email)
        self.emailId += 1

        row = self.email_row_count
        self.email_row_count += 1
        self.tblEmail.setRowCount(self.email_row_count)

        item = QtGui.QTableWidgetItem()
        self.tblEmail.setVerticalHeaderItem(row, item)

        item = QtGui.QTableWidgetItem()
        self.tblEmail.setItem(row, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tblEmail.setItem(row, 1, item)

        item = self.tblEmail.item(row, 0)
        item.setText(email.email)
        item = self.tblEmail.item(row, 1)
        item.setText(email.referencia)

        self.tbEmail.clear()
        self.tbEmailReferencia.clear()

    def remove_email(self):
        row = self.tblEmail.currentRow()
        self.email_row_count -= 1
        self.emails.pop(row)

        self.tblEmail.removeRow(row)

    def parse_numero(self, string):
        try:
            i = int(string)
            return i
        except:
            QtGui.QMessageBox.warning(self, "Erro", "Numero deve ser do tipo inteiro!".format(string))
            return

    def verify_email(self, email):
        import re

        addressToVerify = email
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

        if match is None:
            QtGui.QMessageBox.warning(self, "Erro", "Email invalido!")
            return None
        else:
            return email

    def verify_telefone(self, telefone):
        import re

        addressToVerify = telefone
        match = re.match('(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', addressToVerify)

        if match is None:
            QtGui.QMessageBox.warning(self, "Erro", "Telefone invalido!")
            return None
        else:
            return telefone

    def verify_ddd(self, ddd):
        import re

        addressToVerify = ddd
        match = re.match('^\d{2}$', addressToVerify)

        if match is None:
            QtGui.QMessageBox.warning(self, "Erro", "DDD invalido!")
            return None
        else:
            return ddd
