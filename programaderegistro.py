#fazendo a inserção dos registros no DB

from biblioteca import Connect, BibliotecaDB

c = BibliotecaDB()

registrar = True

prompt = input(' Selecione a opção desejada:\n'
              '\n [ 1 ] para novo Registro'
              '\n [ 2 ] para registro de Devolução'
              '\n [ 3 ] para Cancelar\n'
              '\n Digite sua escolha: ')

if prompt == '1':
  while registrar:
    c.registrar()

    registro = input("\nDeseja adicionar outro registro?(S/N): ")

    if registro == 'n':
      print('\no000o . Sessão Finalizada . o000o')
      registrar = False


elif prompt == '2':
  while registrar:
    muda = input('\nInsira um prontuario valido: ')
    if muda:
      c.imprimir_registro()
      registrar = False

    muda1 = input('\nInsira o ID para atualizar: ')

    if muda1:
      c.atualizar_registro(muda1)
      print('\no000o . Sessão Finalizada . o000o')
      registrar = False

else:
  print('\no000o . Sessão Finalizada . o000o')
