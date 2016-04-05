# -*- coding: utf-8 -*-


class Fornecedor(object):

    def __init__(self, id=None, nome='', descricao='', cidade='', endereco='', bairro='', numero=0):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.cidade = cidade
        self.endereco = endereco
        self.bairro = bairro
        self.numero = numero
        self.telefones = []
        self.emails = []

    def from_db(self, columns, row):
        id = row[columns.index('id')]
        nome = row[columns.index('nome')]
        descricao = row[columns.index('descricao')]
        cidade = row[columns.index('cidade')]
        endereco = row[columns.index('endereco')]
        bairro = row[columns.index('bairro')]
        numero = row[columns.index('numero')]

        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.cidade = cidade
        self.endereco = endereco
        self.bairro = bairro
        self.numero = numero

    def add_telefones(self, telefones):
        if type(telefones) == list:
            for telefone in telefones:
                self.telefones.append(telefone)
        else:
            self.telefones.append(telefones)

    def add_emails(self, emails):
        if type(emails) == list:
            for email in emails:
                self.emails.append(email)
        else:
            self.emails.append(emails)

    def __str__(self):
        pattern = "\nId Fornecedor: {0}" \
                  "\nNome: {1}" \
                  "\nDescrição: {2}" \
                  "\nCidade: {3}" \
                  "\nEndereço: {4}" \
                  "\nBairro: {5}" \
                  "\nNumero: {6}" \
                  "\n{7}" \
                  "\n{8}"

        parameters = [self.id, self.nome, self.descricao, self.cidade, self.endereco, self.bairro, self.numero, self.telefones, self.emails]

        return pattern.format(*parameters)


