import lexico as Lexico
import sintatico as Sintatico

if __name__ == "__main__":
	
	# arquivo = input('Nome do arquivo a ser analisado:')
	arquivo = "teste1.c"
	lista_tokens = Lexico.Lexico().run(arquivo)

	arquivoSaidaXML = arquivo[:-2] 
	arquivoSaidaXML += "XML.txt"
	arquivoSaidaErros = arquivo[:-2] 
	arquivoSaidaErros += "Erros.txt"

	for i in lista_tokens:
		print (str(i))

	root = Sintatico.Programa(lista_tokens, arquivoSaidaXML, arquivoSaidaErros)
	# print('Árvore de Sintaxe Abstrata: ')
	print('\n-------------')
	print('Tabela de símbolos')
	Sintatico.printTabelaSimbolos()
