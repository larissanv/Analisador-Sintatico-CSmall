class Token(object):
	
	def __init__(self, nome, lexema, num_linha):
		self.nome = nome
		# self.cod = cod
		self.lexema = lexema
		self.num_linha = num_linha

	def __str__(self):
		return "Token -> nome:%s \t\t lexema:%s \t\t numero da linha:%s" % (self.nome, self.lexema, self.num_linha)