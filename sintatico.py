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


class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.lexema = value
        self.numLinha = None
        self.value = None
        # print("Tolkien < type ", self.type, ",lex ", self.lexema,">" )

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER_CONST, 3)
            Token(PLUS, '+')
            Token(MUL, '*')
        """
        return 'Token: <lexema: {lexema}, tipo: {type}, valor: {value}>'.format(
            type = dic_tokens[self.type],
            lexema = self.lexema,
            value = self.value
        )

    def __repr__(self):
        #return self.__str__()
        return str(self.type)

    def __convertTo__(self):
        return

"""
 A tabela de símbolos é implementada como uma classe com o seguinte campo:
     - Map<string,TableEntry> symbolTable //Um mapa de objetos tableEntry
"""
"""
 TableEntry é uma classe que possui os seguintes campos:
     - lexema
     - tipo
     - ponteiro para o valor
     - num da linha
"""
# class SymbolTable(object):
#     def __init__(self):
#         self.symbolTable = {}

#     def insertEntry(self, lexema, entry):
#         self.symbolTable[lexema] = entry

#     def getEntry(self, lexema):
#         if (self.symbolTable[lexema]):
#             return self.symbolTable[lexema]
#         else:
#             return None

#     def __repr__(self):
#         str_res = ''
#         for i in self.symbolTable:
#             str_res += ('{' + str(i) + ',' + str(self.symbolTable[i]) + '}') + '\n'
#         return str_res

# class TableEntry(object):
#     def __init__(self, lexema, tipo, num_linha, ref_valor):
#         self.lexema = lexema
#         self.tipo = tipo
#         self.num_linha = num_linha
#         self.ref_valor = ref_valor

#     def setTipo(self, tipo):
#         self.tipo = tipo

#     def setRefValor(self, rv):
#         self.ref_valor = rv

#     def __repr__(self):
#         return '<lexema: ' + str(self.lexema) + ', tipo: ' + str(self.tipo) + ', valor: ' + str(self.ref_valor) + '>'

class AST(object):
    def __init__(self, nome):
         self.nome = nome
         self.children = []
         self.tipo = None  #tipo do nó. Compound, Assign, ArithOp, etc
         self.value = None

    def __str__(self, level=0):
        ret = "   "*level+ repr(self) +"\n"
        for child in self.children:
            if (child != None):
                ret += child.__str__(level+1) #level+1
        return ret

    def __repr__(self):
        return self.nome

    def __evaluate__(self):
        for child in self.children:
            if (child != None):
                return child.__evaluate__()

class Compound(AST):
    """Represents a 'BEGIN ... END' block"""
    def __init__(self):
        AST.__init__(self,'Block')
        print('Criando um nó do tipo Block.')
        self.children = []

    def __repr__(self):
        return self.nome

class Attr(AST):
    def __init__(self, left, op, right):
        AST.__init__(self,'Attr')
        print('Criando um nó do tipo Attr.')
        self.op = op
        self.children.append(left)
        self.children.append(right)

    def __repr__(self):
        return self.nome

class If(AST):
    def __init__(self, exp, c_true, c_false):
        AST.__init__(self, 'If')
        print('Criando um nó do tipo If.')
        self.children.append(exp)
        self.children.append(c_true)
        self.children.append(c_false)

    def __repr__(self):
        return self.nome


class While(AST):
    def __init__(self, exp, commands):
        AST.__init__(self,'While')
        print('Criando um nó do tipo While.')
        self.children.append(exp)
        self.children.append(commands)

    def __repr__(self):
        return self.nome

class Read(AST):
    def __init__(self, id_):
        AST.__init__(self,'Read')
        print('Criando um nó do tipo Read.')
        self.children.append(id_)

    def __repr__(self):
        return self.nome

class Print(AST):
    def __init__(self, exp):
        AST.__init__(self,'Print')
        print('Criando um nó do tipo Print.')
        self.children.append(exp)

    def __repr__(self):
        return self.nome

class Expr(AST):
    def __init__(self, nome, op, left, right):
        AST.__init__(self,nome)
        self.op = op
        self.children.append(left)
        self.children.append(right)

    def __repr__(self):
        return self.op  # + ': ' + self.children[0].__repr__() + ', ' + self.children[1].__repr__()

class LogicalOp(Expr):
    def __init__(self, op, left, right):
        Expr.__init__(self,'LogicalOp', op, left, right)
        print('Criando um nó do tipo LogicalOp com operador ' + str(op))

class ArithOp(Expr):
    def __init__(self, op, left, right):
        Expr.__init__(self,'ArithOp', op, left, right)
        print('Criando um nó do tipo ArithOp com operador ' + str(op))

class RelOp(Expr):
    def __init__(self, left, op, right):
        Expr.__init__(self,'RelOp', op, left, right)
        print('Criando um nó do tipo RelOp com operador ' + str(op))

class Id(AST):
    def __init__(self, token):
        AST.__init__(self,'Id')
        print('Criando um nó do tipo Id.')
        self.token = token


    def __repr__(self):
        return 'ID: ' + repr(self.token.lexema)

    # def __str__(self):
    #     return str(self.entradaTabSimbolos.lexema)

class Num(AST):
    def __init__(self, token, type_):
        AST.__init__(self,'Num')
        print('Criando um nó do tipo Num.')
        self.token = token
        self.value = float(token.lexema)  #em python, não precisamos nos preocupar com o tipo de value
        self.type = type_

    def __repr__(self):
        return str(self.token)  # + '  tipo: ' + str(self.type)

    # def __str__(self):
    #     return str(self.value)

    def __evaluate__(self):
        return self.value

def print_tree(current_node, indent="", last='updown'):

    nb_children = lambda node: sum(nb_children(child) for child in node.children) + 1
    size_branch = {child: nb_children(child) for child in current_node.children}

    """ Creation of balanced lists for "up" branch and "down" branch. """
    up = sorted(current_node.children, key=lambda node: nb_children(node))
    down = []
    while up and sum(size_branch[node] for node in down) < sum(size_branch[node] for node in up):
        down.append(up.pop())

    """ Printing of "up" branch. """
    for child in up:
        next_last = 'up' if up.index(child) is 0 else ''
        next_indent = '{0}{1}{2}'.format(indent, ' ' if 'up' in last else '│', " " * len(current_node.__repr__()))
        print_tree(child, indent=next_indent, last=next_last)

    """ Printing of current node. """
    if last == 'up': start_shape = '┌'
    elif last == 'down': start_shape = '└'
    elif last == 'updown': start_shape = ' '
    else: start_shape = '├'

    if up: end_shape = '┤'
    elif down: end_shape = '┐'
    else: end_shape = ''

    print('{0}{1}{2}{3}'.format(indent, start_shape, current_node.__repr__(), end_shape))

    """ Printing of "down" branch. """
    for child in down:
        next_last = 'down' if down.index(child) is len(down) - 1 else ''
        next_indent = '{0}{1}{2}'.format(indent, ' ' if 'down' in last else '│', " " * len(current_node.__repr__()))
        print_tree(child, indent=next_indent, last=next_last)


dic_tokens = { ID: 'ID', MAIN: 'MAIN',INT: 'INT',FLOAT: 'FLOAT',IF: 'IF',ELSE: 'ELSE',WHILE: 'WHILE',READ: 'READ',PRINT: 'PRINT', LBRACKET: 'LBRACKET' ,RBRACKET: 'RBRACKET',LBRACE: 'LBRACE',RBRACE: 'RBRACE',COMMA: 'COMMA',PCOMMA: 'PCOMMA',ATTR: 'ATTR',LT: 'LT',LE: 'LE',GT: 'GT',GE: 'GE',EQ: 'EQ',NE: 'NE',OR: 'OR',AND: 'AND',PLUS: 'PLUS',MINUS: 'MINUS',MULT: 'MULT',DIV: 'DIV', INTEGER_CONST: 'INTEGER_CONST', FLOAT_CONST: 'FLOAT_CONST'}


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

# tabSimbolos = SymbolTable()

def match(tok):
    global token, i
    if(token.type == tok):
        #print('Token ' + repr(token) + ' reconhecido na entrada.')
        i = i + 1
        if (i < len(vetorTokens)):
            token = vetorTokens[i]
    else:
        print('Erro sintático. Token ' + repr(token) + ' não esperado na entrada.')
        i = i - 1
        token = vetorTokens[i]
        print('Tokens ' + str(Follow[token.type]) + ' esperados na entrada.')
        i = i + 1
        token = vetorTokens[i]
        #sincroniza(tok)

def TabelaSimbolos():
    print("Tabela de simbolos")
    lista_tabelaSimbolos = {}

    for it in range(0,len(vetorTokens)): 
        if(vetorTokens[it].type == INTEGER_CONST or vetorTokens[it].type == FLOAT_CONST):
            vetorTokens[it].value = vetorTokens[it].lexema
        if(vetorTokens[it].type == ID and (vetorTokens[it-1].type == INT or vetorTokens[it-1].type == FLOAT)):
            lista_tabelaSimbolos[vetorTokens[it].lexema] = dic_tokens[vetorTokens[it-1].type],vetorTokens[it].value
            # print(vetorTokens[it])

    for it in range(0,len(vetorTokens)): 
        if(vetorTokens[it].type == ATTR and vetorTokens[it-1].type == ID):
            vetorTokens[it-1].value = vetorTokens[it+1].value
           
    print(lista_tabelaSimbolos)


def Programa(lista_tokens):
    print("\nAnalisador Sintatico CSmall")
    global token,  currentType,  currentToken
    for a in lista_tokens:
        # print (a)
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
    print('Fim da análise sintática.\n')
    return ast

def Decl_Comando(no):
    print('Decl_Comando recebeu:\n ' + str(no))
    global token,  currentType,  currentToken
    # print("!!!!!token!!!!!",token)
    # bla = input('Digite para continuar')
    if (token.type == INT or token.type == FLOAT):
        no1 = Declaracao(no)
        print('Declaracao retornou:\n ' + str(no))
        return Decl_Comando(no1)
    elif (token.type == ID or token.type == IF or token.type == WHILE or token.type == PRINT
          or token.type == READ):
        no1 = Comando(no) #Criamos nós na ast para cada comando encontrado
        print('Comando retornou:\n ' + str(no))
        return Decl_Comando(no1)
    else:
        return no


def Declaracao(no):
    global token,  currentType,  currentToken
    Tipo()  
    if (token.type == ID):
        currentToken = token
        # te = TableEntry(token.lexema, currentType, None, None)
        # currentTableEntry = te
        # tabSimbolos.insertEntry(token.lexema, te)
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
    global token,  currentType,  currentToken
    # print("!!!!!decl2!!!!!",token.lexema)
    # bla = input('Digite para continuar')
    if (token.type == COMMA):
        match(COMMA)
        if (token.type == ID):
            # te = TableEntry(token.lexema, currentType, None, None)
            # currentTableEntry = te
            # tabSimbolos.insertEntry(token.lexema, te)
            match(ID) #cria uma entrada na tabela de símbolos para esse identificador
            return Decl2(no)
    elif (token.type == PCOMMA):
        match(PCOMMA)
        return no
    elif (token.type == ATTR):
        match(ATTR)
        id_node = Id(token)
        expr_node = E()
        attr_node = Attr(id_node, '=', expr_node)
        no.children.append(attr_node)
        return Decl2(no)
    return no

def Comando(no):
    global token,  currentType,  currentToken
    if (token.type == ID): #nesse momento, podemos buscar informações sobre esse Id na tabela de símbolos
        print('Procurando lexema ' + token.lexema)
        # te = tabSimbolos.getEntry(token.lexema)
        id_node = None
        # if (te):
        #     print('Encontrado o lexema na tabela de símbolos.')
        #     print('Tipo do identificador: ' + str(typeNames[te.tipo]))
        #     print('Valor do identificador: ' + str(te.ref_valor))
        #     id_node = Id(te) #Cria o nó Id passando uma referência para a entrada da tabela de símbolos desse identificador
        id_node = Id(token)
        match(ID)
        match(ATTR)
        expr_node = E()
        attr_node = Attr(id_node, '=', expr_node)
        match(PCOMMA)
        no.children.append(attr_node)
        return no

    elif (token.type == IF):
        match(IF)
        match(LBRACKET)
        expr_node = E()
        match(RBRACKET)
        if_node = If(expr_node, None, None)
        Comando(if_node) 
        if(token.type == ELSE):
            match(ELSE)
            Comando(if_node) 
        no.children.append(if_node)
        
    return no

def E():
    global token,  currentType,  currentToken
    no_ope1 = T()
    return E_(no_ope1)

def E_(no_ope1):
    global token,  currentType,  currentToken
    if(token.type == PLUS):
        match(PLUS)
        no_ope2 = T()
        no = ArithOp('+', no_ope1, no_ope2)
        return E_(no)
    elif (token.type == MINUS):
        match(MINUS)
        no_ope2 = T()
        no = ArithOp('-', no_ope1, no_ope2)
        return E_(no)
    return no_ope1

def T():
    global token,  currentType,  currentToken
    no_ope1 = F()
    return T_(no_ope1)

def T_(no_ope1):
    global token,  currentType,  currentToken
    if (token.type == MULT):
        match(MULT)
        no_ope2 = F()
        no = ArithOp('*', no_ope1, no_ope2)
        return T_(no)
    elif(token.type == DIV):
        match(DIV)
        no_ope2 = F()
        no = ArithOp('/', no_ope1, no_ope2)
        return T_(no)
    return no_ope1

def F():
    global token,  currentType,  currentToken
    if(token.type == LBRACKET):
        match(LBRACKET)
        expr = E()
        match(RBRACKET)
        return expr
    elif (token.type == ID):
        # te = tabSimbolos.getEntry(token.lexema)
        id_node =  Id(token)
        # if (te):
        #     print('Encontrado o lexema na tabela de símbolos.')
        #     print('Tipo do identificador: ' + str(typeNames[te.tipo]))
        #     id_node = Id(te)
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
