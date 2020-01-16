from random import choice

def randomCap(sentence):
    #sentence = ('Det er sådan her du lyder')
    return ''.join(choice((str.upper, str.lower))(c) for c in sentence)


if __name__ == '__main__':
    print(randomCap(input()))
