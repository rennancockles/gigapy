# -*- coding: utf-8 -*-

from DAO.Connection import conn
from DAO import TelefoneDAO, EmailDAO
from Model.Fornecedor import Fornecedor


def list():
    query = "SELECT * FROM fornecedor"
    conn.cursor.execute(query)

    if not conn.cursor.rowcount:
        print "Nenhum dado encontrado"
        return

    fornecedores = []
    columns = [i[0] for i in conn.cursor.description]

    for row in conn.cursor.fetchall():
        fornecedor = Fornecedor()
        fornecedor.from_db(columns, row)

        emails = EmailDAO.find_by_fornecedor(fornecedor)
        telefones = TelefoneDAO.find_by_fornecedor(fornecedor)

        fornecedor.add_emails(emails)
        fornecedor.add_telefones(telefones)

        fornecedores.append(fornecedor)
        print fornecedor

    return fornecedores


def find_by_name(name):
    base_query = "SELECT * FROM fornecedor WHERE nome = '{}'"
    query = base_query.format(name)
    conn.cursor.execute(query)

    if not conn.cursor.rowcount:
        print "Nenhum dado encontrado"
        return

    fornecedores = []
    columns = [i[0] for i in conn.cursor.description]

    for row in conn.cursor.fetchall():
        fornecedor = Fornecedor()
        fornecedor.from_db(columns, row)

        emails = EmailDAO.find_by_fornecedor(fornecedor)
        telefones = TelefoneDAO.find_by_fornecedor(fornecedor)

        fornecedor.add_emails(emails)
        fornecedor.add_telefones(telefones)

        fornecedores.append(fornecedor)
        print fornecedor

    return fornecedores


def find_by_id(id):
    base_query = "SELECT * FROM fornecedor WHERE id = '{}'"
    query = base_query.format(id)
    conn.cursor.execute(query)

    if not conn.cursor.rowcount:
        print "Nenhum dado encontrado"
        return

    columns = [i[0] for i in conn.cursor.description]
    row = conn.cursor.fetchone()

    fornecedor = Fornecedor()
    fornecedor.from_db(columns, row)

    emails = EmailDAO.find_by_fornecedor(fornecedor)
    telefones = TelefoneDAO.find_by_fornecedor(fornecedor)

    fornecedor.add_emails(emails)
    fornecedor.add_telefones(telefones)

    print fornecedor

    return fornecedor


def insert(fornecedor):
    base_query = "INSERT INTO fornecedor (nome, descricao, cidade, endereco, bairro, numero) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')"
    query = base_query.format(fornecedor.nome, fornecedor.descricao, fornecedor.cidade, fornecedor.endereco, fornecedor.bairro, fornecedor.numero)

    conn.cursor.execute(query)

    if not conn.cursor.rowcount:
        print "Nenhum dado inserido"
        return

    idFornecedor = conn.cursor.lastrowid

    for telefone in fornecedor.telefones:
        TelefoneDAO.insert(idFornecedor, telefone)

    for email in fornecedor.emails:
        EmailDAO.insert(idFornecedor, email)

    conn.db.commit()


def update(fornecedor):
    base_query = "UPDATE fornecedor SET nome = '{}', descricao = '{}', cidade = '{}', endereco = '{}', bairro = '{}', numero = '{}' WHERE id = '{}'"
    query = base_query.format(fornecedor.nome, fornecedor.descricao, fornecedor.cidade, fornecedor.endereco, fornecedor.bairro, fornecedor.numero, fornecedor.id)
    conn.cursor.execute(query)

    if not conn.cursor.rowcount:
        print "Nenhum dado alterado"
        return

    conn.db.commit()


def delete(fornecedor):
    base_query = "DELETE FROM fornecedor WHERE id = '{}'"
    query = base_query.format(fornecedor.id)
    conn.cursor.execute(query)

    if not conn.cursor.rowcount:
        print "Nenhum dado apagado"
        return

    conn.db.commit()


# list()
# find_by_name('forn_2')
# f = find_by_id(14)
# f.bairro = 'serrano'
# update(f)
# delete(find_by_id(15))

# f = Fornecedor(nome='forn_3', descricao='terceiro fornecedor', cidade='teresopis', endereco='rua de teresa', bairro='alto', numero=171)
# t = Telefone(ddd='24', numero='25256363', referencia='tel doido')
# e = Email(email='eu@me.com', referencia='meu mesmo')
# f.add_telefones(t)
# f.add_emails(e)
# insert(f)

# list()

# conn.close_connection()
