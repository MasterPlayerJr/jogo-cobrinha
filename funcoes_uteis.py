from time import sleep
import os
import json

'''
Aqui tem algumas funçôes
'''

def limpar(tempo):
    sleep(tempo)
    os.system('cls' if os.name == 'nt' else 'clear')

def int_lista(lista):
    tam_lista = len(lista)
    for i in range(0,tam_lista):
        lista[i] = int(lista[i])
    return lista

def mostrar_dict(dicionario):
    for i in dicionario:
        print(f'{i}: {dicionario[i]}')

def abrir_json(nome_arquivo):
    arq_json = open(nome_arquivo)
    dict = json.load(arq_json)
    return dict