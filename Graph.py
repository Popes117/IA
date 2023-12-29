# Classe grafo para representaçao de grafos,
import math
from queue import Queue
from rua import Rua
from Heu import Heu

import networkx as nx  # biblioteca de tratamento de grafos necessária para desnhar graficamente o grafo
import matplotlib.pyplot as plt  # idem




class Grafo:

    def __init__(self, heuristica: Heu, directed=False):
        self.m_nodes = []
        self.m_directed = directed
        self.m_graph = {}  # dicionario para armazenar os nodos e arestas
        self.m_h = heuristica  # dicionario para posterirmente armazenar as heuristicas para cada nodo -< pesquisa informada

    #############
    # Escrever o grafo como string
    #############
    def __str__(self):
        out = ""
        for key in self.m_graph.keys():
            out = out + "rua " + str(key) + ": " + str(self.m_graph[key]) + "\n"
            return out

    ################################
    # Encontrar nodo pelo nome
    ################################

    def get_node_by_name(self, rua):
        for node in self.m_nodes:
            print(node)
            if node.getRua() == rua.getRua():
                return node

        return None

    ###############################
    # Imprimir arestas
    ###############################

    def imprime_aresta(self):
        listaA = ""
        lista = self.m_graph.keys()
        for nodo in lista:
            for (nodo2, custo) in self.m_graph[nodo]:
                listaA = listaA + nodo.getRua() + " -> " + nodo2.getRua() + " custo: " + str(custo) + "\n"
        return listaA

    #############################
    # Adicionar aresta no grafo
    #############################
   
    def add_edge(self, rua1: Rua, rua2: Rua, weight): #nome freguesia

        if (rua1 not in self.m_nodes):
            self.m_nodes.append(rua1)
            self.m_graph[rua1] = list()
            
        #else:
        #    rua1 = self.get_node_by_name(rua1)   

        if (rua2 not in self.m_nodes):
            self.m_nodes.append(rua2)
            self.m_graph[rua2] = list()
        #else:
        #    rua2 = self.get_node_by_name(rua2)

        self.m_graph[rua1].append((rua2, weight))

        if not self.m_directed:
            self.m_graph[rua2].append((rua1, weight))
        

    def imprimeGrafo(self):
        print(self.m_graph)
        print(self.m_nodes)


    #############################
    # Devolver nodos do Grafo
    ############################

    def getNodes(self):
        return self.m_nodes

    ###############################
    # Devolver o custo de uma aresta
    ################################

    def get_arc_cost(self, rua1, rua2):
        custoT = math.inf
        a = self.m_graph[rua1]  # lista de arestas para aquele nodo
        for (nodo, custo) in a:
            if nodo == rua2:
                custoT = custo

        return custoT

    ##############################
    #  Dado um caminho calcula o seu custo
    ###############################

    def calcula_custo(self, caminho):
        # caminho é uma lista de nodos
        teste = caminho
        custo = 0
        i = 0
        while i + 1 < len(teste):
            custo = custo + self.get_arc_cost(teste[i], teste[i + 1])
            #print(teste[i])
            i = i + 1
        return custo

    ################################################################################
    # Procura DFS
    ################################################################################

    def procura_DFS(self, start, end, path=[], visited=set()):
        path.append(start)
        visited.add(start)

        if start == end:
            # calcular o custo do caminho funçao calcula custo.
            custoT = self.calcula_custo(path)
            return (path, custoT)
        for (adjacente, peso) in self.m_graph[start]:
            if adjacente not in visited:
                resultado = self.procura_DFS(adjacente, end, path, visited)
                if resultado is not None:
                    return resultado,visited
        path.pop()  # se nao encontra remover o que está no caminho......
        return None

    #####################################################
    # Procura BFS
    ######################################################

    def procura_BFS(self, start, end):
        # definir nodos visitados para evitar ciclos
        visited = set()
        fila = Queue()

        # adicionar o nodo inicial à fila e aos visitados
        fila.put(start)
        visited.add(start)

        # garantir que o start node nao tem pais...
        parent = dict()
        parent[start] = None

        path_found = False
        while not fila.empty() and path_found == False:
            nodo_atual = fila.get()
            if nodo_atual == end:
                path_found = True
            else:
                for (adjacente, peso) in self.m_graph[nodo_atual]:
                    if adjacente not in visited:
                        fila.put(adjacente)
                        parent[adjacente] = nodo_atual
                        visited.add(adjacente)



        # Reconstruir o caminho

        path = []
        if path_found:
            path.append(end)
            while parent[end] is not None:
                path.append(parent[end])
                end = parent[end]
            path.reverse()
            # funçao calcula custo caminho
            custo = self.calcula_custo(path)
        return (path, custo, visited)

    ###################################################
    # Função   getneighbours, devolve vizinhos de um nó
    ####################################################

    def getNeighbours(self, nodo):
        lista = []
        for (adjacente, peso) in self.m_graph[nodo]:
            lista.append((adjacente, peso))
        return lista

    #############################################################
    #  Desenha grafo  modo grafico através da biblioteca networkx
    #############################################################

    def desenha(self):
        #criar lista de vertices
        lista_v = self.m_nodes
        #lista_a = []
        g = nx.Graph()
        for nodo in lista_v:
            g.add_node(nodo) #problema é que os valores atraves de gets seriam strings e nós colocamos os valores como Rua e duplicava tudo

            for (adjacente, peso) in self.m_graph[nodo]:
                #lista = (nodo, adjacente)
                # lista_a.append(lista)
                g.add_edge(nodo, adjacente, weight=peso)

        pos = nx.spring_layout(g)
        nx.draw_networkx(g, pos, with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

        plt.draw()
        plt.show()
    
    
    ##########################################3
    #
    def calcula_est(self, estima):
        l = list(estima.keys())
        min_estima = estima[l[0]]
        node = l[0]
        for k, v in estima.items():
            if v < min_estima:
                min_estima = v
                node = k
        return node

    ##########################################
    #    A*
    ##########################################

    def procura_aStar(self, start, end):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = {start}
        closed_list = set([])

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}  ##  g é apra substiruir pelo peso  ???

        g[start] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start] = start
        n = None
        while len(open_list) > 0:
            # find a node with the lowest value of f() - evaluation function
            calc_heurist = {}
            flag = 0
            for v in open_list:
                if n == None:
                    n = v
                else:
                    flag = 1
                    calc_heurist[v] = g[v] + self.m_h.getHeu(v,end)
            if flag == 1:
                min_estima = self.calcula_est(calc_heurist)
                n = min_estima
            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == end:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start)

                reconst_path.reverse()

                #print('Path found: {}'.format(reconst_path))
                return (reconst_path, self.calcula_custo(reconst_path), open_list.add(closed_list))

            # for all neighbors of the current node do
            for (m, weight) in self.getNeighbours(n):  # definir função getneighbours  tem de ter um par nodo peso
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

    ###################################3
    # devolve heuristicas do nodo
    ####################################

    def getH(self, nodo):
        heu = list()
        for node in self.m_h:
            if node not in node.keys:
                heu.append(1000)
            if nodo[node] != 0:
                heu.append(nodo[node])
        return heu


    ##########################################
    #   Greedy
    # Precisa ser alterada
    ##########################################

    def greedy(self, start, end):
        # open_list é uma lista de nodos visitados, mas com vizinhos
        # que ainda não foram todos visitados, começa com o  start
        # closed_list é uma lista de nodos visitados
        # e todos os seus vizinhos também já o foram
        open_list = set([start])
        closed_list = set([])

        # parents é um dicionário que mantém o antecessor de um nodo
        # começa com start
        parents = {}
        parents[start] = start

        while len(open_list) > 0:
            n = None

            # encontraf nodo com a menor heuristica
            for v in open_list:
                if n == None or self.m_h.getHeu(v,end) < self.m_h.getHeu(n,end):
                    n = v

            if n == None:
                print('Path does not exist!')
                return None

            # se o nodo corrente é o destino
            # reconstruir o caminho a partir desse nodo até ao start
            # seguindo o antecessor
            if n == end:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start)

                reconst_path.reverse()

                return (reconst_path, self.calcula_custo(reconst_path), open_list.add(closed_list))

            # para todos os vizinhos  do nodo corrente
            for (m, weight) in self.getNeighbours(n):
                # Se o nodo corrente nao esta na open nem na closed list
                # adiciona-lo à open_list e marcar o antecessor
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n

            # remover n da open_list e adiciona-lo à closed_list
            # porque todos os seus vizinhos foram inspecionados
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None
