import networkx as nx
from gtufcg.draw_util import drawgv_graph_vs
from src.Q04 import find_business

# Função auxiliar que retorna o identificador de um vértice
def get_Id(g,label):
    for u in g.nodes:
        if g.nodes[u]['label']==label:
            return u    

# Grafo YELP
filename = 's_25_5.graphml'
G = nx.read_graphml("graphs/"+filename, force_multigraph=True)

# Usuário
name = "Helen"
u_id = get_Id(G,name)
b_ids = find_business(G,u_id)
print(u_id, b_ids)
print(f'Sugestões para {name}: {[G.nodes[b]['label'] for b in b_ids]}')


# Visualização do Grafo
#drawgv_graph_vs(G, layoutid='dot',
 #               with_node_labels=True, with_edge_labels=True, 
  #             color_scheme="pastel13",
   #            shape='box', width=100, height=100)
