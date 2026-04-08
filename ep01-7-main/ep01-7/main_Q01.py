import networkx as nx
from gtufcg.draw_util import drawgv_graph_vs, create_graph_img, drawgv_duo
from src.Q01 import co_reviewers

name = "s_25_5.graphml"
G = nx.read_graphml("graphs/"+name, force_multigraph=True)
C = co_reviewers(G)

# Imprimindo vértices e arestas do grapo de co-revisores
print(C.nodes(data=True))
print(C.edges(data=True))

# Imprimindo vértices e arestas do grafo de co-revisores (com labels para facilitar visualização)
print([G.nodes[n]['label'] for n in C.nodes])
print([f'({G.nodes[x]['label']}, {G.nodes[y]['label']}, "business": {G.nodes[C[x][y][k]["business"]]['label']})' for x,y,k in C.edges])

# Visualização
GV = create_graph_img(G, layoutid="dot", shape="box", width=10, height=10, with_node_labels=True) 
for u in C.nodes:
    C.nodes[u]['label'] = G.nodes[u]['label']
for x, y, k in C.edges:
    b = C[x][y][k]['business']
    C[x][y][k]['label'] = G.nodes[b]['label']
CV = create_graph_img(C, layoutid="dot", shape="box", with_edge_labels=True, width=100, height=100, with_node_labels=True) 
drawgv_duo(GV, CV, title1="GrafoYELP", title2="Grafo Co-revisores", 
           width=10, height=8)
