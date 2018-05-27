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
	# Sintatico.Programa()

