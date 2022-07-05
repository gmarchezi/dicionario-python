# Trabalho de TPA - Tabela Hash (Dicionário Português)
# Autor: Gabriel Marchezi

#Não foi implementado nenhuma interface gráfica, o programa deverá ser executado via Terminal

# Biblioteca utilizada para o cálculo da distância de Levenshtein: python-Levenshtein
# Necessário a instalação da biblioteca via: pip install python-Levenshtein
from Levenshtein import distance as lev

# Implementação da Tabela Hash
from Hash_Table import *

#Função que recebe como paramêtro o arquivo dicionário e retorna uma lista das palavras contidas no mesmo.
def read_arq(dic):
    words = []
    arq = open(dic,encoding='UTF-16')
    for i in arq.readlines():
        words.append(i.replace('\n',''))
    return words

#Função que recebe como parâmetro o dicionário e chama a função "read_arq", inicia a Tabela Hash e insere as palavras. Retorna a Tabela Hash.
def iniciar_dicionario(dic):
    words = read_arq(dic)
    dicionario = HashTable()

    for word in words:
        dicionario.insert(word, word)
    
    return dicionario

#Função que procura a palavra no dicionário e caso não encontre, procura palavras similares.
def search_lev(search_word, dicionario):
    if dicionario.find(search_word) is not None:
            print('A palavra ',dicionario.find(search_word), ' foi encontrada!')
    else:
        print('Palavra não encontrada.')
        for i in dicionario.buckets:
            if i is not None:
                lev_dist = lev(str(i.key),str(search_word))
                if lev_dist == 1:
                    print('Palavra Semelhante: ',i.key)


def main():
    full = input('Carregar dicionário completo? (s/n): ')
    if full.upper() == 'S':
        dicionario = iniciar_dicionario('pt.dic')
    if full.upper() == 'N':
        dicionario = iniciar_dicionario('pt_sample.dic')
    while True:
        search_word = input("Digite uma palavra: ")
        search_lev(search_word, dicionario)

if __name__ == '__main__':
    main()