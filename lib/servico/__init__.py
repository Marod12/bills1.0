# -*- coding: utf-8 -*-
from lib.arquivo import *
from lib.interface import *

def cadastro():
    servicos = []  # list()  #[]
    servico = {}  # dict()  #{}

    while True:
        nome = str(input("Digite o nome do serviço: ")).upper()
        login = str(input("Digite o login do serviço: "))
        senha = str(input("Digite a senha do serviço: "))


        nomeEncrypt = encrypt(nome)
        loginEncrypt = encrypt(login)
        senhaEncrypt = encrypt(senha)

        servico["nome"] = nomeEncrypt
        servico["login"] = loginEncrypt
        servico["senha"] = senhaEncrypt

        while True:
            question = questionSN("deseja cadastrar mais dados? [S/N]: ", 'S', 'N')
            if question == "N":
                break
            nomeDoDado = str(input("Nome do dado: "))
            dado = str(input("Dado: "))

            dadoEncrypt = encrypt(dado)

            servico[nomeDoDado] = dadoEncrypt  # or servico[nomeDoDado: Dado]

        '''Dicts functions
        print(len(servico))
        #servico.clear
        print(servico.values())
        print(servico.keys())
        print(servico.items())'''

        servicos.append(servico.copy())  # importante tenho q copiar serviço para dentro da lista serviços
        print(f'\nServiço {decrypt(servico["nome"])} adicionado com SUCESSO!\n')
        servico.clear()  # limpa o dict(),  apagando um serviço antes de add outro

        question = questionSN("deseja cadastrar outro serviço? [S/N]: ", 'S', 'N')
        if question == "N":
            break
    return servicos


