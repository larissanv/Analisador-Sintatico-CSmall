class token(object):

	def __init__(self, nome, lexema):
		self.nome = nome
		self.lexema = lexema
		self.num_linha = None
		self.value = None

	# def __str__(self):
	# 	return "Token -> nome:%s \t\t lexema:%s \t\t numero da linha:%s" % (self.nome, self.lexema, self.num_linha)

	def __str__(self):
		return 'token({nome}, {lexema})'.format(
            nome = tokenNames[self.nome],
            lexema = self.lexema
        )
#         """String representation of the class instance.

#         Examples:
#             token(INTEGER_CONST, 3)
#             token(PLUS, '+')
#             token(MUL, '*')
		
	
	def __repr__(self):
        #return self.__str__()
		return str(self.nome)
		
	def __convertTo__(self):
		return

#token CODES

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
ATTR = 1
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

int_type = 0
float_type = 1

typeNames = {}
typeNames[int_type] = 'int'
typeNames[float_type] = 'float'

opmap = {}
opmap[PLUS] = '+'
opmap[MINUS] = '-'
opmap[MULT] = '*'
opmap[DIV] = '/'

tokenNames = {}
tokenNames[EOF] = 'EOF'
tokenNames[ID] = 'ID'
tokenNames[INTEGER_CONST] = 'INTEGER_CONST'
tokenNames[FLOAT_CONST] = 'FLOAT_CONST'
tokenNames[LBRACKET] = 'LBRACKET'
tokenNames[RBRACKET] = 'RBRACKET'
tokenNames[PLUS] = 'PLUS'
tokenNames[MINUS] = 'MINUS'
tokenNames[MULT] = 'MULT'
tokenNames[DIV] = 'DIV'

	