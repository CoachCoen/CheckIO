from itertools import chain

def recall_password(cipher_grille, ciphered_password):
    result = ""
    cipher_grille = list(list(a) for a in cipher_grille)
    cp = ''.join(ciphered_password)
    for _ in range(4):
        # cg = chain(*cipher_grille)
        result += ''.join(a for a, b in zip(cp, chain(*cipher_grille)) if b == 'X')
        cipher_grille.reverse()
        cipher_grille = zip(*cipher_grille)
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
