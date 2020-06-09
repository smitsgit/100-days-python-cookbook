"""
 expr ::= expr + term
          |   expr - term
          | term
term ::= term * factor
         |   term / factor
         | factor
factor ::= ( expr )
        |   NUM

EBNF

expr ::= term { (+|-) term }*
term ::= factor { (*|/) factor }*
factor ::= ( expr )
          |   NUM
"""

import re
import collections

# Token specification
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>-)'
TIMES = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>/)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NUM, PLUS, MINUS, TIMES,
                                  DIVIDE, LPAREN, RPAREN, WS]))

# Tokenizer
Token = collections.namedtuple('Token', ['type', 'value'])


def generate_tokens(text):
    scanner = master_pat.scanner(text)
    for m in iter(scanner.match, None):
        tok = Token(m.lastgroup, m.group())
        if tok.type != 'WS':
            yield tok


class ExpressionEvaluator:

    def parse(self, text):
        self.tokens = generate_tokens(text)
        self.tok = None  # Last symbol consumed
        self.next_tok = None  # Next synbol tokenized
        self._advance()  # Load first look ahead token
        return self.expr()

    def _advance(self):
        self.tok, self.next_tok = self.next_tok, next(self.tokens, None)

    def _expect(self, toktype):
        'Consume next token if it matches toktype or raise syntax error'
        if not self._accept(toktype):
            raise SyntaxError('Expected ' + toktype)

    def _accept(self, toktype):
        'Test and consume the next token if it matches toktype'
        if self.next_tok and self.next_tok.type == toktype:
            self._advance()
            return True
        else:
            return False

    def expr(self):
        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval += right
            elif op == 'MINUS':
                exprval -= right
        return exprval

    def term(self):
        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.term()
            if op == 'TIMES':
                termval *= right
            elif op == 'DIVIDE':
                termval /= right
        return termval

    def factor(self):
        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._expect('RPAREN')
            return exprval
        else:
            raise SyntaxError('Expected Number or LPAREN')


class ExpressionTreeBuileder(ExpressionEvaluator):
    def expr(self):
        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval = ('+', exprval, right)
            elif op == 'MINUS':
                exprval = ('-', exprval, right)
        return exprval

    def term(self):
        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.term()
            if op == 'TIMES':
                termval = ('*', termval, right)
            elif op == 'DIVIDE':
                termval = ('/', termval, right)
        return termval

    def factor(self):
        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._expect('RPAREN')
            return exprval
        else:
            raise SyntaxError('Expected Number or LPAREN')


def main():
    e = ExpressionEvaluator()
    print("Evaluator: ", e.parse("2 + 3 * 5"))

    g = ExpressionTreeBuileder()
    print("Expression Builder: ", g.parse("3 + 4 * 5"))


if __name__ == '__main__':
    main()
