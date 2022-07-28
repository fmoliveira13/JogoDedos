#!/usr/bin/env python
# -*- coding: utf-8 -*-

from controlador.jogadas import Jogadas
from controlador.validacoes import Avaliador

class Estado:

    def __init__(self, jogador, adversario, turno=0, antecessor=None):
        self.jogador = jogador
        self.adversario = adversario
        self.jogadores = (jogador, adversario)
        self.turno = turno
        self.sucessores = []
        self.antecessor = antecessor
        Avaliador.jogadores(jogador.cor, adversario.cor)
    
    def __call__(self):
        return Estado(self.jogador, self.adversario, self.turno)

    def terminal(self):
        return self.jogador.mao == (0,0)
    
    def oponente(self, jogador):
        return self.adversario if jogador == self.jogador else self.jogador
    
    # def simula(self, movimento):
    #     jogador, adversario = self.jogadores
    #     nova_mao = Jogadas.novas_maos_adversario(jogador, adversario, [movimento])
    #     adv = adversario.__class__(adversario.cor, *nova_mao[0], adversario.nome)
    #     return Estado(adv, jogador, self.turno+1)
    #
    def conta_zeros(self):
        return self.jogador.mao.count(0) + self.adversario.mao.count(0)

    def adiciona_sucessores(self, movimentos):

        jogador, adversario = self.jogadores

        try:
            dividir = movimentos.pop(movimentos.index(True))
        except:
            dividir = False

        novas_maos_adversario, movimentos_realizados = Jogadas.novas_maos_adversario(jogador, adversario, movimentos)

        for nova_mao in novas_maos_adversario:
            adv = adversario.__class__(adversario.cor, *nova_mao, adversario.nome, adversario.iteracoes)
            proximo_estado = Estado(adv, jogador, self.turno+1, self)
            self.adiciona_sucessor(proximo_estado)

        if dividir:
            nova_mao = Jogadas.dividir_mao(jogador)
            jog = jogador.__class__(jogador.cor, *nova_mao, jogador.nome, jogador.iteracoes)
            proximo_estado = Estado(adversario, jog, self.turno+1, self)
            self.adiciona_sucessor(proximo_estado)
            movimentos_realizados.append(True)

        return movimentos_realizados

    def adiciona_sucessor(self, estado):
        self.sucessores.append(estado)

    def exibir_jogadas(self):
        lst = []
        txt=''
        estado = self
        while estado.antecessor:
            lst.append(estado)
            estado = estado.antecessor
        lst.append(estado)
        
        i=1
        while lst:
            estado = lst.pop()
            turno = estado.turno
            txt += f'{"":-^50}\n' \
            f'{f" Rodada:{i} - Jogador: [{estado.jogador.exibe_cor()}] ":^48}\n' \
            f'{"":-^50}\n\n'

            for jogador in estado.jogadores:
                esq, dir = jogador.mao
                jog = str(jogador) + str(':')
                mao = '|'
                txt += f'{f"{jog:^30} {mao * esq:^5} - {mao * dir:^5}":^38}\n\n'
            i+=1
        return txt

    def __str__(self):
        return  f'Turno {self.turno+1} - Jogador {self.jogador.exibe_cor()}\n' \
                f'{self.jogador:<22} - {self.jogador.mao}\n' \
                f'{self.adversario:<22} - {self.adversario.mao}'
        # return  f'Turno {self.turno+1} \n' \
        #         f'{self.jogador} - {self.jogador.mao}' \
        #          ' x ' \
        #         f'{self.adversario.mao} - {self.adversario}'

    def __eq__(self, estado):
        return  self.jogador    == estado.jogador \
            and self.adversario == estado.adversario

    def resultado(self):
        if self.terminal():
            return self.adversario.nome, self.adversario.exibe_cor()
        return 'empate', ""