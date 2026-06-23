from typing import cast

import process.csv_loader as csv_loader
import process.build_graph as build_graph
import networkx as nx

def main():
    print("Pastikan data telah berada didalam folder ./data/social_following.csv")
    input("Tekan enter untuk melanjutkan...")
    df = csv_loader.datasets()
    graph = cast(nx.DiGraph, build_graph.build(df))

    print("=============================")
    print("Graph jaringan sosial media")
    print("=============================")
    print("silahkan pilih menu yang tersedia:")
    print("1. Menampilkan informasi graph")
    print("2. Menampilkan in degree (followers)")
    print("3. Menampilkan out degree (following)")
    user_input = int(input("Pilih menu: "))

    match user_input:
        case 1:
            import features.graph_info as graph_info
            graph_info.show_graph_information(graph)
        case 2:
            import features.in_degree as in_degree
            in_degree.show_in_degree(graph)
        case 3:
            import features.out_degree as out_degree
            out_degree.show_out_degree(graph)
        case _:
            print("Menu tidak ditemukan. Silahkan coba lagi.")  

if __name__ == "__main__":
    main()