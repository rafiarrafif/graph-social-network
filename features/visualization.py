from pathlib import Path
import webbrowser

import networkx as nx
from pyvis.network import Network


def show_visualization(graph: nx.DiGraph) -> None:
    print("\nGenerating graph visualization...")

    net = Network(
        height="900px",
        width="100%",
        directed=True,
        notebook=False
    )

    net.from_nx(graph)
    net.show_buttons(filter_=["physics"])
    output_file = Path("social_network_visualization.html")
    net.save_graph(str(output_file))
    webbrowser.open(output_file.resolve().as_uri())
    print("Visualization opened in browser.")