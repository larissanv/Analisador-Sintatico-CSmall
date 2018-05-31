import lexico as Lexico
import sintatico as Sintatico

if __name__ == "__main__":
	
	#arquivo = input('Nome do arquivo a ser analisado:')
	# lista_tokens = Lexico.Lexico().run(arquivo)
	arquivo = "teste1.c"
	lista_tokens = Lexico.Lexico().run(arquivo)

	arquivosaida = arquivo[:-2] 
	arquivosaida += ".txt"

	for i in lista_tokens:
		print (str(i))

	root = Sintatico.Programa(lista_tokens, arquivosaida)
	# print('Árvore de Sintaxe Abstrata: ')
	# Sintatico.print_tree(root)
	# print('\n-------------')
	print('Tabela de símbolos')
	print(Sintatico.printTabelaSimbolos())
	print('-------------')


