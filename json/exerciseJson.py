import json
import const

'''
    O objetivo dessa atividade de webservises e treinar a manipulação em jsons
    utilizando a linguagem de programação Python
'''

'''
    JSON com os dados que vamos manipular logo abaixo
'''
biblioteca = '''{

    "informacao": {

        "nome": "Biblioteca Municipal de Barbacena",

        "telefones": ["32 3333-3333", "32 9 9999-9999"]

    },

    "livros": {

        "romance": [

            {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "copias": 10, "emprestados": 5},

            {"titulo": "Quincas Borba", "autor": "Machado de Assis", "copias": 3, "emprestados": 3},

            {"titulo": "O Cortico", "autor": "Aluisio Azevedo", "copias": 3, "emprestados": 0}

        ],

        "tecnologia": [

            {"titulo": "Java: como programar", "autor": "Deitel", "copias": 5, "emprestados": 4},

            {"titulo": "JavaScript: O Guia Definitivo", "autor": "David Flanagan", "copias": 5, "emprestados": 1},

            {"titulo": "C: como programar", "autor": "Deitel", "copias": 1, "emprestados": 1}

        ],

        "autoajuda": [

            {"titulo": "O Segredo", "autor": "Rhonda Byrne", "copias": 2, "emprestados": 0},

            {"titulo": "O Milagre da Manhã", "autor": "Hal Elrod", "copias": 5, "emprestados": 5},

            {"titulo": "Como Fazer Amigos e Influenciar Pessoas", "autor": "Dale Carnegie", "copias": 15, "emprestados": 8}

        ]

    }

}'''

'''
    Método que refica qual é o menor tamanho passado pelo value no dictionary
'''
def searching_for_smaller_size(dictionary,value):
    text = "abcdefghijklm"

    for values in dictionary:
        if len(values[value]) < len(text):
            text = values[value]
    return text

'''
    Método que verifica qual é o maior tamanho de algum value passado por parâmetro presente no dictionary
'''
def searching_for_larger_size(dictionary,value):
    #Variável para armazenar o maior tamanho
    text = ""
    for values in dictionary:
        if len(values[value]) > len(text):
            text = values[value]

    return text

'''
    Método responsável por receber um dicionário e incrimentar um valor representado por value 
'''
def searchingInJson(dictionary,value):
    #Variável para realizar soma
    count = 0
    for values in dictionary:
        count += values[value]

    return count

'''
    Método responsável por verificar se um determindo dado do JSON passado por parâmetro
    é o maior e se ele for setar a variável estática actor com o dado value passado como parâmetro 
'''
def searching_for_the_biggest(dictionary,value_count, value):
    count = 0
    actor = ''

    for option in dictionary:
        valueD = option[value_count]
        if count < valueD:
            count = valueD
            actor = option[value]
    return count,actor

'''
    Método que exporta os json, pegando os dados separados como
    informação, livros, romance, tecnologia e autoajuda para facilitar na manipulação desses dados
'''
def exportation_json():
    biblioteca_json = json.loads(biblioteca)
    #print(biblioteca_json)
    informacoes = biblioteca_json[const.INFORMACAO]
    livros = biblioteca_json[const.LIVROS]

    romatico = livros[const.ROMANCE]
    tecnologia = livros[const.TECNOLOGIA]
    autoajuda = livros[const.AUTOAJUDA]

    #print(informacoes)
    #print(livros)
    #print(romatico)
    #for x in romatico:
        #print(x["titulo"])
    return informacoes,livros,romatico,tecnologia,autoajuda

