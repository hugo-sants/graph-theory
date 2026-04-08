import networkx as nx

# Análise de componentes conectados do grafo
name = "IL/state_IL_city_Columbia.graphml"
G = nx.read_graphml("graphs/"+name, force_multigraph=True)
X = [x for x in G.nodes if G.nodes[x]["type"]=="user"]
Y = [x for x in G.nodes if G.nodes[x]["type"]=="business"]
print(f"Total de usuários: {len(X)}, negócios: {len(Y)}")

C = nx.connected_components(G)
print("Componentes conectados:")
for c in C:
    X = [x for x in c if G.nodes[x]["type"]=="user"]
    Y = [x for x in c if G.nodes[x]["type"]=="business"]
    print(f"\t Tamanho: {len(c)} sendo, usuários: {len(X)}, negócios: {len(Y)}")