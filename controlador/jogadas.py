#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jogadores.jogador import Jogador

class Jogadas:

    def novas_maos_adversario(jogador: Jogador, adversario: Jogador, movimentos):

        #funcao de conferencia
        ja_adicionada = lambda x: tuple(x) in novas_maos \
                        or tuple(x[::-1]) in novas_maos

        novas_maos = []
        movimentos_realizados = []
        for movimento in movimentos:
            copia_adversario = list(adversario.mao)
            i,j = movimento
            nova_mao = (jogador.mao[i] + adversario.mao[j]) % 5
            copia_adversario[j] = nova_mao

            #adiciona se mao eh nova
            if not ja_adicionada(copia_adversario):
                novas_maos.append(tuple(copia_adversario))
                movimentos_realizados.append(movimento)

        return novas_maos, movimentos_realizados

    def dividir_mao(jogador: Jogador):
        i,j = jogador.mao
        k = (i+j)//2
        return (k,k)