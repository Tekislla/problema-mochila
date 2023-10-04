import random

objetos = [
    {"nome": "objeto1", "peso": 5, "recompensa": 10},
    {"nome": "objeto2", "peso": 7, "recompensa": 13},
    {"nome": "objeto3", "peso": 3, "recompensa": 7},
    {"nome": "objeto4", "peso": 2, "recompensa": 5},
    {"nome": "objeto5", "peso": 8, "recompensa": 20},
]
capacidade_mochila = 10

def criar_solucao_inicial():
    return [random.randint(0, 1) for _ in objetos]

def avaliar_solucao(solucao):
    peso_total = sum(objetos[i]["peso"] for i in range(len(solucao)) if solucao[i] == 1)
    recompensa_total = sum(objetos[i]["recompensa"] for i in range(len(solucao)) if solucao[i] == 1)
    
    if peso_total > capacidade_mochila:
        return 0
    
    return recompensa_total

def crossover(solucao1, solucao2):
    ponto_corte = random.randint(1, len(solucao1) - 1)
    filho1 = solucao1[:ponto_corte] + solucao2[ponto_corte:]
    filho2 = solucao2[:ponto_corte] + solucao1[ponto_corte:]
    return filho1, filho2

def mutacao(solucao):
    index = random.randint(0, len(solucao) - 1)
    solucao[index] = 1 - solucao[index]

tamanho_populacao = 100
num_geracoes = 100
taxa_crossover = 0.7
taxa_mutacao = 0.2

populacao = [criar_solucao_inicial() for _ in range(tamanho_populacao)]

for geracao in range(num_geracoes):
    populacao = sorted(populacao, key=avaliar_solucao, reverse=True)
    nova_populacao = []
    
    nova_populacao.extend(populacao[:10])
    
    while len(nova_populacao) < tamanho_populacao:
        pai1, pai2 = random.choices(populacao[:50], k=2)
        filho1, filho2 = crossover(pai1, pai2)
        mutacao(filho1)
        mutacao(filho2)
        nova_populacao.extend([filho1, filho2])
    
    populacao = nova_populacao

melhor_solucao = max(populacao, key=avaliar_solucao)
melhor_recompensa = avaliar_solucao(melhor_solucao)

print("Melhor solução:", melhor_solucao)
print("Melhor recompensa:", melhor_recompensa)
