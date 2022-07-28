#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jogadores.jogador import Jogador

class Movimentos:
    
    esq_esq, esq_dir, dir_esq, dir_dir = (0,0), (0,1), (1,0), (1,1)
    possiveis = (esq_esq, esq_dir, dir_esq, dir_dir)

    def disponiveis(jogador: Jogador, adversario: Jogador):

        i,j = jogador.mao
        m,n = adversario.mao

        movimentos_disponiveis = []

        #verifica se pode dividir a mao
        if Movimentos.dividir_valido(jogador):
            movimentos_disponiveis.append(True)

        #se maos do jogador eh diferente de zero
        if 0 not in jogador.mao:
            movimentos = Movimentos.possiveis
            if m > 0:
                movimentos_disponiveis.append(movimentos[0])
                movimentos_disponiveis.append(movimentos[2])
            if n > 0:
                movimentos_disponiveis.append(movimentos[1])
                movimentos_disponiveis.append(movimentos[3])
            return movimentos_disponiveis

        #se mao esquerda do jogador atual é zero
        if i == 0:
            movimentos = Movimentos.possiveis[2:]
            if m > 0:
                movimentos_disponiveis.append(movimentos[0])
            if n > 0:
                movimentos_disponiveis.append(movimentos[1])
            return movimentos_disponiveis

        #se mao direita do jogador atual é zero
        if j == 0:
            movimentos = Movimentos.possiveis[:2]
            if m > 0:
                movimentos_disponiveis.append(movimentos[0])
            if n > 0:
                movimentos_disponiveis.append(movimentos[1])
            return movimentos_disponiveis
    
    def valido(movimento):
        return movimento in Movimentos.possiveis

    def dividir_valido(jogador):
        if 0 in jogador.mao:
            i, j = jogador.mao
            return (i+j)%2 == 0
        return False