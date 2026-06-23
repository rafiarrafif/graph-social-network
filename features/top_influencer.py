import networkx as nx

def show_top_influencer(graph: nx.DiGraph) -> None:
    degrees = dict(graph.in_degree())
    max_followers = max(degrees.values())
    influencers = [
        user
        for user, followers in degrees.items()
        if followers == max_followers
    ]

    print('\n')
    print("========= Top Influencer =========")
    for user in influencers:
        print(f"Username  : {user}")
        print(f"Followers : {max_followers}")
        print()
    print("==================================")
