import random as rd
import numpy as np
import string

#VARIÁVEIS GLOBAIS QUE DITAM O COMPORTAMENTO DA POPULAÇÃO
CROSSOVER_RATE = 1
MUTATION_RATE = 0.05
COPIAS = 100
GABARITO = 'ME*THINKS*IT*IS*LIKE*A*WEASEL'
TAMANHO = len(GABARITO)

def criaString():
    #sorteia N caracteres aleatórios para ser a palavra inicial
    palavra = ''                                                               #palavra inicia vazia
    for tam in range(0,TAMANHO):                                                                         
        letra = rd.choice(string.ascii_uppercase + string.digits + '*')        #sorteia um caractere       
        palavra = palavra + letra                                              #concatena o caractere com a palavra
    return palavra

def criaPop(individuo):
    pop = list()                                                    #cria uma lista para armazenar a população
    for tam in range(0,COPIAS):
        pop.append(individuo)                                       #cria um número X de cópias do individuo
    return pop

def mutation(pop, MUTATION_RATE):
    new_pop = list()                                                                            #cria uma lista para armazenar a nova população
    cont = 1                                                                                    #cria um contador para diferenciar o primeiro individuo dos demais
    for c in pop:                                                                               #laço que varre todas as cópias
        if cont == 1:                                                                           #analisa o primeiro inidivíduo
            new_pop.append(c)                                                                   #o primeiro individuo é adicionado a nova população sem sofrer nenhuma mutação
        else:                                                                                   #analisa os demais indivíduos
            caracteres = list()                                                                 #cria uma lista vazia para armazenar os caracteres do indivíduo
            for i in range (0,TAMANHO):                                                         #varre todos os caracteres do indivíduo
                letra = c[i]                                                                    #armazena o caractere atual na variavel LETRA
                if(rd.random() < MUTATION_RATE):                                                #analisa se terá mutação ou não
                    letra = rd.choice(string.ascii_uppercase + string.digits + '*')             #caso tenha, sorteia uma letra aleatória para a variável LETRA
                    while letra == c[i]:                                                        #laço que garante que a letra sorteada será diferente da atual
                        letra = rd.choice(string.ascii_uppercase + string.digits + '*')
                caracteres.append(letra)                                                        #adiciona a variavel LETRA na lista caracteres
            palavra = ''.join(caracteres)                                                       #junta todos os caracteres da lista em uma string
            new_pop.append(palavra)                                                             #adiciona essa nova string a nova população
            caracteres.clear()                                                                  #limpa a lista caracteres
        cont +=1                                                                                #incrementa o contador de individuos
    return new_pop

def analisaCaso(palavra, gabarito=GABARITO):
    fitness = 0                                             #inicia fitness com 0
    for tam in range(0,TAMANHO):                            #varre todos os caracteres da palavra
        if gabarito[tam] == palavra[tam]:                   #compara o enésimo-caractere da palavra com o enésimo-caractere do string desejada
            fitness+=1                                      #incrementa o fitness caso os caracteres sejam iguais
    return fitness

def popFitness(pop):
    pop_fitness = [analisaCaso(each_solution) for each_solution in pop]      #analisa o fitness de todos os elementos de pop e o armazena em uma lista      
    return pop_fitness
