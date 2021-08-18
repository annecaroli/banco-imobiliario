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
    # variaveis
    qtd_simulacoes = 300
    qtd_partidas = 1000
    qtd_turnos = []
    n_timeout = 0
    win_imp = 0
    win_exi = 0
    win_cau = 0
    win_ale = 0

    for i in range(0, qtd_simulacoes):

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

        for j in range(0, qtd_partidas):
            for jogador in lst_player:
                # joga o dado
                result = lib.play_dice()

                # anda no tabuleiro
                jogador.pos += result

                # verifica se completou tabuleiro
                if jogador.pos > 20:
                    jogador.pos -= 20
                    jogador.budget += 100

                pos = jogador.pos - 1

                # toma decisoes
                if lst_board[pos].has_owner:
                    # se propriedade possui dono, entao paga aluguel
                    jogadorB = lib.get_player(lst_player, lst_board, pos)
                    lib.pay_rent(jogador, jogadorB, lst_board[pos])
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
            if len(lst_player) == 1:
                qtd_turnos.append(j)
                break

        # elege o ganhador
        if len(lst_player) == 1:
            winner = lst_player[0]
        else:
            winner = lib.tiebreaker(lst_player)

        # preenche estatisticas

        if winner.name == "Impulsivo":
            win_imp += 1
        elif winner.name == "Exigente":
            win_exi += 1
        elif winner.name == "Cauteloso":
            win_cau += 1
        elif winner.name == "Aleatorio":
            win_ale += 1

    lst_campeao = [("Impulsivo", win_imp),
                   ("Exigente", win_exi),
                   ("Cauteloso", win_cau),
                   ("Aleatorio", win_ale)]

    # saida
    print("ESTATÍSTICAS DA SIMULAÇÃO\n")
    print("Qtd partidas que acabaram em timeout: ", 300 - len(qtd_turnos))
    print("Média de turnos que uma partida demora: {:.2f}".format(lib.avg(qtd_turnos)))
    print("\nVitórias")
    print("Impulsivo: {:.2f}%".format((win_imp * 100) / 300))
    print("Exigente: {:.2f}%".format((win_exi * 100) / 300))
    print("Cauteloso: {:.2f}%".format((win_cau * 100) / 300))
    print("Aleatorio: {:.2f}%".format((win_ale * 100) / 300))
    print("\nComportamento campeão: ", lib.champion(lst_campeao))


if __name__ == '__main__':
    main()
