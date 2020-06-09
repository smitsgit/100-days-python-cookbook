import re
from dataclasses import dataclass

NAME = r"(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)"
NUM = r"(?P<NUM>\d+)"
WS = r"(?P<WS>\s+)"
EQ = R"(?P<EQ>=)"

master_re = re.compile('|'.join([NAME, NUM, WS, EQ]))


@dataclass
class Token:
    type: str
    value: str


def generate_tokens(master_pat, text):
    scanner = master_pat.scanner(text)
    for match in iter(scanner.match, None):
        yield Token(match.lastgroup, match.group())


def main():
    for token in generate_tokens(master_re, 'foo = 42'):
        print(token)


if __name__ == '__main__':
    main()