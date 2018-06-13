#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#TOKEN CODES

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

int_type = 0
float_type = 1

typeNames = {}
typeNames[int_type] = 'int'
typeNames[float_type] = 'float'


dic_tokens = { ID: 'ID', MAIN: 'MAIN',INT: 'INT',FLOAT: 'FLOAT',IF: 'IF',ELSE: 'ELSE',WHILE: 'WHILE',READ: 'READ',PRINT: 'PRINT', LBRACKET: 'LBRACKET' ,RBRACKET: 'RBRACKET',LBRACE: 'LBRACE',RBRACE: 'RBRACE',COMMA: 'COMMA',PCOMMA: 'PCOMMA',ATTR: 'ATTR',LT: 'LT',LE: 'LE',GT: 'GT',GE: 'GE',EQ: 'EQ',NE: 'NE',OR: 'OR',AND: 'AND',PLUS: 'PLUS',MINUS: 'MINUS',MULT: 'MULT',DIV: 'DIV', INTEGER_CONST: 'INTEGER_CONST', FLOAT_CONST: 'FLOAT_CONST', FOR : 'FOR'}

i = 0
# token = vetorTokens[i]

Follow = {}
Follow[INTEGER_CONST] = ['MULT','DIV','PLUS','MINUS','RBRACKET','EOF']
Follow[FLOAT_CONST] = ['MULT','DIV','PLUS','MINUS','RBRACKET','EOF']
Follow[ID] = ['MULT','DIV','PLUS','MINUS','RBRACKET','EOF']
Follow[LBRACKET] = ['ID','NUM', 'LBRACKET']
Follow[MINUS] = ['ID','NUM', 'LBRACKET']
Follow[PLUS] = ['ID','NUM', 'LBRACKET']
Follow[MULT] = ['ID','NUM', 'LBRACKET']
Follow[DIV] = ['ID','NUM', 'LBRACKET']
conjSincronismo = [INTEGER_CONST, FLOAT_CONST, ID,LBRACKET,MULT,DIV,PLUS,MINUS,RBRACKET,EOF]

vetorTokens = []
currentType = None
currentTableEntry = None
currentToken = None

class AST(object):
    def __init__(self, nome):
         self.nome = nome
         self.children = []
         self.tipo = None  #tipo do nó. Compound, Assign, ArithOp, etc
         self.valor = None

    def __str__(self, level=0):
        ret = "   "*level+ repr(self) +"\n"
        for child in self.children:
            if (child != None):
                ret += child.__str__(level+1)  #level+1
        return ret

    def __repr__(self):
        return self.nome

    def __evaluate__(self):
        for child in self.children:
            if (child != None):
                return child.__evaluate__()

    def tabs(self, level):
        deslocamento = ""
        while (level!=0):
            level = level - 1
            deslocamento += "    "
        return deslocamento

    def printNode(self, level):
        deslocamento = self.tabs(level)
        print(deslocamento + "<" + str(self.nome) + ">")
        arquivoSaida.write(deslocamento + "<" + str(self.nome) + ">\n")
        
        for child in self.children:
            # if (child != None):
            child.printNode(level+1)
        
        print(deslocamento + "</" + str(self.nome) + ">")
        arquivoSaida.write(deslocamento + "</" +str(self.nome) + ">\n")
        


class Token(object):
    def __init__(self, type, valor,numLinha):
        self.type = type
        self.lexema = valor
        self.numLinha = numLinha
        self.valor = None

    def __str__(self, level=0):
        """String representation of the class instance.

    #     Examples:
    #         Token(INTEGER_CONST, 3)
    #         Token(PLUS, '+')
    #         Token(MUL, '*')
    #     """
        return '{type}: <lexema: {lexema}, tipo: {type}, valor: {valor}, num_linha: {numlinha}>'.format(
            type = dic_tokens[self.type],
            lexema = self.lexema,
            valor = self.valor,
            numlinha = self.numLinha
        )

    def __repr__(self):
        #return self.__str__()
        # return str(self.type)
        return str("Token")

    def __convertTo__(self):
        return
    def printNode(self, level):
        # deslocamento = self.tabs(level)
        print(deslocamento + "< Token >")

