import networkx as nx

def weighted_user_graph(g: nx.MultiGraph) -> nx.Graph:
    returnGraph = None

    if g is not None and len(g.edges) > 0:
        G = nx.Graph()
        business_to_users = {}

        for u, v, data in g.edges(data=True):
            if data.get('type') != 'review':
                continue

            user, business = get_user_business(g, u, v)
            if user is None:
                continue

            if business not in business_to_users:
                business_to_users[business] = set()

            business_to_users[business].add(user)

        if len(business_to_users) > 0:
            for business in business_to_users:
                for user in business_to_users[business]:
                    G.add_node(user)

            edge_weights = {}

            for business in business_to_users:
                add_pair_weights(business_to_users[business], edge_weights)

            for (u1, u2), weight in edge_weights.items():
                G.add_edge(u1, u2, weight=weight)

            returnGraph = G

    return returnGraph


"""
    Retorna user e business a partir de uma aresta
"""
def get_user_business(g, u, v):
    user = None
    business = None

    if g.nodes[u].get('type') == 'user' and g.nodes[v].get('type') == 'business':
        user = u
        business = v
    elif g.nodes[v].get('type') == 'user' and g.nodes[u].get('type') == 'business':
        user = v
        business = u

    return user, business

"""
    Atualiza os pesos das arestas
"""
def add_pair_weights(users, edge_weights):
    users = list(users)
    n = len(users)

    for i in range(n - 1):
        for j in range(i + 1, n):
            u1 = users[i]
            u2 = users[j]

            if u1 > u2:
                u1, u2 = u2, u1
            if (u1, u2) not in edge_weights:
                edge_weights[(u1, u2)] = 0

            edge_weights[(u1, u2)] += 1
    return None