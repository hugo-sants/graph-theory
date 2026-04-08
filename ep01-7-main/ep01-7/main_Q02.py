import networkx as nx
from gtufcg.draw_util import drawgv_graph_vs, create_graph_img, drawgv_duo
from src.Q02 import get_business

name = "s_25_5.graphml"
G = nx.read_graphml("graphs/"+name, force_multigraph=True)
dict_business = get_business(G)
print(dict_business)

for k,b_list in dict_business.items():
    print(k,[G.nodes[b]['label'] for b in b_list])
