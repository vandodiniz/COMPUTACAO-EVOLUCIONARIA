import random as rd
import numpy as np

#variaveis globais que ditam o comportamento do código
crossover_rate = 1
mutation_rate = 0.8 
tamanhoTabuleiro = 8
pop_init = 20

#função disponibilizada pelo professor para gerar a população inicial
def init_population(_mu:int = pop_init, n:int = tamanhoTabuleiro):         
    population = []                                                                 
    for i in range (_mu):
        population.append(rd.sample(range(n), n))
    return population

#função disponibilizada pelo professor para avaliar o número de xeques de uma solução
def fitness_nq(solution):                                                   
    xeques = 0
    for i in range(0,len(solution)):
        for j in range(0,len(solution)):
            if i!=j:
                if i-solution[i] == j-solution[j] or i+solution[i] == j+solution[j]:
                    xeques+=1
    return xeques

def selection(pop):
    #retorna entre 5 soluçoes aleatórias, as duas melhores
    pop_fitness = [fitness_nq(each_solution) for each_solution in pop]    # Mostra o número de xeques de toda a população
    candidatos = list()                                                   # Cria uma lista para armazenar os candidatos a serem pais
    posicao = list()                                                      # Cria uma lista para armazenar a posição desses pais na lista pop
    for c in range(0,5):                                                  # Laço responsável por escolher os 5 indivíduos aleatórios e os colocar na lista 'candidatos' e suas posições na lista 'posicao'
        n = rd.randint(0,len(pop_fitness)-1)
        while n in posicao:                                               # Garante que não haverá um mesmo individuo escolhido 2x
            n = rd.randint(0,len(pop_fitness)-1)
        candidatos.append(pop_fitness[n])                                   
        posicao.append(n)
    menor1 = menor2 = candidatos[0]                                       # Algoritmo para descobrir os 2 menores numeros de candidatos e suas posiçoes. Assume=se primeiramente que os 2 menores numeros são iguais ao primeiro candidato
    cont = pos1 = pos2 =  0
    for c in candidatos:                                                  # Varre a lista inteira 
        if c < menor1:                                                    # Caso c seja menor que o menor número, c passa a ser o menor número e 'pos1' guarda a posição dele
            menor1 = c
            pos1 = cont
        elif c <=menor2:                                                  # Caso c seja menor ou igual que o segundo menor número, c passa a ser ele e 'pos2' guarda a posição dele
            menor2 = c
            pos2 = cont
        cont=cont+1                                                       # Contador incrementa 1 no final. MUITO IMPORTANTE para saber a posição dos números
    pais = [pop[posicao[pos1]], pop[posicao[pos2]]]                       # Cria uma lista pais com os dois individuos selecionados
    return pais

def crossover(pais, crossover_rate):
    '''Código disponibilizado pelo professor em .m
       Apenas adaptamos ele para .pynb         '''
    sizeGeno = np.size(pais, 1)                                 
    crianca = np.zeros((sizeGeno))                          
    offspring = np.array([crianca, crianca], np.int32)      #cria uma array para armazenar os 2 novos individuos
    pos = round(rd.randint(1,sizeGeno-1))
    offspring[0][0:pos] = pais[0][0:pos]                    #iguala os genes dos filhos aos pais até certa parte para manter a hereditariedade
    offspring[1][0:pos] = pais[1][0:pos]
    s1=s2=pos
    if rd.random()<crossover_rate:                          #permuta o restante dos genes
        for i in range(0, sizeGeno):                    
            check1=check2=0
            for j in range(pos):
                if pais[1][i] == offspring[0][j]:
                        check1 = 1
                if pais[0][i] == offspring[1][j]:
                        check2 = 1
            if check1 == 0:
                offspring[0][s1] = pais[1][i]
                s1 = s1+1
            if check2 == 0:
                offspring[1][s2] = pais[0][i]
                s2 = s2+1    
    else:
        offspring = pais
    return offspring

def mutation(offspring, mutation_rate):
    if mutation_rate > rd.random():                                                 #analisa se vai ter ou não mutação
        for c in range(0,2):                                                        #processo se repete para os dois filhos
            n1 = rd.randint(0, tamanhoTabuleiro -1)                                 #sorteia duas posiçoes para serem trocadas
            n2 = rd.randint(0, tamanhoTabuleiro -1)
            while n1==n2:                                                           #garante que não sejam duas posições iguais
                n2 = rd.randint(0,tamanhoTabuleiro -1)
            temp = offspring[c][n1]                                                 #variavel auxiliar que armazena o valor daquela posição        
            offspring[c][n1] = offspring[c][n2]                                     #faz a troca de fato
            offspring[c][n2] = temp                                                     
    return offspring

def replacement(offspring_new, pop):
    for c in range(0,2):                                                            #processo se repete para os dois filhos        
        pop_fitness = [fitness_nq(each_solution) for each_solution in pop]          #analisa todos os indivíduos da população
        maior = max(pop_fitness)                                                    #descobre qual é o pior indivíduo
        pos = pop_fitness.index(maior)                                              #descobre a posição do pior indivíduo
        del(pop[pos])                                                               #deleta o pior indivíduo
        pop.append(offspring_new[c])                                                #adiciona o filho
    return pop