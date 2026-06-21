import networkx as nx


def show_most_active_user(graph: nx.DiGraph) -> None:
    degrees = dict(graph.out_degree())
    max_following = max(degrees.values())
    active_users = [
        user
        for user, following in degrees.items()
        if following == max_following
    ]

    print('\n')
    print("====== Most Active User ======")
    for user in active_users:
        print(f"Username  : {user}")
        print(f"Following : {max_following}")
    print('==============================')