import json

escolha = input('Escolha um tema, Herois, Nome: ').lower()

def ler_arquivos(entrada):
    with open(entrada, 'r', encoding='utf8') as arquivo:
         return json.load(arquivo)

def verifica(escolha):
    if escolha == 'h' or escolha == 'herois':
        HEROIS = 'projeto\\lista.json'
        return ler_arquivos(HEROIS)
    elif escolha == 'n' or escolha == 'nome':
        NOME = 'projeto\\teste.json'
        return ler_arquivos(NOME)
    else:
        return ImportError('Erro de importação')


personagens = verifica(escolha)