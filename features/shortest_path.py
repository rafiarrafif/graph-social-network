import networkx as nx
import helpers.bfs as bfs

def show_shortest_path(graph: nx.DiGraph) -> None:
    print("\n")
    print("==== Sortest Path Relasi ====")
    user_a = input("Username A: ").strip()
    user_b = input("Username B: ").strip()

    if user_a not in graph:
        print(f"\nUser '{user_a}' tidak ditemukan.")
        return

    if user_b not in graph:
        print(f"\nUser '{user_b}' tidak ditemukan.")
        return

    undirected_graph = graph.to_undirected()
    try:
        path = bfs.sortest_path(undirected_graph, user_a, user_b)

        print("\nShortest Path:")
        print(" -> ".join(path))
        print(f"\nDistance : {len(path) - 1}")

    except nx.NetworkXNoPath:
        print(
            f"\nTidak ada jalur terhubung antara user A dan B."
            f"'{user_a}' and '{user_b}'."
        )
    print('=============================')
