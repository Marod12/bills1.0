# -*- coding: utf-8 -*-
# parte inicial do programa
from lib.servico import *

arq = 'servicos.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu('MENU PRINCIPAL', ['Serviços', 'Cadastrar Serviço', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        dados = lerArquivo(arq)
        servicos(dados)
    elif resposta == 2:
        # Opção de cadastrar um serviço novo!
        cabeçalho('Cadastrar Serviço')
        servicosNovos = cadastro()
        cadastrar(arq, servicosNovos)
    elif resposta == 3:
        cabeçalho('Saindo do Sistema...  Até logo')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m'.center(50))