class Compound(AST):
    """Represents a 'BEGIN ... END' block"""
    def __init__(self):
        AST.__init__(self,'Block')
        print('Criando um nó do tipo Block.')
        self.children = []

    def __repr__(self):
        return self.nome
    
    def __str__(self, level):
        return str(self.nome)


class Attr(AST):
    def __init__(self, left, op, right):
        AST.__init__(self,'Attr')
        print('Criando um nó do tipo Attr.')
        self.op = op
        self.children.append(left)
        self.children.append(right)
        print (left)
       
    def __repr__(self):
        return str(self.nome)
    def __str__(self, level):
        return str(self.nome)
   
class If(AST):
    def __init__(self, exp, c_true, c_false):
        AST.__init__(self, 'If')
        print('Criando um nó do tipo If.')
        self.children.append(exp)
        self.children.append(c_true)
        self.children.append(c_false)
        self.exp = exp    
        self.c_true = c_true
        self.c_false = c_false

    def __init__(self,  nome):
    	AST.__init__(self, "If")

    def __repr__(self):
        return str(self.nome)
    def __str__(self, level):
        return str(self.nome)

class While(AST):
    def __init__(self, exp, commands):
        AST.__init__(self,'While')
        print('Criando um nó do tipo While.')
        self.children.append(exp)
        self.children.append(commands)
    def __init__(self,nome):
    	AST.__init__(self, nome)

    def __repr__(self):
        return str(self.nome)
    def __str__(self, level):
        return str(self.nome)

class For(AST):
    def __init__(self, exp, commands):
        AST.__init__(self,'For')
        print('Criando um nó do tipo For.')
        self.children.append(exp)
        self.children.append(commands)
    def __init__(self,nome):
    	AST.__init__(self, nome)
    def __repr__(self):
        return str(self.nome)
    def __str__(self, level):
        return str(self.nome)

class Read(AST):
    def __init__(self):
        AST.__init__(self,'Read')
        print('Criando um nó do tipo Read.')

    def __repr__(self):
        return str(self.nome)
    def __str__(self, level=0):
        return str(self.nome)

class Print(AST):
    def __init__(self):
        AST.__init__(self,'Print')
        print('Criando um nó do tipo Print.')

    def __repr__(self):
        return str(self.nome)
    def __str__(self, level=0):
        return str(self.nome)
    def printNode(self, level):       
        deslocamento = self.tabs(level)
        print(deslocamento + "<" + str(self.nome) +" >")
        arquivoSaida.write(deslocamento + "<" + str(self.nome)+ " >\n")
        for child in self.children:
            # if (child != None):
            child.printNode(level+1)
        
        print(deslocamento + "</" + str(self.nome) + ">")
        arquivoSaida.write(deslocamento + "</" +str(self.nome) + ">\n")

class BinOp(AST):
    def __init__(self, nome, op, left, right):
        AST.__init__(self,nome)
        self.op = op
        self.children.append(left)
        self.children.append(right)
    def __str__(self, level=0):
        return str(self.nome)

    def __repr__(self):
        # return str("op")
        return str(self.op)  # + ': ' + self.children[0].__repr__() + ', ' + self.children[1].__repr__()
    
    def printNode(self, level):       
        deslocamento = self.tabs(level)
        print(deslocamento + "<" + str(self.nome) + " op='" + str(self.op) +"' >")
        arquivoSaida.write(deslocamento + "<" + str(self.nome)+ " op='" + str(self.op) +"' >\n")
        for child in self.children:
            # if (child != None):
            child.printNode(level+1)
        
        print(deslocamento + "</" + str(self.nome) + ">")
        arquivoSaida.write(deslocamento + "</" +str(self.nome) + ">\n")

