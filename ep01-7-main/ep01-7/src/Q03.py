import networkx as nx

def intergraph_users (g1, g2):
    returnGraph = None

    if g1 is not None and g2 is not None:
        users_g1 = {n for n, d in g1.nodes(data=True) if d.get("type") == "user"}
        users_g2 = {n for n, d in g2.nodes(data=True) if d.get("type") == "user"}

        if users_g1 and users_g2:
            returnGraph = nx.Graph()
            
            common_users = users_g1 & users_g2

            for u in common_users:
                returnGraph.add_node(u, **g1.nodes[u])

            add_user_business_edges(g1, common_users, returnGraph)
            add_user_business_edges(g2, common_users, returnGraph)

    return returnGraph

def add_user_business_edges(source_graph, common_users, returnGraph):
    for user in common_users:
        for business in source_graph.neighbors(user):
            if business not in returnGraph:
                returnGraph.add_node(business, **source_graph.nodes[business])
            
            returnGraph.add_edge(user, business)
    return None