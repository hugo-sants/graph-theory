import networkx as nx
from itertools import combinations

def dense_biclique(g: nx.MultiGraph, u: int, b: int) -> list[tuple[set, set]]:
    result = None

    if is_valid_dense(g, u, b):
        users = get_users(g)
        user_business = map_user_business(g, users)

        result_list = []

        user_groups = list(combinations(users, u))

        for group in user_groups:
            common_business = get_common_business(group, user_business)

            if len(common_business) >= b:
                add_bicliques(group, common_business, b, result_list)

        result = result_list

    return result


def is_valid_dense(g, u, b):
    if g is None:
        return False
    if g.number_of_nodes() == 0:
        return False
    if u is None or b is None:
        return False
    if u <= 0 or b <= 0:
        return False
    return True


def get_users(g):
    users = set()

    for node, data in g.nodes(data=True):
        if data.get("type") == "user":
            users.add(node)

    return users


def map_user_business(g, users):
    mapping = {}

    for user in users:
        businesses = set()

        for n in g.neighbors(user):
            businesses.add(n)

        mapping[user] = businesses

    return mapping


def get_common_business(group, mapping):
    common = None

    for user in group:
        if common is None:
            common = mapping[user].copy()
        else:
            common = common.intersection(mapping[user])

    return common


def add_bicliques(group, common_business, b, result):
    business_groups = list(combinations(common_business, b))

    for bg in business_groups:
        result.append((set(group), set(bg)))