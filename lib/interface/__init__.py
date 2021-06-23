def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def linha(tam = 42):  #tam = 42
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(nomeMenu, lista):
    cabeçalho(nomeMenu)
    c = 1
    for item in lista:
        print(f' {c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt(' Sua Opção: ')
    return opc


def questionSN(msg, metodo, metodo2):
    while True:
        m = str(input(msg)).upper().strip()
        if m == metodo:
            return m
            break
        elif m == metodo2:
            return m
            break
        else:
            print('\033[31mERRO! Digite uma opção válida!\033[m'.center(50))


def ValidandoNum(msg, valor):
    while True:
        m = int(input(msg))
        if m <= valor and m > 0:
            return m
            break
        else:
            print('\033[31mERRO! Digite uma opção válida!\033[m'.center(50))


def ValidandoEdit(msg, valor):
    while True:
        m = int(input(msg))
        if m <= valor and m > 0:
            return m
            break
        elif m == 0:
            return m
            break
        elif m == 99:
            return m
            break
        elif m == 100:
            return m
            break
        else:
            print('\033[31mERRO! Digite uma opção válida!\033[m'.center(50))
