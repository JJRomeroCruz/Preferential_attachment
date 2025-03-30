#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 12:43:18 2024

@author: juanjo
"""
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random as random

# Funcion que nos simula el modelo de preferential attachment
def preferential(N, m0):
    # Inicializamos el grafo con m0 nodos
    G = nx.Graph()
    G.add_nodes_from([i for i in range(m0)])
    # Unimos algún nodo de forma aleatoria con el 0 (para que despues no dividamos entre 0)
    G.add_edge(0, random.randint(0, m0))
    tiempo = []
    tiempo.append(range(m0))
    k0 = [] # Grados del nodo 0
    k0.append(G.degree.values[0])
    # Unimos con nodos
    for i in range(m0, N):
        total = sum(dict(G.degree()).values())
        nodos_unidos = []
        G.add_node(i)
        for j in range(len(G.nodes())):
            num = random.random()
            #print(G.degree[j]/total)
            if(num > G.degree[j]/total):
                nodos_unidos.append(j)
        for elemento in nodos_unidos:
            G.add_edge(i, elemento)
        tiempo.append(i)
        k0.append(G.degree.values[0])
    return G, tiempo, k0
# Funcion que nos saca la distribucion de probabilidad del nodo

# Funcion que nos saca y representa la regresion lineal, asi como las pendientes

""" Usamos las funciones """

G, tiempo, k0 = preferential(1200, 2)
d = nx.degree_histogram(G)
# Dibujamos el grafo
pos = nx.spring_layout(G)
node_degrees = dict(G.degree())
node_size = [(node_degrees[node] + 1) for node in G.nodes()]
nx.draw(G, pos, with_labels = False, node_size = node_size, node_color = 'blue', font_size = 1, font_weight = 'bold', edge_color = 'skyblue')
plt.title('Grafo')
plt.show()
print(d)