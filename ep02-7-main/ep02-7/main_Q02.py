import networkx as nx
from gtufcg.draw_util import drawgv_graph_vs
from src.Q02 import critical_users

# Exemplo de uso da função 
name = "Cahokia_esparso_20"
G = nx.read_graphml("graphs/"+name+".graphml", force_multigraph=True)
X = [x for x in G.nodes if G.nodes[x]["type"]=="user"]
Y = [x for x in G.nodes if G.nodes[x]["type"]=="business"]

C = critical_users(G)
print(C)

X = [x for x in G.nodes if G.nodes[x]["type"]=="user" and not x in C.keys()]
Y = [x for x in G.nodes if G.nodes[x]["type"]=="business"]

drawgv_graph_vs(G, layoutid="dot", shape="box", width=10, height=10, with_node_labels=True, 
                components=[X,Y,C]) 

