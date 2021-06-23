# -*- coding: utf-8 -*-
# trabalha com a parte dos arquivos
import ast # importa uma bliblioteca para tranformar uma string em dict

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') # rt leitura de arquivo texto
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # wt+ gravação de arquivo texto incluido o arquivo se caso ele não exista ( + que cria um arquivo se não tiver arquivo )
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        servicos = []
        #return a.read() # ler linha por linha de um Arquivo
        for linha in a:
            dado = linha.split('\n') # elimina o \n e tranforma o dado em uma lista
            #print(f'{dado[0][1:-1]}') tira o primeiro dado de uma string e o ultimo
            servico = ast.literal_eval(dado[0])
            #print(type(servico)) #validadndo o dado para ver se virou {}
            servicos.append(servico)
        #print(servicos) #verificando os dados que iram ser retornados
        return servicos
    finally:
        a.close()


def cadastrar(arq, servicos):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            for servico in servicos:
                a.write(f'{servico}\n')  # o ue será escrito na linha

            a.close()
        except:
            print('Houve um ERRO na hora de escrever os dados!')



def atualizar(arq, servicos):
    try:
        a = open(arq, 'wt')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            for servico in servicos:
                a.write(f'{servico}\n')  # o ue será escrito na linha

            a.close()
        except:
            print('Houve um ERRO na hora de escrever os dados!')
