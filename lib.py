import property
import players
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


def pay_rent(player, prop):
    player.budget -= prop.c_rent

    owner = prop.owner

    ##TODO: melhorar essa parte
    owner.budget += prop.c_rent


def tiebreaker(lst_players):
    return max(lst_players.budget, key=int)
