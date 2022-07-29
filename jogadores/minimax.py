#!/usr/bin/env python
# -*- coding: utf-8 -*-

from controlador.estado import Estado
from controlador.movimentos import Movimentos
from jogadores.jogador import Jogador
from abc import abstractmethod

class Minimax(Jogador):

    MIN, MAX = -1, +1

    def __init__(self, cor, esq=1, dir=1, nome='Minimax', iteracoes=2):
        super().__init__(cor,esq,dir,nome)
        self.min_max = Minimax.MAX
        self.iteracoes = iteracoes

    def define_iteracoes(self):
        while True:
            try:
                i = input(f'Digite o numero do nivel de busca do {self} (min: 1 | max: 10): ')
                i = int(i)
            except ValueError:
                print(f'Valor "{i}" invalido!\n')
                continue

            if i in range(1, 10+1):
                print()
                break
            else:
                print('Valor invalido! Digite um numero no intervalo informado\n')
        self.iteracoes = i

    def jogar(self, estado: Estado):
        return self.estrategia(estado(), self.iteracoes, self.funcao_utilidade)[1]

    def funcao_utilidade(self, estado: Estado):
        jogador, adversario = estado.jogadores
        soma_mao_jogador = jogador.mao[0] + jogador.mao[1]
        soma_mao_adversario = adversario.mao[0] + adversario.mao[1]
        bonus1 = 10 if jogador.mao.count(0) == 1 else 0
        bonus2 = 100 if jogador.mao.count(0) == 2 else 0
        return soma_mao_adversario - soma_mao_jogador + bonus1 + bonus2
    

    def eh_max(self, jogador):
        if self.min_max == Minimax.MAX:
            return self.cor == jogador.cor
        else:
            return self.cor != jogador.cor

    @abstractmethod
    def estrategia(self, estado: Estado, iteracoes, funcao_utilidade, cut=None):
        ...
