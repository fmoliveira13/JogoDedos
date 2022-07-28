#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import mkdir, remove
from glob import glob
from controlador.jogo_dedos import JogoDedos
from jogadores.jogador import Jogador
from jogadores.humano_j import Humano
from jogadores.minimax import Minimax
from statistics import median
from datetime import datetime
import os

def saudacao():
    print(f'*{"*":-^50}*')
    print(f'{"BEM VINDO AO JOGO DOS DEDOS!!!":^50}')
    print(f'*{"*":-^50}*')
    print()

def selecionar_jogadores():
    red = JogoDedos.selecionar_jogador(Jogador.RED)
    blue = JogoDedos.selecionar_jogador(Jogador.BLUE)
    return red, blue

def configurar_partida():
    while True:
        try:
            x = input('Informe o numero de jogos (min: 1 | max: 1000): ')
            partidas = int(x)
            x = input('Informe o numero de turnos (min: 10 | max: 500): ')
            rodadas = int(x)
        except ValueError:
            print(f'\nOpcao "{x}" invalida!\n')
            continue

        if partidas not in range(1,1000+1):
            print('\nNumero de partidas invalida! Digite um numero no intervalo informado\n')
            continue

        if rodadas not in range(1,500+1):
            print('\nNumero de turnos invalido! Digite um numero no intervalo informado\n')
            continue

        print()
        return partidas, rodadas

def configuracao_inicial(red, blue, partidas):
    acompanhar_jogadas = False
    if Humano.__name__ in (blue.__class__.__name__, red.__class__.__name__):
        acompanhar_jogadas = True
        partidas = 1

    if issubclass(red.__class__, Minimax):
        red.define_iteracoes()
        red.nome += str(red.iteracoes)

    if issubclass(blue.__class__, Minimax):
        blue.define_iteracoes()
        blue.nome += str(blue.iteracoes)

    return partidas, acompanhar_jogadas

def obter_estatisticas(cond, lista_turnos, lista_num_partida):
    if cond:
        min_turno, max_turno = min(lista_turnos), max(lista_turnos)
        p_min = lista_num_partida[(lista_turnos.index(min_turno))]
        p_max = lista_num_partida[(lista_turnos.index(max_turno))]
        med_turno = int(median(lista_turnos))
        return min_turno, max_turno, p_min, p_max, med_turno
    return['...','...','...','...','...']


def obter_resumo(partidas,red,v_red,p_red,blue,v_blue,p_blue,empates,p_empates, tempo, jogo):
    turnos_partidas_ganhas_por_red = []
    turnos_partidas_ganhas_por_blue = []
    num_partida_red = []
    num_partida_blue = []
    r = False
    b = False
    # breakpoint()
    for i,partida in enumerate(partidas):
        if partida.resultado()[0] != 'empate':
            if partida.resultado()[1] == 'RED':
                turnos_partidas_ganhas_por_red.append(partida.turno)
                num_partida_red.append(i+1)
                r = True
            if partida.resultado()[1] == 'BLUE':
                turnos_partidas_ganhas_por_blue.append(partida.turno)
                num_partida_blue.append(i+1)
                b = True

    min_turno_red, max_turno_red, p_min_red, p_max_red, med_turno_red = obter_estatisticas(r, turnos_partidas_ganhas_por_red, num_partida_red)
    min_turno_blue, max_turno_blue, p_min_blue, p_max_blue, med_turno_blue = obter_estatisticas(b, turnos_partidas_ganhas_por_blue, num_partida_blue)

    txt = f'{"RESUMO":-^55}\n' \
    f'| {f"":^52}|\n' \
    f'| {f"Tempo de jogo: {tempo}":<52}|\n' \
    f'| {f"Total de jogos: {jogo.partidas}":<52}|\n' \
    f'| {f"Jogadas permitidas: {jogo.rodadas*2}":<52}|\n' \
    f'| {f"":^52}|\n' \
    f'| {f"Vitorias {red} : {v_red} ({p_red}%)":<52}|\n' \
    f'| {f"Vitorias {blue} : {v_blue} ({p_blue}%)":<52}|\n' \
    f'| {f"Empates : {empates} ({p_empates}%)":<52}|\n' \
    f'| {f"":^52}|\n' \
    f'| {f"{red}":<52}|\n' \
    f'| {f"-Vitoria mais rapida: {min_turno_red} jogadas (partida {p_min_red})":<52}|\n' \
    f'| {f"-Vitoria mais longa: {max_turno_red} jogadas (partida {p_max_red})":<52}|\n' \
    f'| {f"-Mediana das vitorias: {med_turno_red} jogadas ":<52}|\n' \
    f'| {f"":^52}|\n' \
    f'| {f"{blue}":<52}|\n' \
    f'| {f"-Vitoria mais rapida: {min_turno_blue} jogadas (partida {p_min_blue})":<52}|\n' \
    f'| {f"-Vitoria mais longa: {max_turno_blue} jogadas (partida {p_max_blue})":<52}|\n' \
    f'| {f"-Mediana das vitorias: {med_turno_blue} jogadas ":<52}|\n' \
    f'{"":-^55}'
    return txt

def obter_caminho(pasta):
    cur = os.path.dirname(os.path.abspath(__file__))
    caminho = os.path.join(cur,*pasta.split('/'))
    return caminho

def criar_pasta(caminho):
    try:
        mkdir(caminho)
    except:
        pass

def deletar_arquivos(lista_arquivos):
    for arquivo in lista_arquivos:
        try:
            remove(arquivo)
        except:
            print("Erro ao tentar deletar :", arquivo)

def criar_arquivo_resumo(caminho, resumo):
    with open(f'{caminho}/__resumo__.txt', 'w') as fl:
        fl.write(resumo)

def criar_arquivo_jogadas(partidas, caminho):
    for i, partida in enumerate(partidas):
        turnos = partida.turno
        vencedor = '_'.join(partida.resultado())
        nome_arquivo_jogo = f'p{i + 1}_t{turnos + 1}_{vencedor}.txt'

        with open(f'{caminho}/{nome_arquivo_jogo}', 'w') as fl:
            txt = partida.exibir_jogadas()
            fl.write(txt)

def encerramento(caminho):
    print('\n\nFIM!!!')
    print(f'Arquivos salvos em: {caminho}\n')
    input('...Pressione enter para sair...')

def jogar(red, blue, turnos, partidas):
    partidas, acompanhar_jogadas = configuracao_inicial(red, blue, partidas)
    jogo = JogoDedos(red, blue, turnos, partidas, acompanhar_jogadas)
    inicio = datetime.now()
    partidas, vitorias_red, p_red, vitorias_blue, p_blue, empates, p_empates = jogo.iniciar()
    fim = datetime.now()
    tempo = fim - inicio
    resumo = obter_resumo(partidas, red, vitorias_red, p_red, blue, vitorias_blue, p_blue, empates, p_empates, tempo, jogo)
    nome_partida = f'{red.nome}_x_{blue.nome}'
    caminho = obter_caminho(f'partidas/{nome_partida}')
    criar_pasta(caminho)
    lista_arquivos = glob(f'{caminho}/*.txt')
    deletar_arquivos(lista_arquivos)
    criar_arquivo_resumo(caminho, resumo)
    criar_arquivo_jogadas(partidas, caminho)
    encerramento(caminho)
