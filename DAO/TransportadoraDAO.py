# -*- coding: utf-8 -*-

from DAO.Connection import conn
from Model.Transportadora import Transportadora


def list():
    query = "SELECT * FROM transportadora"
    conn.cursor.execute(query)

    if not conn.cursor.rowcount:
        print "Nenhum dado encontrado"
        return

    transportadoras = []
    columns = [i[0] for i in conn.cursor.description]

    for row in conn.cursor.fetchall():
        transportadora = Transportadora()
        transportadora.from_db(columns, row)
        transportadoras.append(transportadora)
        print transportadora

    return transportadoras


def find_by_name(name):
    base_query = "SELECT * FROM transportadora WHERE nome = '{}'"
    query = base_query.format(name)
    conn.cursor.execute(query)

    if not conn.cursor.rowcount:
        print "Nenhum dado encontrado"
        return

    transportadoras = []
    columns = [i[0] for i in conn.cursor.description]

    for row in conn.cursor.fetchall():
        transportadora = Transportadora()
        transportadora.from_db(columns, row)
        transportadoras.append(transportadora)
        print transportadora

    return transportadoras


def find_by_id(id):
    base_query = "SELECT * FROM transportadora WHERE id = '{}'"
    query = base_query.format(id)
    conn.cursor.execute(query)

    if not conn.cursor.rowcount:
        print "Nenhum dado encontrado"
        return

    columns = [i[0] for i in conn.cursor.description]
    row = conn.cursor.fetchone()

    transportadora = Transportadora()
    transportadora.from_db(columns, row)
    print transportadora

    return transportadora


def insert(transportadora):
    base_query = "INSERT INTO transportadora (nome) VALUES ('{}')"
    query = base_query.format(transportadora.nome)

    conn.cursor.execute(query)

    if not conn.cursor.rowcount:
        print "Nenhum dado inserido"
        return

    idTransportadora = conn.cursor.lastrowid
    print idTransportadora

    conn.db.commit()


def update(transportadora):
    base_query = "UPDATE transportadora SET nome = '{}' WHERE id = '{}'"
    query = base_query.format(transportadora.nome, transportadora.id)
    conn.cursor.execute(query)

    if not conn.cursor.rowcount:
        print "Nenhum dado alterado"
        return

    conn.db.commit()


def delete(transportadora):
    base_query = "DELETE FROM transportadora WHERE id = '{}'"
    query = base_query.format(transportadora.id)
    conn.cursor.execute(query)

    if not conn.cursor.rowcount:
        print "Nenhum dado apagado"
        return

    conn.db.commit()


# list()
# find_by_name("vaptvupt")
# t = find_by_id(3)
# t.nome = 'ta chegando'
# update(t)
# delete(3)

# t = Transportadora(nome='chegaja')
# insert(t)
# list()

# conn.close_connection()