class LogicalOp(BinOp):
    def __init__(self, op, left, right):
        BinOp.__init__(self,'LogicalOp', op, left, right)
        print('Criando um nó do tipo LogicalOp com operador ' + str(op))
    def __str__(self, level=0):
        return str(self.nome)
    def printNode(self, level):       
        deslocamento = self.tabs(level)
        print(deslocamento + "<" + str(self.nome) + " op='" + str(self.op) +"' >")
        arquivoSaida.write(deslocamento + "<" + str(self.nome)+ " op='" + str(self.op) +"' >\n")
        for child in self.children:
            # if (child != None):
            child.printNode(level+1)
        
        print(deslocamento + "</" + str(self.nome) + ">")
        arquivoSaida.write(deslocamento + "</" +str(self.nome) + ">\n")

class ArithOp(BinOp):
    def __init__(self, op, left, right):
        BinOp.__init__(self,'ArithOp', op, left, right)
        print('Criando um nó do tipo ArithOp com operador ' + str(op))
    def __str__(self, level=0):
        return str(self.nome)
    def printNode(self, level):       
        deslocamento = self.tabs(level)
        print(deslocamento + "<" + str(self.nome) + " op='" + str(self.op) +"' >")
        arquivoSaida.write(deslocamento + "<" + str(self.nome)+ " op='" + str(self.op) +"' >\n")
        for child in self.children:
            # if (child != None):
            child.printNode(level+1)
        
        print(deslocamento + "</" + str(self.nome) + ">")
        arquivoSaida.write(deslocamento + "</" +str(self.nome) + ">\n")

class RelOp(BinOp):
    def __init__(self, op, left, right):
        BinOp.__init__(self,'RelOp', op, left, right)
        print('Criando um nó do tipo RelOp com operador ' + str(op))
    def __str__(self, level=0):
        return str(self.nome)
    def printNode(self, level):       
        deslocamento = self.tabs(level)
        print(deslocamento + "<" + str(self.nome) + " op='" + str(self.op) +"' >")
        arquivoSaida.write(deslocamento + "<" + str(self.nome)+ " op='" + str(self.op) +"' >\n")
        for child in self.children:
            # if (child != None):
            child.printNode(level+1)
        
        print(deslocamento + "</" + str(self.nome) + ">")
        arquivoSaida.write(deslocamento + "</" +str(self.nome) + ">\n")

class Id(AST):
    def __init__(self, token):
        AST.__init__(self,'Id')
        print('Criando um nó do tipo Id.')
        self.token = token
    def __str__(self, level=0):
        return str("ID")

    def __repr__(self):
        # return str(self.token)
        return str("ID")
    
    def printNode(self, level):
        deslocamento = self.tabs(level)
        print(deslocamento + "<" + self.nome, end='')
        arquivoSaida.write(deslocamento + "<" + self.nome)   
        tipoTabelaSimbolos = getIdTabelaSimbolos(str(self.token.lexema)) 
        print(" lexema='" + str(self.token.lexema) +"' type='"+ str(tipoTabelaSimbolos) + "' />")
        arquivoSaida.write(" lexema='" + str(self.token.lexema) +"' type='"+ tipoTabelaSimbolos + "' />\n")

class Num(AST):
    def __init__(self, token, type_):
        AST.__init__(self,'Num')
        print('Criando um nó do tipo Num.')
        self.token = token
        self.valor = float(token.lexema)  #em python, não precisamos nos preocupar com o tipo de value
        self.type = type_

    def __repr__(self):
        return str("Num")

    def __evaluate__(self):
        return self.valor
    def __str__(self, level=0):
        return str(self.nome)
   
    def printNode(self, level):
        deslocamento = self.tabs(level)
        print(deslocamento + "<" + self.nome, end='')
        arquivoSaida.write(deslocamento + "<" + self.nome)        
        print(" value=" + str(self.token.lexema) +" type='"+ str(dic_tokens[self.token.type]) + "' />")
        arquivoSaida.write(" value=" + str(self.token.lexema) +" type='"+ str(dic_tokens[self.token.type]) + "' />\n")

