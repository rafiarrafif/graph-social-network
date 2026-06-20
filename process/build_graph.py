import networkx as nx
import pandas as pd

def build(df: pd.DataFrame) -> nx.DiGraph | None:
    try:
        graph = nx.DiGraph()
        graph.add_edges_from(df[['from_user', 'to_user']].itertuples(index=False, name=None))
        return graph
    except Exception as e:
        print(f"Error building graph. Pastikan nama kolom adalah 'from_user' dan 'to_user'. {e}")
        exit(1)
