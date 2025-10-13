from graphe import graphe
import random

def bron_kerbosch1(G: graphe, K: list, C: list):
    """ 
    Renvoie la plus grande amelioration possible d'une clique donnée par l'algorithme de braun-kerbosch

    Args:
        graphe G:   le graphe dans lequel chercher la clique
        str list K: liste des points d'une clique deja trouvée
        str list C: liste des voisins communs de tous les points de K
    
    Return: 
        str list: la liste des points de la plus grande clique trouvée
    """
    if not C:
        return K 
    else:
        res = [K]
        for x in C:
            voisins = G.edges[x]
            inter = [e for e in C if e in voisins] # on calcule C inter gamma(x)
            res.append(bron_kerbosch1(G, K+list(x), inter)) 
        return max(res, key=len) # on renvoie la plus grande des cliques maximales trouvées

def bron_kerbosch2(G: graphe, K: list, C: list, A:list):
    """ 
    Renvoie la plus grande amelioration possible d'une clique donnée par la version améliorée de l'algorithme de braun-kerbosch

    Args:
        graphe G:   le graphe dans lequel chercher la clique
        str list K: liste des points d'une clique deja trouvée
        str list C: liste des voisins communs de tous les points de K
        str list A: sous ensemble de C des points encore possibles d'ajouter a la clique
    
    Return: 
        str list: la liste des points de la plus grande clique trouvée
    """
    if not C:
        return K
    res = [K]
    while A:
        x = random.choice(A)
        voisins = G.edges[x]
        inter_C = [e for e in C if e in voisins] # on calcule C inter gamma(x)
        inter_A = [e for e in A if e in voisins] # on calcule A inter gamma(x)
        res.append(bron_kerbosch2(G, K+list(x), inter_C, inter_A))
        A.remove(x)
    return max(res, key=len) # on renvoie la plus grande des cliques maximales trouvées

def bron_kerbosch(G: graphe, K: list, ameliore: bool):
    """
    Renvoie la plus grande amelioration possible d'une clique donnée par l'algorithme de braun-kerbosch

    Args:
        graphe G:      Le graphe global
        str list K:    liste des points de G formant une clique déja trouvée
        bool ameliore: True si on veut la version améliorée de l'algorithme, false sinon

    Return
        str list: la liste des points de la plus grande clique trouvée
    """
    C = []
    for x in G.edges[K[0]]:
        for i in range(1, len(K)):
            if x not in G.edges[K[i]]:
                break
        C.append(x)
    if ameliore:
        return bron_kerbosch2(G, K, C, C)
    else:
        return bron_kerbosch1(G, K, C)