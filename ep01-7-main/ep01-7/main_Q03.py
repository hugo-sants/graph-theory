import networkx as nx
from gtufcg.draw_util import drawgv_graph_vs
from src.Q03 import intergraph_users

name1 = "IL/state_IL_city_Dupo.graphml"
name2 = 'IL/state_IL_city_Millstadt.graphml'
G1 = nx.read_graphml("graphs/"+name1, force_multigraph=True)
G2 = nx.read_graphml("graphs/"+name2, force_multigraph=True)

c_users = intergraph_users(G1, G2)
print(c_users.nodes)
print([c_users.nodes[u]['label'] for u in c_users.nodes])
print(c_users.edges)
print([(c_users.nodes[u]['label'], c_users.nodes[b]['label']) for b,u in c_users.edges])

user_nodes = [u for u in c_users.nodes if c_users.nodes[u]['type']=='user']
business_nodes = [u for u in c_users.nodes if c_users.nodes[u]['type']=='business']
drawgv_graph_vs(c_users, layoutid='dot', components=[business_nodes, user_nodes],
                with_node_labels=True, with_edge_labels=True, color_scheme="pastel13",
                shape='plain', width=100, height=100)
