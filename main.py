# Trabalho de TPA - Tabela Hash (Dicionário Português)
# Autor: Gabriel Marchezi


# Biblioteca utilizada para o cálculo da distância de Levenshtein: python-Levenshtein
# Necessário a instalação da biblioteca via: pip install python-Levenshtein
from Levenshtein import distance as lev

# Implementação da Tabela Hash
from Hash_Table import *

#Biblioteca Interface Gráfica
from tkinter import *
from tkinter import ttk

#Biblioteca para lidar com Strings
import string

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

#Função que procura a palavra no dicionário e caso não encontre, procura palavras similares.
def search_lev2(search_word, dicionario):
    lst = []
    search_word_2 = search_word.translate(str.maketrans('','',string.punctuation)).lower()
    if dicionario.find(search_word_2) is not None:
        lst.append(1)
        lst.append(search_word)
    else:
        lst.append(0)
        lst.append(search_word)
        for i in dicionario.buckets:
            if i is not None:
                lev_dist = lev(str(i.key),str(search_word_2))
                if lev_dist == 1:
                    lst.append(i.key)
    print(lst)
    return lst


def main_editor(dic):

    '''def callback():
        words = []
        text = textEditor.get(0.1,END)
        for word in text.split():
            words.append(word)

        for word in words:
            lev = search_lev2(word, dic)
            print(lev)
    '''

    def corrige(e):

        def aplica_corr():
            retorno = opcoes.curselection()
            if len(retorno) > 0:
                if lev[1][0].isupper() == True:
                    words[len(words)-1] = words[len(words)-1].replace(lev[1].translate(str.maketrans('','',string.punctuation)), opcoes.get(retorno[0]).capitalize())
                else:
                    words[len(words)-1] = words[len(words)-1].replace(lev[1].translate(str.maketrans('','',string.punctuation)), opcoes.get(retorno[0]))
            textEditor.delete(0.0,END)
            for word in words:
                word = word + ' '
                textEditor.insert(INSERT, word)
            root2.destroy()
            return

        words = []
        text = textEditor.get(0.1,END)
        for word in text.split():
            words.append(word)
        lev = search_lev2(words[len(words)-1], dic)
        if lev[0] == 0:
            if len(lev) > 2:
                root2 = Tk()
                texto = 'A palavra ' + lev[1] + ' não foi encontrada. Você quis dizer?'
                title = Text(root2,width=40,height=5)
                #title.insert(INSERT,texto)
                title.insert(INSERT,'A palavra ')
                title.insert(INSERT,lev[1],('alert'))
                title.tag_configure('alert',background='yellow')
                title.insert(INSERT, ' não foi encontrada. Você quis dizer?')
                title['state'] = DISABLED
                title.pack()
                opcoes = Listbox(root2,selectmode=SINGLE, selectbackground='green')
                scrollbar = Scrollbar(root2,orient='vertical',command=opcoes.yview)
                opcoes['yscrollcommand'] = scrollbar.set
                scrollbar.pack(side='right',fill='y')
                for i in range(len(lev)):
                    if (i > 1):
                        opcoes.insert(i,lev[i])
                opcoes.pack()
                buttonOk = Button(root2,text='OK', command=aplica_corr)
                buttonOk.pack()
                root2.geometry('500x300')
                root2.mainloop()
            else:
                print(words)
                print(lev)
                textEditor.delete(0.0,END)
                for i in range(len(words)):
                    print(i)
                    if i == (len(words)-1):
                        textEditor.insert(INSERT,words[i],('error'))
                        textEditor.tag_configure('error', background='yellow')
                        textEditor.insert(INSERT," ")
                    else:
                        aux = words[i] + ' '
                        textEditor.insert(INSERT,aux)
            

    root = Tk()
    textEditor = Text(root,width=80,height=30)
    textEditor.pack()
    #button1 = Button(root,text = 'Corrigir Texto', command=callback)
    #button1.pack(pady=12)
    #button2 = Button(root,text = 'Corrigir Última Palavra', command=callback)
    #button2.pack(pady=6)
    root.geometry('800x600')
    root.title('Trab. TPA - Hash Table')
    root.bind('<space>',corrige)
    #root.bind('<Return>',corrige)
    root.mainloop()


def main():
    dicionario = iniciar_dicionario('pt.dic')
    main_editor(dicionario)


'''def main():
    full = input('Carregar dicionário completo? (s/n): ')
    if full.upper() == 'S':
        dicionario = iniciar_dicionario('pt.dic')
    if full.upper() == 'N':
        dicionario = iniciar_dicionario('pt_sample.dic')
    while True:
        search_word = input("Digite uma palavra: ")
        search_lev(search_word, dicionario)
'''

if __name__ == '__main__':
    main()