from random import choice

def randomCap(sentence):
    #sentence = ('Det er sådan her du lyder')
    print(''.join(choice((str.upper, str.lower))(c) for c in sentence))


if __name__ == '__main__':
    randomCap()
