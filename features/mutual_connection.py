import networkx as nx


def show_mutual_connection(graph: nx.DiGraph) -> None:
    print("\n")
    print("========= Mutual Connection =========")
    user_a = input("Username A: ").strip()
    user_b = input("Username B: ").strip()

    if user_a not in graph:
        print(f"\nUser '{user_a}' tidak ditemukan.")
        return

    if user_b not in graph:
        print(f"\nUser '{user_b}' tidak ditemukan.")
        return

    following_a = set(graph.successors(user_a))
    following_b = set(graph.successors(user_b))
    mutual_connections = following_a.intersection(following_b)
    if not mutual_connections:
        print(
            f"\nTidak ada hubungan saling mengikuti antara "
            f"'{user_a}' dan '{user_b}'."
        )
        return

    print("\nMutual Connections:")

    for user in sorted(mutual_connections):
        print(f"- {user}")
    print("======================================")
