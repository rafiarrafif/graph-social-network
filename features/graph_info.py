import networkx as nx

def show_graph_information(graph: nx.DiGraph) -> None:
    print("======== Informasi Graph ========")
    print(f"Jumlah node: {graph.number_of_nodes()}")
    print(f"Jumlah edge: {graph.number_of_edges()}")
    print("=================================")