def match(tok):
    global token, i
    print (tok)
    if(token.type == tok):
        #print('Token ' + repr(token) + ' reconhecido na entrada.')
        i = i + 1
        if (i < len(vetorTokens)):
            token = vetorTokens[i]
    else:
        print('Erro sintático. Token ' + repr(token) + ' não esperado na entrada.')
       
def TabelaSimbolos():
    print("Tabela de simbolos")
    global lista_tabelaSimbolos 
    lista_tabelaSimbolos = {}
    iterator = 0

    for it in range(0,len(vetorTokens)): 
        if(vetorTokens[it].type == INTEGER_CONST or vetorTokens[it].type == FLOAT_CONST):
            vetorTokens[it].valor = vetorTokens[it].lexema
        elif(vetorTokens[it].type == ID and (vetorTokens[it-1].type == INT or vetorTokens[it-1].type == FLOAT)):
            lista_tabelaSimbolos[iterator] = vetorTokens[it].lexema,dic_tokens[vetorTokens[it-1].type],0
            iterator += 1
        elif(vetorTokens[it].type == ID and vetorTokens[it-1].type == COMMA):
            aux = it
            tipo = None
            while(aux > 1):
                aux -= 1
                if(vetorTokens[aux].type == INT):
                    tipo = INT
                    break
                elif(vetorTokens[aux].type == FLOAT):
                    tipo = FLOAT
                    break

            lista_tabelaSimbolos[iterator] = vetorTokens[it].lexema,dic_tokens[tipo],0
            iterator += 1
           
    printTabelaSimbolos()

def getIdTabelaSimbolos(id):
    for it in range(0,len(lista_tabelaSimbolos)): 
        if(id == lista_tabelaSimbolos[it][0]):
            return(lista_tabelaSimbolos[it][1])
    return "None"

def printTabelaSimbolos():
    print(lista_tabelaSimbolos)

def Programa(lista_tokens, nomeArquivoSaida):
    print("\nAnalisador Sintatico CSmall")
    global token, currentType, currentToken, arquivoSaida

    for a in lista_tokens:
        vetorTokens.append(a)

    TabelaSimbolos()
    token = lista_tokens[i]

    match(INT)
    match(MAIN)
    match(LBRACKET)
    match(RBRACKET)
    match(LBRACE)

    lista = AST('Main')
    ast = Decl_Comando(lista)
    match(RBRACE)
    
    arquivoSaida = open(nomeArquivoSaida,'w')
    level = 0
    ast.printNode(level)
    arquivoSaida.close()
    print('Fim da análise sintática.\n')
    return ast

def Decl_Comando(lista):
    global token,  currentType,  currentToken

    if (token.type == INT or token.type == FLOAT):
        no1 = Declaracao(lista)
        return Decl_Comando(no1)
    elif (token.type == ID or token.type == IF or token.type == WHILE or token.type == PRINT
          or token.type == READ or token.type == FOR):
        no1 = Comando(lista) #Criamos nós na ast para cada comando encontrado
        return Decl_Comando(no1)
    else:
        return lista

def Declaracao(no):
    global token,  currentType, currentToken, id_node
    Tipo()  
    if (token.type == ID):
        currentToken = token
        id_node = Id(token)
        match(ID) #cria uma entrada na tabela de símbolos para esse identificador
        return Decl2(no)
    return no

def Tipo():
    global token,  currentType,  currentToken
    if (token.type == INT):
        match(INT)
        currentType = int_type
    elif (token.type == FLOAT):
        match(FLOAT)
        currentType = float_type

