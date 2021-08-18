import property
import random


def build_board():
    lst_names = ["Forte São João", "Pedra da Cebola", "Itatiaia", "Cléber Andrade", "Mestre Álvaro",
                 "Pituã", "Penedo", "Homero Massena", "Fonte Grande", "Solar Monjardim", "Manguinhos",
                 "Camburi", "Morro do Moreno", "Moxuara", "Vila Rubim", "Praia da Costa", "Anchieta",
                 "Ponta da Sereia", "Jacaraipe", "Moscoso"]
    lst_properties = []
    for i in range(0, 20):
        lst_properties.append(property.Property(lst_names[i]))

    ## teste
    # for i in range(len(lst_properties)):
    #    print(repr(lst_properties[i]))

    return lst_properties


def play_dice():
    return random.randint(1, 6)


def pay_rent(playerA, playerB, prop):
    if playerA.budget < prop.c_rent:
        pay = playerA.budget
    else:
        pay = prop.c_rent

    playerA.budget -= pay
    playerB.budget += pay


def tiebreaker(lst_players):
    winner = None
    maior = 0
    for elem in lst_players:
        if elem.budget > maior:
            maior = elem.budget
            winner = elem

    return winner


def get_player(lst_player, lst_board, pos):
    for elem in lst_player:
        if elem.name == lst_board[pos].owner:
            player = elem

    return player


def avg(lst):
    div = sum(lst) + (1000 * (300 - len(lst)))
    return div / 300


def champion(lst):
    winner = ''
    maior = 0

    for elem in lst:
        if elem[1] > maior:
            maior = elem[1]
            winner = elem

    return winner[0]