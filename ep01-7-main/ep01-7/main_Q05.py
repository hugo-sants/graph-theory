import networkx as nx
from gtufcg.draw_util import drawgv_graph_vs, create_graph_img, drawgv_duo
from src.Q05 import business_graph

# Função auxiliar que retorna o identificador de um vértice
def get_Id(g,label):
    for u in g.nodes:
        if g.nodes[u]['label']==label:
            return u    

# Grafo YELP
filename = 'IL/state_IL_city_Cahokia.graphml'
G = nx.read_graphml("graphs/"+filename, force_multigraph=True)

# Usuário
B = business_graph(G, 'Restaurant')
print(f'{B.nodes}')
print(f'{B.edges}')

# Visualização
GV = create_graph_img(G, layoutid="dot", shape="box", width=10, height=10, with_node_labels=True) 
for u in B.nodes:
    B.nodes[u]['label'] = G.nodes[u]['label']
CV = create_graph_img(B, layoutid="dot", shape="box", with_edge_labels=True, width=100, height=100, with_node_labels=True) 
drawgv_duo(GV, CV, title1="Grafo YELP", title2="Grafo Business", 
           width=10, height=8)
