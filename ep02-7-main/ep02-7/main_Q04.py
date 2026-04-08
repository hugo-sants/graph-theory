import networkx as nx
from gtufcg.draw_util import drawgv_graph_vs, create_graph_img, drawgv_duo
from src.Q04 import recommendation_capacity

# Exemplo de uso da função
name = "Sauget_10_2"
S = nx.read_graphml("graphs/"+name+".graphml", force_multigraph=True)
U = [x for x in S.nodes if S.nodes[x]["type"]=="user"]
B = [x for x in S.nodes if S.nodes[x]["type"]=="business"]

print(f"Capacidade para conjunto completo: {recommendation_capacity(S, U, B)}")
U1 = U[0:5]
B1 = B[0:3]    
print(f"Capacidade do subconjunto: {recommendation_capacity(S, U1, B1)}")

# Subconjunto destacado em verde
drawgv_graph_vs(S, layoutid="dot", shape="box", width=10, height=10, with_node_labels=True, 
                components=[U,B,U1,B1]) 