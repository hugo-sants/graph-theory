import networkx as nx
from gtufcg.draw_util import drawgv_graph_vs, create_graph_img, drawgv_duo
from src.Q05 import business_polarization

# Exemplo de uso da função
name = "Cahokia_10_2"
#name = "IL/state_IL_city_Cahokia"
S = nx.read_graphml("graphs/"+name+".graphml", force_multigraph=True)
U = [x for x in S.nodes if S.nodes[x]["type"]=="user"]
B = [x for x in S.nodes if S.nodes[x]["type"]=="business"]

for b in B:
    p = business_polarization(S,b)
    if p >= 0.3:
        print(f"{S.nodes[b]['name']}: {p}")


