#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import *

saudacao()
red, blue = selecionar_jogadores()
partidas, turnos = configurar_partida()
jogar(red, blue, turnos, partidas)