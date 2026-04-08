# EXEMPLOS DE USO ( ver folder graphs ):
# python view_user_graph.py --graph graphs/sample5_5_simple.graphml
# python view_user_graph.py --graph graphs/sample5_5_simple.graphml --only_connected

import argparse
import networkx as nx
from gtufcg.draw_util import drawgv_graph_vs

parser = argparse.ArgumentParser(description="Visualizar grafo de usuários e negócios de arquivo GraphML")
parser.add_argument("--graph", default="graphs/sample5_5_simple.graphml", help="Caminho para arquivo GraphML (padrão: graphs/sample10_5.graphml)")
parser.add_argument("--only-connected", action="store_true", help="Exibir todos os vértices ou ocultar vértices isolados")
args = parser.parse_args()

G = nx.read_graphml(args.graph, force_multigraph=True)

# Criar visão H apenas vértices não isolados, se solicitado
if args.only_connected:
    print("Filtrando apenas vértices conectados (grau > 0)")
    connected_nodes = [n for n in G.nodes if G.degree(n) > 0]
    H = G.subgraph(connected_nodes)
else:
    print("Exibindo todos os vértices (incluindo isolados)")
    H = G

user_nodes = [n for n, d in H.nodes(data=True) if d.get('type') == 'user']
business_nodes = [n for n, d in H.nodes(data=True) if d.get('type') == 'business']

for a in H.nodes:
    H.nodes[a]['label'] = H.nodes[a]['name']
for u, v, k in H.edges:
    H[u][v][k]['label'] = H[u][v][k]['type']

print(f'Reviews: {[(u,v,d) for u,v,d in H.edges(data=True)]}')

drawgv_graph_vs(H, layoutid="dot", width=100, height=100,
                shape="plaintext", color_scheme="pastel13",
                with_node_labels=True, with_edge_labels=True,
                components=[user_nodes, business_nodes])