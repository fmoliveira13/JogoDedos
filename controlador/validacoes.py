#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Avaliador:

    INTERVALO = range(0,5) #dedos

    def maos(maos):
        for mao in maos:
            assert mao in Avaliador.INTERVALO, f'Mão {maos} inválida!'

    def inicio_com_terminal(maos):
        assert maos != (0,0), 'Não é possível iniciar o jogo com mão terminal!'

    def jogadores(cor_jogador, cor_adversario):
        assert cor_jogador != cor_adversario, 'Jogadores iniciados com a mesma cor!'

    def cor(cor):
        assert cor in [-1,1], f'Cor "{cor}" inválida!'
