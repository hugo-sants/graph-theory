from itertools import combinations
import networkx as nx

def co_reviewers(g: nx.Graph) -> nx.MultiGraph:
    returnGraph = None

    if g is not None:
        users = get_users(g)

        if len(users) > 0:
            returnGraph = nx.MultiGraph()
            add_users_to_graph(users, returnGraph)

            businesses = get_business_nodes(g)

            for business in businesses:
                reviewers = get_reviewers(g, business)

                if len(reviewers) >= 2:
                    add_co_review_edges(reviewers, business, returnGraph)

            if len(returnGraph) == 0:
                returnGraph = None

    return returnGraph


def get_users(g: nx.Graph) -> set:
    users = set()

    for node, data in g.nodes(data=True):
        if data.get("type") == "user":
            users.add(node)

    return users


def get_business_nodes(g: nx.Graph) -> list:
    businesses = []

    for node, data in g.nodes(data=True):
        if data.get("type") == "business":
            businesses.append(node)

    return businesses


def get_reviewers(g: nx.Graph, business: str) -> list:
    reviewers = []

    for neighbor in g.neighbors(business):
        if g.nodes[neighbor].get("type") == "user":
            reviewers.append(neighbor)

    return reviewers


def add_users_to_graph(users: set, g: nx.MultiGraph) -> None:
    for user in users:
        g.add_node(user)


def add_co_review_edges(reviewers: list, business: str, g: nx.MultiGraph) -> None:
    for user1, user2 in combinations(reviewers, 2):
        g.add_edge(user1, user2, business=business)