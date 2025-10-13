# 1. Retrieve the degree of each vertex in the graph.
# 2. Sort the vertices in decreasing order based on their degrees. In some cases, there are many possibilities.
# 3. Assign a color to the first vertex A of the list.
# 4. For each vertices in the list, assign the same color to the first vertice B which is not adjacent to A.
# 5. Scroll through the list until the next vertice C which is not adjacent to A and B.
# 6. Continue until the end of the list.
# 7. Take a second color for the first vertice D of the list not colored yet.
# 8. Repeat steps 4 to 7 until all vertices are colored.

from graphe import graphe
import time

### --- WELSH-POWELL ALGORITHM --- ###
### Hypothesis: G is a simple undirected graph
def welsh_powell(G: graphe):
    # Retrieve the degree of each vertex in the graph
    node_degrees = {node: G.degree(node) for node in G.nodes}
    print("Node degrees:", node_degrees)

    # Sort the vertices in decreasing order based on their degrees
    sorted_nodes = sorted(node_degrees, key=node_degrees.get, reverse=True)
    print("Sorted nodes by degree:", sorted_nodes)

    # Assign a color to the first vertex A of the list.
    current_color = 0
    current_node = sorted_nodes[0]
    color_assignment = {current_node: current_color} # Color assignment dictionary

    # For each vertex in the list, assign colors
    for node in sorted_nodes[1:]:
        colored = False
        neighbors = G.edges[node]
        unauthorized_colors = []

        # For each neighbor of the current node, collect their colors
        for neighbor in neighbors:
            if neighbor in color_assignment:
                unauthorized_colors.append(color_assignment[neighbor])

        # For each already colored node, check if we can assign the same color
        for colored_node in color_assignment:
            # If the node is not adjacent to a colored node and this colored node has an authorized color, we can assign the same color
            if node not in G.edges[colored_node] and color_assignment[colored_node] not in unauthorized_colors:
                colored = True
                color_assignment[node] = color_assignment[colored_node]
                break
        
        # If the node is not colored yet, we need a new color
        if not colored:
            current_color += 1
            color_assignment[node] = current_color

    print("Color assignment:", color_assignment)
    return color_assignment
    
### --- VALIDATION FUNCTION --- ###
def is_valid_coloring(G: graphe, color_assignment: dict):
    # For each node
    for node in G.nodes:
        color = color_assignment[node]
        # Check that none of its neighbors have the same color and are colored
        for neighbor in G.edges[node]:
            if neighbor not in color_assignment:
                print("Neighbor", neighbor, "not colored")
                return False
            if color_assignment[neighbor] == color:
                print("Node", node, "and neighbor", neighbor, "have the same color", color)
                return False   
    return True


#### --- TEST --- ####
# Test random graph
G = graphe({"A", "B", "C", "D", "E", "F", "G"}, {
    "A": {"B", "C", "D"},
    "B": {"A", "E", "F"},
    "C": {"A", "F"},
    "D": {"A", "G"},
    "E": {"B"},
    "F": {"B", "C"},
    "G": {"D"}
})

start = time.time()
color_assignments = welsh_powell(G)
end = time.time()
print("Execution time:", end - start)
print("Is valid coloring:", is_valid_coloring(G, color_assignments))


# Test star graph
G_star = graphe({"A", "B", "C", "D", "E"}, {
    "A": {"B", "C", "D", "E"},
    "B": {"A"},
    "C": {"A"},
    "D": {"A"},
    "E": {"A"}
})
start = time.time()
color_assignments = welsh_powell(G_star)
end = time.time()
print("Execution time:", end - start)
print("Is valid coloring:", is_valid_coloring(G_star, color_assignments))

# Test complete graph
G_complete = graphe({"A", "B", "C", "D"}, {
    "A": {"B", "C", "D"},
    "B": {"A", "C", "D"},
    "C": {"A", "B", "D"},
    "D": {"A", "B", "C"}
})

start = time.time()
color_assignments = welsh_powell(G_complete)
end = time.time()
print("Execution time:", end - start)
print("Is valid coloring:", is_valid_coloring(G_complete, color_assignments))

# Test bipartite graph
G_bipartite = graphe({"A", "B", "C", "D", "E"}, {
    "A": {"D", "E"},
    "B": {"D", "E"},
    "C": {"D"},
    "D": {"A", "B", "C"},
    "E": {"A", "B"}
})

start = time.time()
color_assignments = welsh_powell(G_bipartite)
end = time.time()
print("Execution time:", end - start)
print("Is valid coloring:", is_valid_coloring(G_bipartite, color_assignments))


# Test cycle graph
G_cycle = graphe({"A", "B", "C", "D"}, {
    "A": {"B", "D"},
    "B": {"A", "C"},
    "C": {"B", "D"},
    "D": {"A", "C"}
})

start = time.time()
color_assignments = welsh_powell(G_cycle)
end = time.time()
print("Execution time:", end - start)
print("Is valid coloring:", is_valid_coloring(G_cycle, color_assignments))


