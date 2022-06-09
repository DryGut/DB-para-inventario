-- definição da tabela registro.

CREATE TABLE registro (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL,
	sobrenome	VARCHAR(30) NOT NULL,
	livro TEXT NOT NULL,
	autor TEXT NOT NULL,
	data_saida DATETIME NOT NULL,
  data_retorno VARCHAR(10)
);
