from sort import selection_sort, insertion_sort, bubble_sort
import json
import os
import sys
import json
import numpy as np
import time
import matplotlib.pyplot as plt

def main():
    os.system('cls||clear')
    print('\033[1m'+'==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n')
    print('Estrutura de Dados 2 - Algoritmos de Ordenção O(n²)\n')
    print('==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n')
    print('Selecione uma opção: ' + '\n')
    print('[1] - Ordenar Matérias')
    print('[2] - Teste de Desempenho')
    print('[3] - Sair')
    print('')
    print('\033[1m'+'==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n' + '\033[0m')
    option = int(input('>>>'))

    while(option not in [1, 2, 3]):
        option = int(input("Insira uma opção válida: "))

    if(option == 1):
        discipline_menu()
    elif(option == 2):
        graph_menu()
    else:
        sys.exit()

def discipline_menu():

    os.system('cls||clear')

    with open('disciplines.json') as f:
        disciplines = json.load(f)

    print('\033[1m'+'==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n')
    print('Estrutura de Dados 2 - Algoritmos de Ordenção O(n²)\n')
    print('==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n')
    print('Selecione uma opção de busca: ' + '\n')
    print('[1] - Selection Sort')
    print('[2] - Insertion Sort')
    print('[3] - Bubble Sort')
    print('[4] - Sair')
    print('')
    print('\033[1m'+'==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n' + '\033[0m')
    option = int(input('>>>'))

    while(option not in [1, 2, 3, 4]):
        option = int(input("Insira uma opção válida: "))

    if(option == 4):
        sys.exit()
    
    os.system('cls||clear')
    
    print('\033[1m'+'==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n')
    print('Estrutura de Dados 2 - Algoritmos de Ordenção O(n²)\n')
    print('==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n')
    print('Ordernar por : ' + '\n')
    print('[1] - Código da Matéria')
    print('[2] - Nome da Matéria')
    print('[3] - Sair')
    print('')
    print('\033[1m'+'==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n' + '\033[0m')
    param = int(input('>>>'))

    while(option not in [1, 2, 3]):
        option = int(input("Insira uma opção válida: "))

    if(param == 3):
        sys.exit()

    param = 'name' if (param > 1) else 'code' 

    if(option == 1):
        start = time.time()
        disciplines = selection_sort(disciplines, param)
        end = time.time()
        runtime = end - start
    elif(option == 2): 
        start = time.time()
        disciplines = insertion_sort(disciplines, param)
        end = time.time()
        runtime = end - start
    else: 
        start = time.time()
        disciplines = bubble_sort(disciplines, param)
        end = time.time()
        runtime = end - start

    
    os.system('cls||clear')
    print('\033[1m'+'==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n')

    for i in range(0, 45):
        print(disciplines[i]['code'], '-', disciplines[i]['name'])
    
    print('\033[0m', '\n', 'Tempo de execução:', runtime)
        
    print('\n'+ '\033[1m' + '==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n' + '\033[0m')
    
def graph_menu():
    
    os.system('cls||clear')

    with open('disciplines.json') as f:
        disciplines = json.load(f)


    print('\033[1m'+'==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n')
    print('Estrutura de Dados 2 - Algoritmos de Ordenção O(n²)\n')
    print('==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n')
    print('Ordernar por : ' + '\n')
    print('[1] - Código da Matéria')
    print('[2] - Nome da Matéria')
    print('[3] - Sair')
    print('')
    print('\033[1m'+'==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n' + '\033[0m')
    param = int(input('>>>'))

    param = 'name' if (param > 1) else 'code' 

    runtime = []
    sort = ['Insertion Sort', 'Selection Sort', 'Bubble Sort']

    start = time.time()
    i = insertion_sort(disciplines, param)
    end = time.time()
    runtime.append(end - start)

    with open('disciplines.json') as f:
        disciplines = json.load(f)

    start = time.time()
    i = selection_sort(disciplines, param)
    end = time.time()
    runtime.append(end - start)

    with open('disciplines.json') as f:
        disciplines = json.load(f)
    
    start = time.time()
    i = bubble_sort(disciplines, param)
    end = time.time()
    runtime.append(end - start)

    print(runtime)

    plt.figure(figsize=(10,5))
    plt.barh(sort, runtime, color='blue')
    plt.xlabel('Tempo de execução')
    plt.show()

if __name__ == '__main__':
    main()
