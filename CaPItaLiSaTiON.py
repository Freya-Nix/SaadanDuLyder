from random import choice

sentence = ('Det er sådan her du lyder')
print(''.join(choice((str.upper, str.lower))(c) for c in sentence))
