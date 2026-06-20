import networkx as nx


def show_in_degree(graph: nx.DiGraph) -> None:
    print("======== In Degree (Followers) ========")
    for user, degree in graph.in_degree():
        print(f"{user:<20} : {degree}")
    print("=======================================")
