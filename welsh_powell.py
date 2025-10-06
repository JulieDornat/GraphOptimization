# 1. Retrieve the degree of each vertex in the graph.
# 2. Sort the vertices in decreasing order based on their degrees. In some cases, there are many possibilities.
# 3. Assign a color to the first vertex A of the list.
# 4. For each vertices in the list, assign the same color to the first vertice B which is not adjacent to A.
# 5. Scroll through the list until the next vertice C which is not adjacent to A and B.
# 6. Continue until the end of the list.
# 7. Take a second color for the first vertice D of the list not colored yet.
# 8. Repeat steps 4 to 7 until all vertices are colored.

from graphe import graphe

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

    for node in sorted_nodes[1:]:
        adjacent = False
        for colored_node in color_assignment:
            # If the node is adjacent to the colored node, we cannot assign the same color
            if node in G.edges[colored_node]:
                adjacent = True
            # If the node is not adjacent to a colored node, we can assign the same color
            else:
                adjacent = False
                color_assignment[node] = color_assignment[colored_node]
                break
        # If the node is adjacent to all colored nodes, we need a new color
        if adjacent:
            current_color += 1
            color_assignment[node] = current_color

    print("Color assignment:", color_assignment)
    
        
        



#### --- TEST --- ####
G = graphe({"A", "B", "C", "D", "E", "F", "G"}, {
    "A": {"B", "C", "D"},
    "B": {"A", "E", "F"},
    "C": {"A", "F"},
    "D": {"A", "G"},
    "E": {"B"},
    "F": {"B", "C"},
    "G": {"D"}
})
welsh_powell(G)
