import networkx as nx
import matplotlib.pyplot as plt


def visualize_graph(graph):
    if graph.directed:
        G = nx.DiGraph()
    else:
        G = nx.Graph()

    for vertex in graph.vertices.values():
        G.add_node(vertex.name)
        for neighbor in vertex.adjacency_list:
            G.add_edge(vertex.name, neighbor.name)

    pos = nx.spring_layout(G, k=1)  # positions for all nodes

    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue')

    # edges
    if graph.directed:
        nx.draw_networkx_edges(G, pos, edgelist=G.edges(),
                               arrowstyle='-|>', arrowsize=20)
    else:
        nx.draw_networkx_edges(G, pos, edgelist=G.edges())

    # labels
    nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

    plt.title("Graph Visualization")
    plt.axis('off')  # turn off the axis
    plt.show()
