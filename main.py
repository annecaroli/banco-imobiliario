"""
Desafio Keeggo
Anne Caroline Silva
2021-08-17

"""

import lib
import impulsivo
import exigente
import cauteloso
import aleatorio
import random


def main():

    # cria tabuleiro
    lst_board = lib.build_board()

    # cria jogadores
    lst_player = [
        impulsivo.Impulsivo(),
        exigente.Exigente(),
        cauteloso.Cauteloso(),
        aleatorio.Aleatorio()
    ]
    random.shuffle(lst_player)

    for j in range(0, 1000):
        for jogador in lst_player:

            # joga o dado
            result = lib.play_dice()

            # anda no tabuleiro
            jogador.pos += result

            # verifica se completou tabuleiro
            if jogador.pos >= 20:
                jogador.pos -= 20
                jogador.budget += 100

            pos = jogador.pos - 1

            # toma decisoes
            if lst_board[pos].has_owner:
                # se propriedade possui dono, entao paga aluguel
                ## TODO: fazer metodo receber jogador que paga, jogador que recebe, propriedade
                lib.pay_rent(jogador, lst_board[pos])
            else:
                # se nao possuir dono, entao decide se compra
                if jogador.buy_property(lst_board[pos]):
                    # Subtrai valor de venda no saldo do jogador
                    jogador.budget -= lst_board[pos].c_sale
                    # atrubui propriedade ao jogador
                    lst_board[pos].has_owner = True
                    lst_board[pos].owner = jogador.name
                    jogador.properties.append(lst_board[pos])

            # verifica se tem saldo positivo
            if not jogador.has_budget():
                for item in jogador.properties:
                    item.has_owner = False
                    item.owner = ''

                jogador.properties = []
                lst_player.remove(jogador)

        # verifica se ha apenas 1 jogador
        if lst_player == 1:
            break

    # # elege o ganhador
    # if len(lst_player) == 1:
    #     winner = lst_player[0]
    # else:
    #     winner = lib.tiebreaker(lst_player)

    print("WINNER: ", lst_player)


    """
    n_timeout = 0
    avg_turnos = 0.0
    win_imp = 0.0
    win_exi = 0.0
    win_cau = 0.0
    win_ale = 0.0

    # esquema do programa funcionando

    # 300 - execucoes do jogo
    for i in range(0, 300):
        # 1000 - numero maximo de jogadas
        for j in range(0, 1000):
            # executas jogadas
    """


if __name__ == '__main__':
    main()
