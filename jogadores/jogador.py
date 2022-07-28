#!/usr/bin/env python
# -*- coding: utf-8 -*-

from controlador.validacoes import Avaliador

class Jogador:

    RED, BLUE = +1, -1

    def __init__(self, cor, esq=1, dir=1, nome='Jogador', iteracoes=None):
        self.mao = (esq,dir)
        self.cor = cor
        self.nome = nome
        self.iteracoes = iteracoes
        Avaliador.maos(self.mao)
        Avaliador.cor(self.cor)

    def __eq__(self, jogador):
        return (self.mao == jogador.mao or self.mao == jogador.mao[::-1]) and self.cor == jogador.cor

    def __str__(self):
        cor = 'RED' if self.cor == Jogador.RED else 'BLUE'
        return f'{self.nome} [{cor}]'

    def __format__(self, format_spec):
        return format(str(self), format_spec)

    def exibe_cor(self):
        cor = 'RED' if self.cor == Jogador.RED else 'BLUE'
        return f'{cor}'
