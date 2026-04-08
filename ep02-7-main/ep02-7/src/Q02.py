import networkx as nx
from src.Q01 import weighted_user_graph

def critical_users(g: nx.MultiGraph) -> dict[str, int]:
    result = None

    if is_valid_graph(g):
        user_graph = weighted_user_graph(g)

        if is_valid_user_graph(user_graph):
            critical_nodes = get_articulation_points(user_graph)

            if len(critical_nodes) > 0:
                result_dict = {}

                for user in critical_nodes:
                    weight = sum_edge_weights(user_graph, user)
                    result_dict[user] = weight

                result = result_dict
            else:
                result = {}

    return result


def is_valid_graph(g):
    if g is None:
        return False
    if len(g.edges) == 0:
        return False
    return True


def is_valid_user_graph(g):
    if g is None:
        return False
    if len(g.nodes) == 0:
        return False
    return True


def get_articulation_points(g):
    result = set()

    for node in nx.articulation_points(g):
        result.add(node)

    return result


def sum_edge_weights(g, user):
    total = 0

    for neighbor in g.neighbors(user):
        total += g[user][neighbor]['weight']

    return total