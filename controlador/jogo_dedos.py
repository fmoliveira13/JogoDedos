#!/usr/bin/env python
# -*- coding: utf-8 -*-

from controlador.estado import Estado
from jogadores.humano_j import Humano
from jogadores.minimax import Minimax
import glob
import os
import re

class JogoDedos:

    def __init__(self, jogador, adversario, rodadas, partidas=1, acompanhar_jogadas=True):
        self.red = jogador
        self.blue = adversario
        self.rodadas = rodadas
        self.partidas = partidas
        self.acompanhar_jogadas = acompanhar_jogadas

    def iniciar(self):
        resultados = []
        estados = []
        for partida in range(self.partidas):
            resultado, estado = self.jogo(Estado(self.red, self.blue))
            resultados.append(resultado)
            estados.append(estado)
        return estados, *self.computar_resultados(resultados)

    def computar_resultados(self, resultados):
        partidas = len(resultados)
        vitorias = resultados.count(self.red.cor)
        empates = resultados.count(0)
        derrotas = resultados.count(self.blue.cor)
        p_vitorias = round(vitorias/partidas*100,2)
        p_derrotas = round(derrotas/partidas*100,2)
        p_empates = round(empates/partidas*100,2)
        return vitorias, p_vitorias, derrotas, p_derrotas, empates, p_empates

    def jogo(self, estado):

        rodadas = self.rodadas * 2
        # explorados = []

        rodada = 1
        while rodada <= rodadas:

            jogador, adversario = estado.jogadores
            if estado.terminal():
                return estado.adversario.cor, estado

            # if estado in explorados:
            #     if explorados.count(estado) == 3:
            #         return 0, estado

            if self.acompanhar_jogadas:
                print(estado, '\n')

            # explorados.append(estado)
            movimentos = jogador.jogar(estado)
            estado.adiciona_sucessores(movimentos)
            estado = estado.sucessores[0]
            rodada += 1

        return 0, estado

    def selecionar_jogador(cor):
        jogadores = glob.glob(os.path.dirname(__file__)+r'\..\jogadores\*_j.py')
        nome_cor = '[RED]' if cor == 1 else '[BLUE]'

        while True:
            print ('Selecione um dos jogadores abaixo para ser ' + nome_cor)
            for i, jogador in enumerate(jogadores):
                jogador = re.findall('(\w*)_j.py$',jogador)[0]
                print(i.__str__() + " - " + jogador)

            jogador = input("\nDigite o numero do jogador: ")
            module_globals = {}

            try:
                if int(jogador) not in range(len(jogadores)):
                    print('\nOpção inválida!\n')
                    continue
            except:
                print('\nOpção inválida!\n')
                continue

            print()
            exec(open(jogadores[int(jogador)]).read(), module_globals)
            return module_globals[[a for a in module_globals.keys()][len(module_globals.keys()) - 1]](cor=cor)
