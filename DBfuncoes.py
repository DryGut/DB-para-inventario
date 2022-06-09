#criando o banco de dados para registro de entrada e saida
#exemplo: uma biblioteca.

import sqlite3
import os
import io
import datetime

class Connect():

  def __init__(self, db_name):
    """
      Acessando e Criando 
      o Banco de Dados
                          """
    try:
      #conectando...
      self.conn = sqlite3.connect(db_name)
      self.cursor = self.conn.cursor()

    except sqlite3.Error:
      print('Erro ao se conectar ao DB')
      return False

  def commit_db(self):
    """
        conecta ao Banco de Dado 
        para fazer as devidas alterações
                                          """
    if self.conn:
      self.conn.commit()

  def close_db(self):
    """
    fecha a conexão
                    """
    if self.conn:
      self.conn.close()
      print('Conexao Encerrada')


class BibliotecaDB():
  """
      criando classe para
      gerar as tabelas e funções 
      inserir, atualizar, consultar
      e deletar dados existentes
                                  """

  nome_tb = 'nomedoDB'
  
  def __init__(self):
    """
    conectando ao Banco de Dados
                                    """

    self.db = Connect('nomedoDB.db')
    self.nome_tb

  def fechar_conexao(self):
    """
    fechando a conexao
                      """
    self.db.close_db()

  def criar_schema(self, table_schema='nomedatabela_schema.sql'):
    """
    Criando a tabela a partir
    de um arquivo
                              """

    print('Criando Tabela %s...' % self.nome_tb)

    try:
      with open(table_schema, 'rt') as f:
        schema = f.read()
        self.db.cursor.executescript(schema)

    except sqlite3.Error:
      print('Aviso: A Tabela ja Existe %s' % self.nome_tb)
      return False
    print('Tabela criada com Sucesso')

  def registrar(self):
    """
        metodo para inserir os
        os registro de movimentação
        de livro na biblioteca
                                    """

    self.nome = input('Nome: ')
    self.sobrenome = input('sobrenome: ')
    self.livro = input('Titulo do livro: ')
    self.autor = input('Autor: ')
    self.data_saida = datetime.datetime.now()
    
    """
      se quiser inserir a data ao inves da data automatica atual
      
      data = datetime.datetime.now().isoformat(" ")
      self.data_saida = input('Insira data de Registro (%s): ' % data) or data
      
      este formato pedirá a data, se não for especificada uma, sera usada a data atual.
                                                                                       """

    try:
      self.db.cursor.execute("""
                             INSERT INTO table(
                             nome,
                             sobrenome,
                             livro,
                             autor,
                             data_saida)
                             VALUES(?, ?, ?, ?, ?)
                             """, (self.nome, self.sobrenome, self.livro, self.autor, self.data_saida))

      self.db.commit_db()
      print('Registro Efetuado com Sucesso')

    except sqlite3.IntegrityError:
      print('Dados Invalidos')
      return False

  
  def localizador(self, id):
    """
    busca pelo registro para que
    seja feita as devidas alterações
                                    """
    p = self.db.cursor.execute('SELECT * FROM registro WHERE id = ?', (id, ))
    
    return p.fetchone()

  def atualizar_registro(self, id):
    """
    inserindo data de devolução
    conforme entrega do livro
                                """
    try:
      
      a = self.localizador(id)

      if a:
        self.data_retorno = input('Livro Devolvido em: ' )

        self.db.cursor.execute("""
                                UPDATE registro SET
                                data_retorno = ?
                                WHERE id = ?
                                """, (self.data_retorno, id, ))
        self.db.commit_db()
        print('Registro Efetuado com Sucesso')

      else:
        print('Dados Invalidos')

    except ValueError:
      return None

  def deletar_registro(self, id):
    """
        deletando registro se for
        necessario
                                  """
    try:

      a = self.localizador(id)

      if a:
        self.db.cursor.execute("""
                               DELETE FROM registro
                               WHERE id = ?
                               """, (id, ))
        self.db.commit_db()
        print('Registro removido com Sucesso')

      else:
        print('Dados Invalidos')

    except ValueError:
      return None

  def ler_registro(self):

      sql = 'SELECT * FROM registro ORDER BY '
      r = self.db.cursor.execute(sql)
      return r.fetchall()
    
  def imprimir_registro(self):
    lista = self.ler_registro()
    for c in lista:
      print(c)
