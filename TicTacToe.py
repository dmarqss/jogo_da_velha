from random import randint
import time

tab = [0, 1, 2, 3, 4, 5, 6, 7, 8]
tabf = [0, 1, 2, 3, 4, 5, 6, 7, 8]
sele = []
stop = False
op = False
pturn = True

def verificar():
    global stop
    if tab[0] == 'X' and tab[1] == 'X' and tab[2] == 'X':
        stop = True
        print('PARABENS VC \033[0;32mGANHOU\033[0;0m')
    if tab[0] == 'O' and tab[1] == 'O' and tab[2] == 'O':
        stop = True
        print('VC \033[1;31mPERDEU\033[0;0m O,COMPUTADOR GANHOU')
    if tab[3] == 'X' and tab[4] == 'X' and tab[5] == 'X':
        stop = True
        print('PARABENS VC "\033[0;32mGANHOU\033[0;0m"')
    if tab[3] == 'O' and tab[4] == 'O' and tab[5] == 'O':
        stop = True
        print('VC \033[1;31mPERDEU\033[0;0m O,COMPUTADOR GANHuOU')
    if tab[6] == 'X' and tab[7] == 'X' and tab[8] == 'X':
        stop = True
        print('PARABENS VC \033[0;32mGANHOU\033[0;0m')
    if tab[6] == 'O' and tab[7] == 'O' and tab[8] == 'O':
        stop = True
        print('VC \033[1;31mPERDEU\033[0;0m O,COMPUTADOR GANHOU')
    if tab[0] == 'X' and tab[3] == 'X' and tab[6] == 'X':
        stop = True
        print('PARABENS VC \033[0;32mGANHOU\033[0;0m')
    if tab[0] == 'O' and tab[3] == 'O' and tab[6] == 'O':
        stop = True
        print('VC \033[1;31mPERDEU\033[0;0m O,COMPUTADOR GANHOU')
    if tab[1] == 'X' and tab[4] == 'X' and tab[7] == 'X':
        stop = True
        print('PARABENS VC \033[0;32mGANHOU\033[0;0m')
    if tab[1] == 'O' and tab[4] == 'O' and tab[7] == 'O':
        stop = True
        print('VC \033[1;31mPERDEU\033[0;0m O,COMPUTADOR GANHOU')
    if tab[2] == 'X' and tab[5] == 'X' and tab[8] == 'X':
        stop = True
        print('PARABENS VC \033[0;32mGANHOU\033[0;0m')
    if tab[2] == 'O' and tab[5] == 'O' and tab[8] == 'O':
        stop = True
        print('VC \033[1;31mPERDEU\033[0;0m O,COMPUTADOR GANHOU')
    if tab[0] == 'X' and tab[4] == 'X' and tab[8] == 'X':
        stop = True
        print('PARABENS VC \033[0;32mGANHOU\033[0;0m')
    if tab[0] == 'O' and tab[4] == 'O' and tab[8] == 'O':
        stop = True
        print('VC \033[1;31mPERDEU\033[0;0m O,COMPUTADOR GANHOU')
    if tab[2] == 'X' and tab[4] == 'X' and tab[6] == 'X':
        stop = True
        print('PARABENS VC \033[0;32mGANHOU\033[0;0m')
    if tab[2] == 'O' and tab[4] == 'O' and tab[6] == 'O':
        stop = True
        print('VC \033[1;31mPERDEU\033[0;0m O COMPUTADOR GANHOU')
    if len(sele) == 9:
        stop = True
        print('O JOGO \033[1;34mEMPATOU\033[0;0m')

def inicio():
    print('       JOGO DA VELHA')

def tabuleiro():
    print(tabf[0], "|", tabf[1], '|', tabf[2])
    print(tabf[3], "|", tabf[4], '|', tabf[5])
    print(tabf[6], "|", tabf[7], '|', tabf[8])


inicio()
while stop == False:
    if pturn == True:
        tabuleiro()
        print('=-=-=-=-=-=-=')
        print('VEZ DO PLAYER')
        player = int(input(''))
        if player >= 0 and player <= 8 and not player in sele:
            tabf[player] = ('\033[1;34mX\033[m')
            tab[player] = 'X'
            sele.append(player)
            pturn = False
            verificar()
            print('=-=-=-=-=-=-=-=-=')
        else:
            print('ESSE NUMERO JA FOI ESCOLHIDO')
            break
    else:
        pc = randint(0, 8)
        while pc in sele:
            pc = randint(0, 8)
        else:
            print('VEZ DO COMPUTADOR')
            time.sleep(0.5)
            tabf[pc] = ('\033[1;34mO\033[m')
            tab[pc] = 'O'
            sele.append(pc)
            pturn = True
            verificar()
tabuleiro()