'''
    Método responsável por chamar as funções que auxiliaram nas respostas das perguntas feitas abaixo.
'''
def control_program():
    informacao,livros,romance,tecnologia,autoajuda = exportation_json()

    # 1) Qual o nome da biblioteca?
    print('\n1- Nome da biblioteca: ' + informacao[const.NOME])
    
    # 2)Quantos telefones a biblioteca possui?
    print('2- Número de telefones = ' + str(len(informacao[const.TELEFONES])))

    # 3) Quantos livros existem na categoria autoajuda?
    print('3- Número de livros de autoajuda: ' + str(len(autoajuda)))

    # 4) Quantos livros diferentes a biblioteca possui?
    print('4- Número de livros da biblioteca: ' + str(len(autoajuda) + len(romance) + len(tecnologia)))

    # 5) Quantos livros totais a biblioteca possui?
    print('5- Número de livros totais da biblioteca: ' + str(searchingInJson(romance,const.COPIAS) + searchingInJson(tecnologia,const.COPIAS) + searchingInJson(autoajuda,const.COPIAS)))

    # 6) Quantos livros da categoria romance estão emprestados?
    print('6- Numéro de livros de romance emprestados: ' + str(searchingInJson(romance,const.EMPRESTADOS)))

    # 7) Qual o autor possui mais livros emprestados?
    countR,actorR = searching_for_the_biggest(romance,const.EMPRESTADOS,const.AUTOR)
    countT,actorT = searching_for_the_biggest(tecnologia,const.EMPRESTADOS,const.AUTOR)
    countA,actorA = searching_for_the_biggest(autoajuda,const.EMPRESTADOS,const.AUTOR)

    if(countA > countR and countA > countT):
        print('7- O autor com mais livros emprestados é: ' + actorA)
    elif(countT > countR):
        print('7- O autor com mais livros emprestados é: ' + actorT)
    else:
        print('7- O autor com mais livros emprestados é: ' + actorR)

    # 8) Qual o nome do livro com mais cópias?
    countR,actorR = searching_for_the_biggest(romance,const.COPIAS,const.TITULO)
    countT,actorT = searching_for_the_biggest(tecnologia,const.COPIAS,const.TITULO)
    countA,actorA = searching_for_the_biggest(autoajuda,const.COPIAS,const.TITULO)

    if(countA > countR and countA > countT):
        print('8- O livro com o maior número de cópias é: ' + actorA)
    elif(countT > countR):
        print('8- O livro com o maior número de cópias é: ' + actorT)
    else:
        print('8- O livro com o maior número de cópias é: ' + actorR)

    # 9) O nome de cada autor e o nome de cada um dos seus livros.
    print('\n9- Autores - títulos:')
    for rom, tec, auto in romance,tecnologia, autoajuda:
        print(rom[const.AUTOR] + ' - ' + rom[const.TITULO])
        print(tec[const.AUTOR] + ' - ' + tec[const.TITULO])
        print(auto[const.AUTOR] + ' - ' + auto[const.TITULO])

    print('\n')

    # 10) Qual a categoria possui mais livros?
    countR = searchingInJson(romance,const.COPIAS)
    countT = searchingInJson(tecnologia,const.COPIAS)
    countA = searchingInJson(autoajuda,const.COPIAS)

    if(countA > countR and countA > countT):
        print('10- A categoria com mais livros é: ' + const.AUTOAJUDA)
    elif(countT > countR):
        print('10- A categoria com mais livros é: ' + const.TECNOLOGIA)
    else:
        print('10- A categoria com mais livros é: ' + const.ROMANCE)
    
    
    
    # 11) Qual o livro com o maior título?
    titleR = searching_for_larger_size(romance,const.TITULO)
    titleT = searching_for_larger_size(tecnologia,const.TITULO)
    titleA = searching_for_larger_size(autoajuda,const.TITULO)

    if len(titleR) > len(titleT) and len(titleR) > len(titleA):
        print('11- O livro com maior título é: ' + titleR)
    elif len(titleT) > len(titleA):
        print('11- O livro com maior título é: ' + titleT)
    else:
        print('11- O livro com maior título é: ' + titleA)


    # 12) Qual o autor com o menor nome?
    actorR = searching_for_smaller_size(romance,const.AUTOR)
    actorT = searching_for_smaller_size(tecnologia,const.AUTOR)
    actorA = searching_for_smaller_size(autoajuda,const.AUTOR)

    if len(actorR) < len(actorT) and len(actorR) < len(actorA):
        print('12- O autor com menor nome é: ' + actorR)
    elif len(actorT) < len(actorA):
        print('12- O autor com menor nome é: ' + actorT)
    else:
        print('12- O autor com menor nome é: ' + actorA)

'''
    Método responsável por inicializar o código
'''
def main():
    control_program()

'''
    Chamando o código que irá inicializar o código
'''
if __name__ == "__main__" :
    main()

