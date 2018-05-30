import lexico as Lexico
import sintatico as Sintatico

if __name__ == "__main__":
	
	#JEITO CERTO
	#arquivo = input('Nome do arquivo a ser analisado:')
	# Lexico.Lexico().run(arquivo) 

	# GAMBIARRA
	lista_tokens = Lexico.Lexico().run("codigo-fonte.c")
	for i in lista_tokens:
		print (str(i))

	root = Sintatico.Programa(lista_tokens)
	# print('Árvore de Sintaxe Abstrata: ')
	# Sintatico.print_tree(root)
	# print('\n-------------')
	# print('Tabela de símbolos')
	# print(str(Sintatico.tabSimbolos))
	# print('-------------')


