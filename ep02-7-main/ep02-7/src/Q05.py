import networkx as nx
import statistics
from typing import Any

def business_polarization(g: nx.MultiGraph, b: Any) -> float:
    result = None

    if is_valid_polarization(g, b):
        Upos, Uneg = split_users_by_review(g, b)

        if len(Upos) == 0 and len(Uneg) == 0:
            result = 0.0

        elif len(Upos) == 0 or len(Uneg) == 0:
            result = 0.0

        else:
            U_total = merge_sets(Upos, Uneg)

            induced = build_induced_graph(g, U_total, b)

            mi_pos = compute_mean(Upos)
            mi_neg = compute_mean(Uneg)

            Etotal, Ecross = count_edges(induced, Upos, Uneg)

            result = compute_polarization(mi_pos, mi_neg, Etotal, Ecross)

    return result


def is_valid_polarization(g, b):
    if g is None:
        return False
    if b is None:
        return False
    if len(g.nodes) == 0:
        return False
    if not g.has_node(b):
        return False

    return True


def split_users_by_review(g, b):
    Upos = {}
    Uneg = {}

    for user in g.neighbors(b):
        for key in g[user][b]:
            rating = g[user][b][key].get("review_stars")

            if rating >= 4:
                Upos[user] = rating
            elif rating <= 2:
                Uneg[user] = rating

    return Upos, Uneg


def merge_sets(Upos, Uneg):
    result = set()

    for u in Upos:
        result.add(u)

    for u in Uneg:
        result.add(u)

    return result


def build_induced_graph(g, users, b):
    G = nx.Graph()

    for u in users:
        G.add_node(u)

    user_business = {}

    for u in users:
        businesses = set()

        for n in g.neighbors(u):
            if n != b:
                businesses.add(n)

        user_business[u] = businesses

    user_list = list(users)
    n = len(user_list)

    for i in range(n):
        for j in range(i + 1, n):
            u1 = user_list[i]
            u2 = user_list[j]

            if not user_business[u1].isdisjoint(user_business[u2]):
                G.add_edge(u1, u2)

    return G


def compute_mean(d):
    if len(d) == 0:
        return 0.0

    values = []

    for v in d.values():
        values.append(v)

    return statistics.mean(values)


def count_edges(G, Upos, Uneg):
    Etotal = G.number_of_edges()
    Ecross = 0

    for u, v in G.edges():
        if (u in Upos and v in Uneg) or (u in Uneg and v in Upos):
            Ecross += 1

    return Etotal, Ecross


def compute_polarization(mi_pos, mi_neg, Etotal, Ecross):
    diff = abs(mi_pos - mi_neg)

    if Etotal > 0:
        factor = 1.0 - (Ecross / Etotal)
    else:
        factor = 1.0

    return round((factor * diff) / 5.0, 2)