def Decl2(no):
    global token,  currentType,  currentToken, id_node
   
    if (token.type == COMMA):
        match(COMMA)
        if (token.type == ID):
            id_node = Id(token)
            match(ID)
            return Decl2(no)
    elif (token.type == PCOMMA):
        match(PCOMMA)
        return no
    elif (token.type == ATTR):
        match(ATTR)
        expr_node = Expressao()
        attr_node = Attr(id_node, '=', expr_node)
        no.children.append(attr_node)
        return Decl2(no)
    return no

def Comando(lista):
	if(token.type == LBRACE):
		return Bloco(lista)
	elif(token.type == FOR):
		return ComandoFor(lista)
	elif(token.type == ID):
		return Atribuicao(lista)
	elif(token.type == IF):
		return ComandoSe(lista)
	elif(token.type == WHILE):
		return ComandoEnquanto(lista)
	elif(token.type == READ):
		return ComandoRead(lista)
	elif(token.type == PRINT):
		return ComandoPrint(lista)

def Bloco(lista):
	match(LBRACE)
	bloco = AST('Bloco')
	retorno = Decl_Comando(bloco)
	match(RBRACE)	
	lista.children.append(retorno)
	return lista

def Atribuicao(lista):
    global id_node
    id_node = Id(token)
    match(ID)
    match(ATTR)
    expr_node = Expressao()
    lista.children.append(Attr(id_node,'=',expr_node))
    match(PCOMMA)
    return lista

def ComandoRead(lista):
	read_node = Read()
	match(READ)
	id_node = Id(token)
	read_node.children.append(id_node)
	match(ID)
	match(PCOMMA)	
	lista.children.append(read_node)		
	return lista

def ComandoSe(lista):
	if_node = If(IF)
	match(IF)
	match(LBRACKET)
	expr_node = Expressao()
	if_node.children.append(expr_node)
	match(RBRACKET)
	c_true = AST('C_TRUE')
	retorno = Comando(c_true)
	if_node.children.append(retorno)
	ComandoSenao(if_node)	
	lista.children.append(if_node)
	return lista

def ComandoSenao(if_node):
	if(token.type == ELSE):
		c_false = AST('C_FALSE')
		match(ELSE)
		retorno = Comando(c_false)
		if_node.children.append(retorno)
		return if_node
	else:
		return if_node

def ComandoEnquanto(lista):
	while_node = While("While")
	match(WHILE)
	match(LBRACKET)
	expr_node = Expressao()
	while_node.children.append(expr_node)
	match(RBRACKET)
	c_true = AST('C_TRUE')
	retorno = Comando(c_true)
	while_node.children.append(retorno)
	lista.children.append(while_node)
	return lista

def ComandoFor(lista):
	global id_node
	for_node = For("For")
	match(FOR)
	match(LBRACKET)
	id_node = Id(token)
	match(ID)
	match(ATTR)
	expr_node = Expressao()
	for_node.children.append(Attr(id_node,'=',expr_node))
	match(PCOMMA)
	expr_node = Expressao()
	for_node.children.append(expr_node)
	match(PCOMMA)	
	id_node = Id(token)
	match(ID)
	match(ATTR)
	expr_node = Expressao()
	for_node.children.append(Attr(id_node,'=',expr_node))	
	match(RBRACKET)
	c_true = AST('C_TRUE')
	retorno = Comando(c_true)
	for_node.children.append(retorno)
	lista.children.append(for_node)
	return lista

# ComandoFor → FOR LBRACKET AtribuicaoFor PCOMMA Expressao PCOMMA AtribuicaoFor RBRACKET Comando
# AtribuicaoFor → ID ATTR Expressao

def ComandoPrint(lista):
	print_node = Print()
	match(PRINT)
	match(LBRACKET)
	expr = Expressao()
	print_node.children.append(expr)
	match(RBRACKET)
	match(PCOMMA)	
	lista.children.append(print_node)	
	return lista


def Expressao():      
    expr = Conjuncao()
    return ExpressaoOpc(expr)

