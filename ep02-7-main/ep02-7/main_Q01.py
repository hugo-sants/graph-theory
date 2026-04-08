import networkx as nx
from gtufcg.draw_util import drawgv_graph_vs, create_graph_img, drawgv_duo
from src.Q01 import weighted_user_graph

# Exemplo de uso da função 
name = "Sauget_5_2.graphml"
G = nx.read_graphml("graphs/"+name, force_multigraph=True)
X = [x for x in G.nodes if G.nodes[x]["type"]=="user"]
Y = [x for x in G.nodes if G.nodes[x]["type"]=="business"]

C = weighted_user_graph(G)
print(C.nodes)
print(C.edges(data=True))

GV = create_graph_img(G, layoutid="dot", shape="box", width=10, height=10, with_node_labels=True, components=[X,Y]) 
count = 0
for u in C.nodes:
    C.nodes[u]['label'] = G.nodes[u]['label']
for x, y in C.edges:
    b = C[x][y]['weight']
    C[x][y]['label'] = str(b)
    if b > 2:
        print(f"Um maior {b}")
        count = count+1
print(count)

CV = create_graph_img(C, layoutid="dot", shape="box", with_edge_labels=True, width=100, height=100, with_node_labels=True) 
drawgv_duo(GV, CV, title1="GrafoYELP", title2="Grafo Co-revisores", 
           width=10, height=8)