def servicos(dados):
    servicos = dados

    while True:
        resposta = menu('SERVIÇOS CADASTRADOS', ['Listar todos os serviços', 'Pesquisar por serviço', 'Editar serviço', 'Excluir serviço', 'Voltar'])

        if resposta == 1:
            # Lista o Nome dos serviços cadastrados!
            lista = []
            for servico in servicos:
                lista.append(decrypt(servico["nome"])) #pega cada um dos nomes cadastrados na lista e os coloca em uma lista

            result = sorted(lista) #pega a lista e a coloca em ordem alfabetica
            for i in result: #pecorre a lista e mostra todos os itens da lista em ordem alfabetica
                print(f'{i}'.center(42)) #alinha ao centro

            return #retorna para o menu principal

        if resposta == 2:
            # Pesquisa ver se tem o que é pesquisado nos nomes dos serviços e retorna os serviços que contenham o que é pesquisado
            pesquisa = str(input('  Pesquisa: ')).upper()
            lista = []
            for servico in servicos: #percorre os servicos
                if pesquisa in decrypt(servico["nome"]): #verifica se contem algo parecido com a pesquisa nos nomes do serviço
                    lista.append(decrypt(servico["nome"])) #cada um que for adicionado é add a lista

            if lista == []: #se a lista não tiver nenhum dado
                print('* Nenhum serviço foi encontrado! *'.center(42))
            else:
                if len(lista) == 1: #se a lista tiver só um servico nela
                    print(lista[0].center(42))
                    question = questionSN("deseja ver os dados desse serviço? [S/N]: ", 'S', 'N')
                    if question == 'S':
                        pesquisaEncry = encrypt(lista[0])
                        for servico in servicos:
                            if pesquisaEncry in servico["nome"]:
                                if True:
                                    for i in servico:  # mostra os dados do servico escolhido
                                        print(f'{i}: {decrypt(servico[i])}'.center(42))

                if len(lista) > 1: #se a lista tiver mais de 1 servico nela
                    result = sorted(lista) #colocar a lista em oredem alfabetica
                    cont = 1
                    for i in result:
                        print(f'{cont} - {i}'.center(42)) #mostra os servicos encontrados que estao na lista
                        cont += 1

                    question = questionSN("deseja ver os dados de algum desses serviços? [S/N]: ", 'S', 'N')
                    if question == 'S':
                        numServico = ValidandoNum("digite o número do serviço que deseja ver: ", len(lista))
                        nameServico = result[numServico - 1]

                        print(nameServico.center(42))

                        pesquisaEncry = encrypt(nameServico)
                        for servico in servicos:
                            if pesquisaEncry in servico["nome"]:
                                if True:
                                    for i in servico: #mostra os dados do servico escolhido
                                        print(f'{i}: {decrypt(servico[i])}'.center(42))

            return #retorna para o menu principal

        if resposta == 3:
            # atualiza algum dado de um determinado serviço
            nomeServico = str(input('Digite o nome do serviço: ')).upper()

            lista = []

            pesquisaEncry = encrypt(nomeServico)
            for i, v in enumerate(servicos): #enumera os itens da lista servicos
                if pesquisaEncry in v["nome"]: #verifica se a pesquisa é igual a um servico cadastrado

                    print(nomeServico.center(42))  # mostra o nome do servico

                    # print(i, v) #mostra a posição na listas e seu conteudo
                    print('0 - add um novo dado'.center(42))
                    for k, y in enumerate(v): #enumera os dados do servico e os coloca em uma lista
                        lista.append(y)
                        print(f'{int(k) + 1} - alterar {y}'.center(42))
                    print('99 - exclui um dado'.center(42))
                    print('100 - Voltar <-'.center(42))
                    numDado = ValidandoEdit(" Sua Opção: ", len(lista)) #pegunta qual é a opção do usuario

                    # se a opção for 0 ou 99 ou 100
                    if numDado == 0 or numDado == 99 or numDado == 100:
                        if numDado == 0:
                            nomeDoNovoDado = str(input("Nome do dado: "))
                            novoDado = str(input("Dado: "))
                            v[f'{nomeDoNovoDado}'] = encrypt(novoDado)

                            print(f'\n  {nomeDoNovoDado}: {decrypt(v[f"{nomeDoNovoDado}"])} adicionado com SUCESSO!\n')

                            servicos[i] = v

                            atualizar('servicos.txt', servicos)
                            return

                        if numDado == 99:
                            numDadoExcl = ValidandoNum(" Número do dado a ser exluido: ", len(lista))
                            if numDadoExcl == 1:
                                print('O nome NÃO pode ser excluido!!'.center(42))
                                return
                            confirmation = questionSN(f"tem certeza que deseja EXCLUIR {lista[numDadoExcl - 1]}? [S/N]: ", 'S', 'N')
                            if confirmation == 'S':
                                del v[f'{lista[numDadoExcl - 1]}'] #exclui o dado
                                print(f'\n  {lista[numDadoExcl - 1]} excluido com SUCESSO!\n'.center(42))

                                servicos[i] = v

                                atualizar('servicos.txt', servicos)
                                return
                            if confirmation == 'N':
                                return

                        if numDado == 100:
                            return

                    else:
                        #para alterar os dados ja existentes
                        nameDado = lista[numDado - 1]

                        print(f'{lista[numDado - 1]} atual é {decrypt(v[nameDado])}'.center(42))
                        dadoAtual = decrypt(v[nameDado])

                        if nameDado == "nome":
                            novoValor = str(input(f"Digite oa nov(oa) {lista[numDado - 1]} do serviço: ")).upper()
                        else:
                            novoValor = str(input(f"Digite oa nov(oa) {lista[numDado - 1]} do serviço: "))

                        v[f'{lista[numDado - 1]}'] = encrypt(novoValor)

                        print(f'\033[32m{lista[numDado - 1]} alterada com SUCESSO!\033[m'.center(50))
                        print(f'de {dadoAtual} para {novoValor}'.center(42))

                        servicos[i] = v

                        atualizar('servicos.txt', servicos)
                        return

            else:
                print(f'* Não temos nenhuma serviço com {nomeServico} cadastrado *'.center(42))

            return #retorna para o menu principal

        if resposta == 4:
            # deleta um determinado serviço
            nomeServico = str(input('Digite o nome do serviço: ')).upper()

            pesquisaEncry = encrypt(nomeServico)
            for i, v in enumerate(servicos):  # enumera os itens da lista servicos
                if pesquisaEncry in v["nome"]:  # verifica se a pesquisa é igual a um servico cadastrado

                    nomeServicoEncontrado = decrypt(v["nome"])

                    print(nomeServicoEncontrado.center(42))  # mostra o nome do servico
                    # print(i, v) #mostra a posição na listas e seu conteudo

                    confirmation = questionSN(f"tem certeza que deseja EXCLUIR o serviço \"{nomeServicoEncontrado}\"? [S/N]: ", 'S', 'N')
                    if confirmation == 'S':
                        # print(v, '\n', servicos[i]) # verificando se os dois são iguais
                        print(f'Serviço \"{nomeServicoEncontrado}\" excluido com SUCESSO!'.center(42))
                        del servicos[i] #excluindo o serviço

                        atualizar('servicos.txt', servicos) #salva o arquivo editado
                        return

                    if confirmation == 'N':
                        return

            return  # retorna para o menu principal

        if resposta == 5:
            cabeçalho('Voltando para o Menu principal')
            break

        else:
            print('\033[31mERRO! Digite uma opção válida!\033[m'.center(50))


Alfabeto = 'abcdefghijklmnopqrstuvwxyz'
AlfabetoM = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
cond = 1

def cryp(msg, dir):
    m = ''
    for c in msg:
        if c in AlfabetoM:
            c_index = AlfabetoM.index(c)
            m += AlfabetoM[(c_index + (dir * cond)) % len(AlfabetoM)]
        else:
            m += c
    return m

def encrypt(msg):
    return cryp(msg, len(msg))

def decrypt(msg):
    return cryp(msg, -len(msg))
