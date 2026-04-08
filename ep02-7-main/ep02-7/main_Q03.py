import networkx as nx
from gtufcg.draw_util import drawgv_graph_vs
from src.Q03 import dense_biclique

# Exemplo de uso da função 
name = "Sauget_3_2"
G = nx.read_graphml("graphs/"+name+".graphml", force_multigraph=True)
X = [x for x in G.nodes if G.nodes[x]["type"]=="user"]
Y = [x for x in G.nodes if G.nodes[x]["type"]=="business"]

C = dense_biclique(G,3,2)
for c in C:
    print(c)

# Destacando na visualização a primeira tupla retornada
if C:
    C0 = C[0][0]
    C1 = C[0][1]
else:
    C0 = []
    C1 = []
X = [x for x in G.nodes if G.nodes[x]["type"]=="user" if not x in C0]
Y = [x for x in G.nodes if G.nodes[x]["type"]=="business" if not x in C1]
Z_x = [x for x in C0]
Z_y = [x for x in C1]
drawgv_graph_vs(G, layoutid="dot", shape="box", width=10, height=10, with_node_labels=True, 
                components=[X,Y,Z_x,Z_y]) 


