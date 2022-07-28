#!/usr/bin/env python
# -*- coding: utf-8 -*-

from controlador.estado import Estado
from controlador.movimentos import Movimentos
from jogadores.minimax import Minimax

class MinimaxSemPoda(Minimax):

    def __init__(self, cor, esq=1, dir=1, nome='MinimaxSemPoda', iteracoes=2):
        super().__init__(cor,esq,dir,nome,iteracoes)

    def estrategia(self, estado: Estado, iteracoes, funcao_utilidade, cut=None):

        (melhor_pontuacao, melhor_jogada) = (None, None)

        if estado.terminal() or iteracoes == 0:
            (melhor_pontuacao, melhor_jogada) = (funcao_utilidade(estado), None)
            return (melhor_pontuacao, melhor_jogada)

        # cria uma lista com todos os movimentos possiveis a partir do estado atual do jogo e retorna o de maior heuristica
        jogador, adversario = estado.jogadores
        movimentos_disponiveis = Movimentos.disponiveis(jogador, adversario)
        movimentos_realizados = estado.adiciona_sucessores(movimentos_disponiveis)
        melhor_pontuacao = None
        melhor_jogada = None

        for novo_estado, movimento in zip(estado.sucessores, movimentos_realizados):
            # breakpoint()
            if melhor_pontuacao is None:
                nova_pontuacao = self.estrategia(novo_estado, iteracoes-1, funcao_utilidade)[0]
            else:
                nova_pontuacao = self.estrategia(novo_estado, iteracoes-1, funcao_utilidade, melhor_pontuacao)[0]
            if nova_pontuacao is None:
                continue

            if self.eh_max(jogador):
                if melhor_pontuacao is None or melhor_pontuacao < nova_pontuacao:
                    melhor_pontuacao = nova_pontuacao
                    melhor_jogada = movimento
            else:
                nova_pontuacao *= -1
                if melhor_pontuacao is None or melhor_pontuacao > nova_pontuacao:
                    melhor_pontuacao = nova_pontuacao
                    melhor_jogada = movimento

        # pega a jogada de valor maximo e retorna isso
        return (melhor_pontuacao, [melhor_jogada])
        # pontos_estado_atual = funcao_utilidade(estado)
        # if self.eh_max(jogador): pontos_estado_atual *= -1
        # return (melhor_pontuacao+pontos_estado_atual, [melhor_jogada])
