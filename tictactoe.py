a1 = '-'
a2 = '-'
a3 = '-'
b1 = '-'
b2 = '-'
b3 = '-'
c1 = '-'
c2 = '-'
c3 = '-'

vitoria = False
simbolo = int(input('escolha um simbolo [X - 1] ou [O - 2]: '))
if simbolo in range(1, 3):
    if simbolo == 1:
        simbolo = 'X'
    if simbolo == 2:
        simbolo = 'O'
print(f'        1 |  2  |  3  ')
print(f'      ----+-----+-----')
print(f'       4  |  5  |  6  ')
print(f'      ----+-----+-----')
print(f'       7  |  8  |  9  ')

posicao = int(input('Digite sua jogada (1 - 9): '))
if posicao in range(1, 10):
    if (posicao == 1) and (a1 == '-'):
        a1 = simbolo
    if (posicao == 2) and (a2 == '-'):
        a2 = simbolo
    if (posicao == 3) and (a3 == '-'):
        a3 = simbolo
    if (posicao == 4) and (b1 == '-'):
        b1 = simbolo
    if (posicao == 5) and (b2 == '-'):
        b2 = simbolo
    if (posicao == 6) and (b3 == '-'):
        b3 = simbolo
    if (posicao == 7) and (c1 == '-'):
        c1 = simbolo
    if (posicao == 8) and (c2 == '-'):
        c2 = simbolo
    if (posicao == 9) and (c3 == '-'):
        c3 = simbolo

while (vitoria != True):
    simbolo = int(input('escolha um simbolo [X - 1] ou [O - 2]: '))
    if simbolo in range (1, 3):
        if simbolo == 1:
            simbolo = 'X'
        if simbolo == 2:
            simbolo = 'O'
        if posicao != 0:
            print(f'        {a1} |  {a2}  |  {a3}  ')
            print(f'      ----+-----+-----')
            print(f'       {b1}  |  {b2}  |  {b3}  ')
            print(f'      ----+-----+-----')
            print(f'       {c1}  |  {c2}  |  {c3}  ')

        posicao = int(input('Digite sua jogada (1 - 9): '))

        if posicao in range (1, 10):
            if (posicao == 1) and (a1 == '-'):
                a1 = simbolo
            if (posicao == 2) and (a2 == '-'):
                a2 = simbolo
            if (posicao == 3) and (a3 == '-'):
                a3 = simbolo
            if (posicao == 4) and (b1 == '-'):
                b1 = simbolo
            if (posicao == 5) and (b2 == '-'):
                b2 = simbolo
            if (posicao == 6) and (b3 == '-'):
                b3 = simbolo
            if (posicao == 7) and (c1 == '-'):
                c1 = simbolo
            if (posicao == 8) and (c2 == '-'):
                c2 = simbolo
            if (posicao == 9) and (c3 == '-'):
                c3 = simbolo

            if (a1 == a2) and (a1 == a3) and (a1 != '-'):
                vitoria = True
                print(f'        {a1} |  {a2}  |  {a3}  ')
                print(f'      ----+-----+-----')
                print(f'       {b1}  |  {b2}  |  {b3}  ')
                print(f'      ----+-----+-----')
                print(f'       {c1}  |  {c2}  |  {c3}  ')

                print(f'{a1} ganhou.')
            if (a1 == b2) and (a1 == c3) and (a1 != '-'):
                print(f'{a1} ganhou')
                vitoria = True
                print(f'        {a1} |  {a2}  |  {a3}  ')
                print(f'      ----+-----+-----')
                print(f'       {b1}  |  {b2}  |  {b3}  ')
                print(f'      ----+-----+-----')
                print(f'       {c1}  |  {c2}  |  {c3}  ')

            if (a1 == b1) and (a1 == c1) and (a1 != '-'):
                print(f'{a1} ganhou')
                vitoria = True
                print(f'        {a1} |  {a2}  |  {a3}  ')
                print(f'      ----+-----+-----')
                print(f'       {b1}  |  {b2}  |  {b3}  ')
                print(f'      ----+-----+-----')
                print(f'       {c1}  |  {c2}  |  {c3}  ')

            if (b1 == b2) and (b1 == b3) and (b1 != '-'):
                print(f'{b1} ganhou')
                vitoria = True
                print(f'        {a1} |  {a2}  |  {a3}  ')
                print(f'      ----+-----+-----')
                print(f'       {b1}  |  {b2}  |  {b3}  ')
                print(f'      ----+-----+-----')
                print(f'       {c1}  |  {c2}  |  {c3}  ')

            if (c1 == c2) and (c1 == c3) and (c1 != '-'):
                print(f'{c1} ganhou')
                vitoria = True
                print(f'        {a1} |  {a2}  |  {a3}  ')
                print(f'      ----+-----+-----')
                print(f'       {b1}  |  {b2}  |  {b3}  ')
                print(f'      ----+-----+-----')
                print(f'       {c1}  |  {c2}  |  {c3}  ')

            if (a3 == b3) and (a3 == c3) and (a3 != '-'):
                print(f'{a3} ganhou')
                vitoria = True
                print(f'        {a1} |  {a2}  |  {a3}  ')
                print(f'      ----+-----+-----')
                print(f'       {b1}  |  {b2}  |  {b3}  ')
                print(f'      ----+-----+-----')
                print(f'       {c1}  |  {c2}  |  {c3}  ')

            if (a2 == b2) and (a2 == c2) and (a2 != '-'):
                print(f'{a2} ganhou')
                vitoria = True
                print(f'        {a1} |  {a2}  |  {a3}  ')
                print(f'      ----+-----+-----')
                print(f'       {b1}  |  {b2}  |  {b3}  ')
                print(f'      ----+-----+-----')
                print(f'       {c1}  |  {c2}  |  {c3}  ')

        else:
            print('posição inválida.')
    else:
        print('Simbolo inválido.')

print('so um teste de git')