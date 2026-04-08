import networkx as nx

def business_graph(g: nx.MultiGraph, category='') -> nx.Graph:
    returnGraph = None

    if g is not None and len(g) > 0 and category is not None:
        returnGraph = nx.Graph()

        valid_nodes = get_business_by_category(g, category)

        add_nodes_with_attrs(g, valid_nodes, returnGraph)
        connect_related_businesses(g, valid_nodes, returnGraph)

    return returnGraph


def get_business_by_category(g: nx.Graph, category: str) -> list:
    result = []

    for node, attrs in g.nodes(data=True):
        categories = attrs.get("categories")

        if categories is not None:
            if category == '' or category in categories:
                result.append(node)

    return result


def add_nodes_with_attrs(source, nodes, target):
    for node in nodes:
        target.add_node(node, **source.nodes[node])


def connect_related_businesses(g, businesses, returnGraph):
    for b1 in businesses:
        for user in g.neighbors(b1):
            for b2 in g.neighbors(user):
                if b2 != b1:
                    if returnGraph.has_node(b2):
                        returnGraph.add_edge(b1, b2)