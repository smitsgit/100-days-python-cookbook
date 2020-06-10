from sly import Lexer, Parser


class CalcLexer(Lexer):
    # Set of token names.   This is always required
    tokens = {NUMBER, ID, WHILE, IF, ELSE, PRINT, LET, RETURN,SET,
              PLUS, MINUS, TIMES, DIVIDE, ASSIGN,
              EQ, LT, LE, GT, GE, NE, LPAREN, RPAREN}

    literals = {'(', ')', '{', '}', ';'}

    # String containing ignored characters
    ignore = ' \t'

    # Regular expression rules for tokens
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    EQ = r'=='
    ASSIGN = r'='
    LE = r'<='
    LT = r'<'
    GE = r'>='
    GT = r'>'
    NE = r'!='

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    # Identifiers and keywords
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['if'] = IF
    ID['else'] = ELSE
    ID['while'] = WHILE
    ID['print'] = PRINT
    ID['let'] = LET
    ID['return'] = RETURN
    ID['set'] = SET

    ignore_comment = r'\#.*'

    # Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1


class Expr:
    pass


class BinOp(Expr):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right


class Number(Expr):
    def __init__(self, value):
        self.value = value


class LetStatement(Expr):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f'LET {self.name} = {self.value}'

    def __repr__(self):
        return f'LET {self.name} = {self.value}'

class ReturnStatement(Expr):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'RETURN {self.value}'

    def __repr__(self):
        return f'RETURN {self.value}'


class CalcParser(Parser):
    # Get the token list from the lexer (required)
    tokens = CalcLexer.tokens
    literals = CalcLexer.literals


    @_('statements statement')
    def statements(self, p):
        return p.statements + [ p.statement ]

    @_('statement')
    def statements(self, p):
        return [ p.statement ]

    @_('LET ID ASSIGN expr')
    def statement(self, p):
        return LetStatement(name=p.ID, value=p.expr)

    @_('RETURN expr')
    def statement(self, p):
        return ReturnStatement(p.expr)

    # Grammar rules and actions
    @_('expr PLUS term')
    def expr(self, p):
        return p.expr + p.term

    @_('expr MINUS term')
    def expr(self, p):
        return p.expr - p.term

    @_('term')
    def expr(self, p):
        return p.term

    @_('term TIMES factor')
    def term(self, p):
        return p.term * p.factor

    @_('term DIVIDE factor')
    def term(self, p):
        return p.term / p.factor

    @_('factor')
    def term(self, p):
        return p.factor

    @_('NUMBER')
    def factor(self, p):
        return p.NUMBER

    @_('"(" expr ")"')
    def factor(self, p):
        return p.expr


if __name__ == '__main__':
    data = "let x = 10\n let y = 10"

    lexer = CalcLexer()
    parser = CalcParser()

    # while True:
    #     try:
    #         text = input('calc > ')
    #         result = parser.parse(lexer.tokenize(text))
    #         print(result)
    #     except EOFError:
    #         break

    lexer = CalcLexer()
    for tok in lexer.tokenize(data):
        print(tok)

    result = parser.parse(lexer.tokenize(data))
    print(result)
