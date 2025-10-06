class graphe:
    def __init__(self, X: list, E: dict):
        self.nodes = X # {"A", "B", "C"}
        self.edges = E 

    def degree(self, node):
        return len(self.edges[node])