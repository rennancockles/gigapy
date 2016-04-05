# -*- coding: utf-8 -*-

from DAO.Connection import conn
from DAO import FornecedorDAO
from Model.Produto import Produto


def list():
    query = "SELECT * FROM produto"
    conn.cursor.execute(query)

    if not conn.cursor.rowcount:
        print "Nenhum dado encontrado"
        return

    produtos = []
    columns = [i[0] for i in conn.cursor.description]

    for row in conn.cursor.fetchall():
        produto = Produto()
        produto.from_db(columns, row)

        idFornecedor = row[columns.index('idFornecedor')]
        fornecedor = FornecedorDAO.find_by_id(idFornecedor)

        produto.add_fornecedor(fornecedor)

        produtos.append(produto)
        print produto

    return produtos


def find_by_name(name):
    base_query = "SELECT * FROM produto WHERE nome = '{}'"
    query = base_query.format(name)
    conn.cursor.execute(query)

    if not conn.cursor.rowcount:
        print "Nenhum dado encontrado"
        return

    produtos = []
    columns = [i[0] for i in conn.cursor.description]

    for row in conn.cursor.fetchall():
        produto = Produto()
        produto.from_db(columns, row)

        idFornecedor = row[columns.index('idFornecedor')]
        fornecedor = FornecedorDAO.find_by_id(idFornecedor)

        produto.add_fornecedor(fornecedor)

        produtos.append(produto)
        print produto

    return produtos


def find_by_id(id):
    base_query = "SELECT * FROM produto WHERE id = '{}'"
    query = base_query.format(id)
    conn.cursor.execute(query)

    if not conn.cursor.rowcount:
        print "Nenhum dado encontrado"
        return

    columns = [i[0] for i in conn.cursor.description]
    row = conn.cursor.fetchone()

    produto = Produto()
    produto.from_db(columns, row)

    idFornecedor = row[columns.index('idFornecedor')]
    fornecedor = FornecedorDAO.find_by_id(idFornecedor)

    produto.add_fornecedor(fornecedor)

    print produto

    return produto


def insert(produto):
    base_query = "INSERT INTO produto (nome, descricao, idFornecedor) VALUES ('{}', '{}', '{}')"
    query = base_query.format(produto.nome, produto.descricao, produto.fornecedor.id)

    conn.cursor.execute(query)

    if not conn.cursor.rowcount:
        print "Nenhum dado inserido"
        return

    idProduto = conn.cursor.lastrowid

    conn.db.commit()


def update(produto):
    base_query = "UPDATE produto SET nome = '{}', descricao = '{}', idFornecedor = '{}' WHERE id = '{}'"
    query = base_query.format(produto.nome, produto.descricao, produto.fornecedor.id, produto.id)
    conn.cursor.execute(query)

    if not conn.cursor.rowcount:
        print "Nenhum dado alterado"
        return

    conn.db.commit()


def delete(produto):
    base_query = "DELETE FROM produto WHERE id = '{}'"
    query = base_query.format(produto.id)
    conn.cursor.execute(query)

    if not conn.cursor.rowcount:
        print "Nenhum dado apagado"
        return

    conn.db.commit()


# list()
# find_by_name('tinta')
# p = find_by_id(11)
# p.descricao = 'Vodka doida'
# update(p)
# delete(find_by_id(10))

# f = FornecedorDAO.find_by_id(1)
# p = Produto(nome='Absolut', descricao='Bebida forte', fornecedor=f)
# insert(p)
# list()

# conn.close_connection()
