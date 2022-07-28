#!/usr/bin/env python
# -*- coding: utf-8 -*-

from controlador.estado import Estado
from controlador.movimentos import Movimentos
from jogadores.jogador import Jogador

class Humano(Jogador):

    def __init__(self, cor, esq=1, dir=1, nome='Humano', iteracoes=None):
        super().__init__(cor,esq,dir,nome)

    def converte_jogada(self, jogada):
        movimento = []
        for mao in jogada:
            if mao == 1:
                movimento.append(0)
            elif mao == 2:
                movimento.append(1)
            else:
                movimento.append(-1)
        return tuple(movimento)

    def jogar(self, estado: Estado):

        jogador, adversario = estado.jogadores

        while True:
            try:
                print('Controle: 1 para esquerda | 2 para direita | 3 para dividir')
                v = input('Escolha sua mao de jogada: ')
                x = int(v)
                y = -1
                movimento = (x,y)
                if x != 3:
                    v = input('Escolha a mao do adversario: ')
                    y = int(v)
                    movimento = self.converte_jogada([x,y])
                print()

            except ValueError:
                print(f'Jogada "{v}" invalido!\n')
                print(estado,'\n')
                continue

            if x == 3:
                if Movimentos.dividir_valido(jogador):
                    return [True]
                print('Nao eh possivel dividir a mao!\n')
                print(estado,'\n')
                continue

            if not Movimentos.valido(movimento):
                print(f'Jogada {(x,y)} invalida!\n')
                print(estado,'\n')
                continue

            if movimento not in Movimentos.disponiveis(jogador, adversario):
                print(f'Nao eh possivel realizar a jogada {(x,y)}!\n')
                print(estado,'\n')
                continue

            return [movimento]
