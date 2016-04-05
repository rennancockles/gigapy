# -*- coding: utf-8 -*-

from DAO.Connection import conn
from Model.Email import Email


def list():
    query = "SELECT * FROM email"
    conn.cursor.execute(query)

    if not conn.cursor.rowcount:
        print "Nenhum dado encontrado"
        return

    emails = []
    columns = [i[0] for i in conn.cursor.description]

    for row in conn.cursor.fetchall():
        email = Email()
        email.from_db(columns, row)
        emails.append(email)
        print email

    return emails


def find_by_email(email):
    base_query = "SELECT * FROM email WHERE email = '{}'"
    query = base_query.format(email)
    conn.cursor.execute(query)

    if not conn.cursor.rowcount:
        print "Nenhum dado encontrado"
        return

    emails = []
    columns = [i[0] for i in conn.cursor.description]

    for row in conn.cursor.fetchall():
        email = Email()
        email.from_db(columns, row)
        emails.append(email)
        print email

    return emails


def find_by_id(id):
    base_query = "SELECT * FROM email WHERE id = '{}'"
    query = base_query.format(id)
    conn.cursor.execute(query)

    if not conn.cursor.rowcount:
        print "Nenhum dado encontrado"
        return

    columns = [i[0] for i in conn.cursor.description]
    row = conn.cursor.fetchone()

    email = Email()
    email.from_db(columns, row)
    print email

    return email


def find_by_fornecedor(fornecedor):
    base_query = "SELECT * FROM email WHERE idFornecedor = '{}'"
    query = base_query.format(fornecedor.id)
    conn.cursor.execute(query)

    if not conn.cursor.rowcount:
        print "Nenhum dado encontrado"
        return

    emails = []
    columns = [i[0] for i in conn.cursor.description]

    for row in conn.cursor.fetchall():
        email = Email()
        email.from_db(columns, row)
        emails.append(email)

    return emails


def insert(idFornecedor, email):
    base_query = "INSERT INTO email (email, referencia, idFornecedor) VALUES ('{}', '{}', '{}')"
    query = base_query.format(email.email, email.referencia, idFornecedor)

    conn.cursor.execute(query)

    if not conn.cursor.rowcount:
        print "Nenhum dado inserido"
        return

    idEmail = conn.cursor.lastrowid

    conn.db.commit()


def update(email):
    base_query = "UPDATE email SET email = '{}', referencia = '{}' WHERE id = '{}'"
    query = base_query.format(email.email, email.referencia, email.id)
    conn.cursor.execute(query)

    if not conn.cursor.rowcount:
        print "Nenhum dado alterado"
        return

    conn.db.commit()


def delete(email):
    base_query = "DELETE FROM email WHERE id = '{}'"
    query = base_query.format(email.id)
    conn.cursor.execute(query)

    if not conn.cursor.rowcount:
        print "Nenhum dado apagado"
        return

    conn.db.commit()


# list()
# find_by_email("forn1@lardocelar.com")
# e = find_by_id(4)
# e.referencia = 'meu mesmo'
# update(e)
# delete(4)

# e = Email(email='eu@me.com', referencia='meu mesmo')
# insert(2, e)
# list()

# conn.close_connection()
