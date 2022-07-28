#!/usr/bin/env python
# -*- coding: utf-8 -*-

from controlador.estado import Estado
from controlador.movimentos import Movimentos
from jogadores.jogador import Jogador
import random

class AleatorioAtaque(Jogador):

    def __init__(self, cor, esq=1, dir=1, nome='AleatorioAtaque', iteracoes=None):
        super().__init__(cor, esq, dir, nome)
    
    def jogar(self, estado: Estado):
        return self.estrategia(estado())

    def estrategia(self, estado: Estado):

        jogador, adversario = estado.jogadores
        movimentos_disponiveis = Movimentos.disponiveis(jogador, adversario)
        movimentos_realizados = estado.adiciona_sucessores(movimentos_disponiveis)


        zeros_atual = estado.conta_zeros()
        for novo_estado, movimento in zip(estado.sucessores, movimentos_realizados):
            zeros = novo_estado.conta_zeros()
            if zeros > zeros_atual:
                return [movimento]
        
        # random.seed(127)
        movimento = random.choice(movimentos_realizados)
        return [movimento]
