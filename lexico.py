import regex as regex
import sintatico as token

class Lexico():

	def __init__(self):
		self.dic_tokens = {'id': ID, 'main': MAIN, 'int': INT, 'float': FLOAT, 'if': IF,'else': ELSE,'while': WHILE, 'read': READ,'print': PRINT,'(': LBRACKET,')': RBRACKET,'{': LBRACE,'}': RBRACE,',': COMMA,';': PCOMMA,'=': ATTR,'<': LT,'<=': LE,'>': GT,'>=': GE,'==': EQ,'!=': NE,'||': OR,	'&&': AND,'+': PLUS,'-': MINUS,'*': MULT,'/': DIV, 'num_integer': INTEGER_CONST, 'num_float': FLOAT_CONST, '!': 'EXCLAMACAO', 'for': FOR}
		self.operadores = ['+','-','*','/','=','<','>','!','&','|']
		self.separadores = [' ', '\n', '\t', '(', ')','{','}',',',';','\r']

	def num_inteiro(self, token):
		result = regex.match("^-?\\d*(\\d+)?$", token)
		if result == None:
			return False
		else:
			 return True

	def num_float(self, token):
		result = regex.match("([0-9]+[.])+[0-9]+", token)
		if result == None:
			return False
		else:
			 return True
	
	def identificador(self, token):
		result = regex.match('[A-Za-z]([A-Za-z]|[0-9])*', token)
		if result == None:
			return False
		else:
			 return True

	def run(self,arquivo):

		print ("Analisador Lexico CSmall")

		#lista que armazenara os tokens
		lista_tokens = list()
		#arquivo que contem o codigo fonte a ser analisado
		arq = open(arquivo, 'r')
		codigofonte = list(arq.read())
		#variavel que marca em qual linha se encontra a leitura do arquivo
		linha = 0
		#Buffer de leitura 
		buffer = ""
		flag = 0
		aux = ""

		#inicio do for que le o codigo fonte
		for c in codigofonte:

			#se o caractere lido for quebra de linha, aumenta o contador de linhas
			if c == '\n':
				linha += 1
			
			#verificando se foi encontrado \ ou &
			if(c == '|' or c == '&' ):

				if flag == 1:
					if aux == c:
						novotoken = token.Token(self.dic_tokens[c+aux],c+aux,linha)
						# novotoken = token.Token(self.dic_tokens[c+aux],c+aux)
						lista_tokens.append(novotoken)
					flag = 0
					aux = ""
				else:
					flag = 1
					aux = c

			else:
				#se o caractere lido for um separado ou operador
				if (c in self.separadores or c in self.operadores):
					if buffer != "":
						
						if buffer in self.dic_tokens:
							novotoken = token.Token(self.dic_tokens[buffer],buffer,linha)
							lista_tokens.append(novotoken)
							buffer = ""
						else:
							if(self.num_inteiro(buffer) or self.num_float(buffer) or self.identificador(buffer)):
								if self.num_inteiro(buffer):
									novotoken = token.Token(self.dic_tokens['num_integer'],buffer,linha)
								elif self.num_float(buffer):
									novotoken = token.Token(self.dic_tokens['num_float'],buffer,linha)
								elif self.identificador(buffer):
									novotoken = token.Token(self.dic_tokens['id'],buffer,linha)
								lista_tokens.append(novotoken)
								buffer = ""
					if c in self.dic_tokens:
						novotoken = token.Token(self.dic_tokens[c],c,linha)
						lista_tokens.append(novotoken)
				else:
					buffer = buffer + c
			
			#verificando se foi encontrado os tokens ==, !=, <=, >= 
			if len(lista_tokens) > 2:
				if lista_tokens[-1].lexema == lista_tokens[-2].lexema == '=':
					lista_tokens.pop()
					lista_tokens.pop()
					novotoken = token.Token(self.dic_tokens['=='],'==',linha)
					lista_tokens.append(novotoken)
				elif lista_tokens[-1].lexema == '=' and lista_tokens[-2].lexema == '!':
					lista_tokens.pop()
					lista_tokens.pop()
					novotoken = token.Token(self.dic_tokens['!='],'!=',linha)
					lista_tokens.append(novotoken)
				elif lista_tokens[-1].lexema == '=' and lista_tokens[-2].lexema == '<':
					lista_tokens.pop()
					lista_tokens.pop()
					novotoken = token.Token(self.dic_tokens['<='],'<=',linha)
					lista_tokens.append(novotoken)
				elif lista_tokens[-1].lexema == '=' and lista_tokens[-2].lexema == '>':
					lista_tokens.pop()
					lista_tokens.pop()
					novotoken = token.Token(self.dic_tokens['>='],'>=',linha)
					lista_tokens.append(novotoken)
		#fim do for que le o codigo fonte

		#imprime os tokens encontrados
		# for i in lista_tokens:
		# 	print (str(i))

		return lista_tokens

EOF = -1
ID = 0
INTEGER_CONST = 1
FLOAT_CONST = 2
LBRACKET = 3
RBRACKET = 4
PLUS = 5
MINUS = 6
MULT = 7
DIV = 8
INT = 9
FLOAT = 10
MAIN = 11
LBRACE = 12
RBRACE = 13
COMMA = 14
PCOMMA = 15
ATTR = 16
IF = 17
ELSE = 18
WHILE = 19
PRINT = 20
READ = 21
OR = 22
AND = 23
EQ = 24
NE = 25
LT = 26
LE = 27
GT = 28
GE = 29
FOR = 30