from graphe import graphe
import random

def bron_kerbosch1(G: graphe, K: list, C: list):
    if not C:
        return K 
    else:
        res = []
        for x in C:
            voisins = G.edges[x]
            inter = [e for e in C if e in voisins] # on calcule C inter gamma(x)
            res.append(bron_kerbosch1(G, K+list(x), inter)) 
        return max(res, key=len) # on renvoie la plus grande des cliques maximales trouvées

def bron_kerbosch2(G: graphe, K: list, C: list, A:list):
    if not C:
        return K
    res = []
    while A:
        x = random.choice(A)
        voisins = G.edges[x]
        inter_C = [e for e in C if e in voisins] # on calcule C inter gamma(x)
        inter_A = [e for e in A if e in voisins] # on calcule A inter gamma(x)
        res.append(bron_kerbosch2(G, K+list(x), inter_C, inter_A))
        A.remove(x)
    return max(res, key=len) # on renvoie la plus grande des cliques maximales trouvées

def clique3(G: graphe):
    l = sorted(G.nodes, key=lambda x: len(G.edges[x]), reverse=True)
    for x in range(len(l)):
        for y in range(x+1, len(l)):
            for z in range(y+1, len(l)):
                if l[x] in [e for e in G.edges[l[y]] if e in G.edges[l[z]]]:
                    return [l[x], l[y], l[z]]
    return []

def cliques3(G:graphe):
    l = sorted([e for e in G.nodes if len(G.edges[e]) >= 2], key=lambda x: len(G.edges[x]), reverse=True)
    res = []
    while l:
        x = l[0]
        voisins_x = G.edges[x]
        for y in [e for e in voisins_x if e in l]:
            voisins_y = G.edges[y]
            voisins_communs = [e for e in voisins_x if e in voisins_y and e in l]
            for z in voisins_communs:
                res.append([x, y, z])
    l.remove(x)
    return res