def ExpressaoOpc(expr):
	if(token.type == OR):
		match(OR)
		expr2 = Conjuncao()
		or_node = LogicalOp('||',expr,expr2)
		expr2 = ExpressaoOpc(or_node)		
		return expr2
	else: 
		return expr

def Conjuncao():
	expr = Igualdade()
	return ConjuncaoOpc(expr)


def ConjuncaoOpc(expr):
	if(token.type == AND):
		match(AND)
		expr2= Igualdade()
		and_node = LogicalOp('&&',expr,expr2)
		expr2 = ConjuncaoOpc(and_node)		
		return expr2
	else:
		return expr

def Igualdade():
	expr = Relacao()
	return IgualdadeOpc(expr)

def IgualdadeOpc(expr):
	if(token.type == EQ):
		match(EQ)
		expr2 = Relacao()
		igual_node = RelOp('==',expr,expr2)
		return IgualdadeOpc(igual_node)
	elif(token.type == NE):
		match(NE)	
		expr2 = Relacao()
		diferente_node = RelOp('!=',expr,expr2)
		return IgualdadeOpc(diferente_node)
	else : 
		return expr

def Relacao():
	expr = Adicao()
	return RelacaoOpc(expr)


def RelacaoOpc(expr):
	if(token.type == LT):
		OpRel()
		expr2 = Adicao()
		menor_node = RelOp('<',expr,expr2)
		return RelacaoOpc(menor_node)
	elif(token.type == LE):
		OpRel()
		expr2 = Adicao()
		menorigual_node = RelOp('<=',expr,expr2)
		return RelacaoOpc(menorigual_node)
	elif(token.type == GT):
		OpRel()
		expr2 = Adicao()
		maior_node = RelOp('>',expr,expr2)
		return RelacaoOpc(maior_node)
	elif(token.type == GE):
		OpRel()
		expr2 = Adicao()
		maiorigual_node = RelOp('>=',expr,expr2)
		return RelacaoOpc(maiorigual_node)
	else : 
		return expr	

	
def OpRel():
	if(token.type == LT ):
		match(LT)
	elif(token.type == LE) :
		match(LE)		
	elif(token.type == GT):
		match(GT)		
	elif(token.type == GE):
		match(GE)



def Adicao():
    global token,  currentType,  currentToken
    no_ope1 = Termo()
    return AdicaoOpc(no_ope1)

def AdicaoOpc(no_ope1):
    global token,  currentType,  currentToken
    if(token.type == PLUS):
        match(PLUS)
        no_ope2 = Termo()
        no = ArithOp('+', no_ope1, no_ope2)
        return AdicaoOpc(no)
    elif (token.type == MINUS):
        match(MINUS)
        no_ope2 = Termo()
        no = ArithOp('-', no_ope1, no_ope2)
        return AdicaoOpc(no)
    else:
        return no_ope1

def Termo():
    global token, currentType, currentToken
    no_ope1 = Fator()
    return TermoOpc(no_ope1)

def TermoOpc(no_ope1):
    global token, currentType, currentToken
    if (token.type == MULT):
        match(MULT)
        no_ope2 = Fator()
        no = ArithOp('*', no_ope1, no_ope2)
        return TermoOpc(no)
    elif(token.type == DIV):
        match(DIV)
        no_ope2 = Fator()
        no = ArithOp('/', no_ope1, no_ope2)
        return TermoOpc(no)
    else:
        return no_ope1


def Fator():
    global token, currentType, currentToken
    if(token.type == LBRACKET):
        match(LBRACKET)
        expr = Expressao()
        match(RBRACKET)
        return expr
    elif (token.type == ID):
        id_node = Id(token)
        match(ID)
        return id_node
    elif(token.type == INTEGER_CONST):
        num_node = Num(token, int_type)
        match(INTEGER_CONST)
        return num_node
    elif(token.type == FLOAT_CONST):
        num_node = Num(token, float_type)
        match(FLOAT_CONST)
        return num_node
