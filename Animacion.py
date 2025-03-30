#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 18:55:13 2024

@author: juanjo
"""
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def preferential_attachment_animation(num_nodes, num_edges_to_attach, num_iterations):
    # Función para actualizar el grafo en cada iteración
    def update(frame):
        G.add_node(frame)
        
        # Selecciona nodos para unirse con preferential attachment
        nodes_to_attach = []
        for _ in range(num_edges_to_attach):
            node = random.choice(list(G.nodes()))
            nodes_to_attach.append(node)
        
        # Añade el nuevo nodo y se conecta a los nodos seleccionados
        for node_to_attach in nodes_to_attach:
            G.add_edge(frame, node_to_attach)
        
        # Dibuja el grafo actualizado
        ax.clear()
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=100, ax=ax)
        ax.set_title(f"Iteración {frame + 1}")

    # Crea un nuevo grafo vacío
    G = nx.Graph()
    
    # Configura la figura y el eje para la animación
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Crea la animación
    ani = animation.FuncAnimation(fig, update, frames=num_iterations, interval=1000)
    ani.save('Problema14.gif')
    plt.title("Modelo de preferential attachment (Barabási-Albert)")
    plt.show()

# Parámetros de la simulación
num_nodes = 30  # Número total de nodos en la simulación
num_edges_to_attach = 2  # Número de enlaces que se agregarán para cada nuevo nodo
num_iterations = num_nodes - 2  # Número total de iteraciones (nodos a agregar)

# Ejecuta la animación
preferential_attachment_animation(num_nodes, num_edges_to_attach, num_iterations)

#ani = preferential_attachment_model_animation(num_nodes, num_edges_to_attach, num_steps)
