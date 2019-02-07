from multiprocessing import Pool

def funcao_demorada(el):
    print (el)
    # funcao demorada

def cria_lista(n):
    return []
    
long_list = cria_lista(1)
resultados = []
for el in long_list:
    resultados.append(funcao_demorada(el))