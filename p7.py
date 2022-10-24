import os
from os import system
system('clear')

import random


pw = 0
cw = 0
coin = 100
q = 'y'

def ran():
    r = random.randint(1,10)
    return r

def player(q):
    pn = 0
    cn = 0
    while q == 'y':
        system('clear')
        r = ran()
        pn += r
        if cn < 16 :
            rc = ran()
            cn += rc
        print(f"You got {r} nad your total is {pn}. The computer got {rc} and its total is {cn}.")
        if (pn > 20) or cn > 20:
            break
        q = input("Do you want to draw another card?(Press 'y' if yes): ")
        
        if q != 'y':
            while cn < 16:
                cn += ran()
    system('clear')
    return pn, cn

def play():
    g = player(q)
    print(f"Your total is {g[0]}, and the computer's total is {g[1]}.")
    if g[0] > 20 and g[1] > 20:
        print('You both went over 20.')
    elif g[1] > 20:
        print("The computer went over 20 and you won!")
        return 2
    elif g[0] > 20:
        print('You went over 20 and the computer won.')
        return 4
    elif g[0] == g[1]:
        print("You both tied!")
        return 1
    elif g[0] < g[1]:
        print('You lost by having a lower number than the computer.')
        return 4
    elif g[0] > g[1]:
        print('You won by having a higher number than the computer!')
        if g[0] == 20:
            return 3
        else :
            return 2

def point(c,p):
    print(f"The score is Player: {p}, Computer: {c}")
    if c == p:
        print(f'You and the computer tied.')
    elif c > p:
        print(f'You lost to the computer.')
    elif c < p:
        print(f'You won against the computer!')

def end(g,ca,p,c,cb):
    if g == 1:
        cb += ca
    elif g == 2:
        cb += ca * 2
        p += 1
    elif g == 3: 
        cb += ca * 3
        p += 1
    elif g == 4:
        c += 1
    return cb, p, c

def spend(coin):
    a = input('How many coins would you like to use?: ')
    while (a.isdigit() == False) or (int(a) == 0) or (int(a) > coin):
        system('clear')
        if a.isdigit() == False:
            print(f'This is not a number. Please try again. You have {coin} coins left.')
        elif int(a) == 0:
            print(f"You can't put 0 coins in. Please try again. You have {coin} coins left.")
        elif int(a) > coin:
            print(f'You dont have that much coins. Please try again. You have {coin} coins left.')
        a = input('How many coins would you like to use?: ')
    coin -= int(a)
    return coin, int(a)

def game(coin,c,p,q):
    while q == 'y':
        if coin > 0:
            print(f'You have {coin} coins left.')
            coin = spend(coin)
            game = play()
            e = end(game, coin[1], p, c, coin[0])
            coin = e[0]
            p = e[1]
            c = e[2]
            print(f'You have {coin} coins.')
        elif coin == 0:
            # system('clear')
            print('You ran out of coins.')
            break
        q = input('Press y to continue playing, if not then press any value. ')
        system('clear')
    point(c, p)
    # print(f'Your coin amount is {a}.')
    
def run():
    game(coin, cw, pw, q)
    print('Thank you for playing!')

run()
