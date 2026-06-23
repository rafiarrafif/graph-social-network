import networkx as nx


def show_out_degree(graph: nx.DiGraph) -> None:
    print("\n====== Out Degree (Following) ======")
    for user, degree in graph.out_degree():
        print(f"{user:<20} : {degree}")
    print("======================================")

