# -*- coding: utf-8 -*-

from DAO.Connection import conn
from Model.TelefoneModel import Telefone


def list():
    query = "SELECT * FROM telefone"
    conn.cursor.execute(query)

    if not conn.cursor.rowcount:
        print "Nenhum dado encontrado"
        return

    telefones = []
    columns = [i[0] for i in conn.cursor.description]

    for row in conn.cursor.fetchall():
        telefone = Telefone()
        telefone.from_db(columns, row)
        telefones.append(telefone)
        print telefone

    return telefones


def find_by_numero(numero):
    base_query = "SELECT * FROM telefone WHERE numero = '{}'"
    query = base_query.format(numero)
    conn.cursor.execute(query)

    if not conn.cursor.rowcount:
        print "Nenhum dado encontrado"
        return

    telefones = []
    columns = [i[0] for i in conn.cursor.description]

    for row in conn.cursor.fetchall():
        telefone = Telefone()
        telefone.from_db(columns, row)
        telefones.append(telefone)
        print telefone

    return telefones


def find_by_id(id):
    base_query = "SELECT * FROM telefone WHERE id = '{}'"
    query = base_query.format(id)
    conn.cursor.execute(query)

    if not conn.cursor.rowcount:
        print "Nenhum dado encontrado"
        return

    columns = [i[0] for i in conn.cursor.description]
    row = conn.cursor.fetchone()

    telefone = Telefone()
    telefone.from_db(columns, row)
    print telefone

    return telefone


def find_by_fornecedor(fornecedor):
    base_query = "SELECT * FROM telefone WHERE idFornecedor = '{}'"
    query = base_query.format(fornecedor.id)
    conn.cursor.execute(query)

    if not conn.cursor.rowcount:
        print "Nenhum dado encontrado"
        return

    telefones = []
    columns = [i[0] for i in conn.cursor.description]

    for row in conn.cursor.fetchall():
        telefone = Telefone()
        telefone.from_db(columns, row)
        telefones.append(telefone)

    return telefones


def insert(idFornecedor, telefone):
    base_query = "INSERT INTO telefone (ddd, numero, referencia, idFornecedor) VALUES ('{}', '{}', '{}', '{}')"
    query = base_query.format(telefone.ddd, telefone.numero, telefone.referencia, idFornecedor)

    conn.cursor.execute(query)

    if not conn.cursor.rowcount:
        print "Nenhum dado inserido"
        return

    idTelefone = conn.cursor.lastrowid
    print idTelefone

    conn.db.commit()


def update(telefone):
    base_query = "UPDATE telefone SET ddd = '{}', numero = '{}', referencia = '{}' WHERE id = '{}'"
    query = base_query.format(telefone.ddd, telefone.numero, telefone.referencia, telefone.id)
    conn.cursor.execute(query)

    if not conn.cursor.rowcount:
        print "Nenhum dado alterado"
        return

    conn.db.commit()


def delete(telefone):
    base_query = "DELETE FROM telefone WHERE id = '{}'"
    query = base_query.format(telefone.id)
    conn.cursor.execute(query)

    if not conn.cursor.rowcount:
        print "Nenhum dado apagado"
        return

    conn.db.commit()
