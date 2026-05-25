keywords = ('for', 'if', 'else', 'in', ':')

FOR, IF, ELSE, IN, COLON = keywords

INDENT = "    "

lines = [
    (0, FOR + " each token " + IN + " the postfix expression " + COLON),
    (1, IF + " the token is a number " + COLON),
    (2, "print('Convert it to an integer and add it to the end of values')"),
    (1, ELSE),
    (2, "print('Append the result to the end of values')"),
]

for level, text in lines:
    print(INDENT * level + text)
