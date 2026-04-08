import networkx as nx

def recommendation_capacity(g: nx.Graph, U: list, B: list) -> float:
    result = None

    if is_valid_recommendation(g, U, B):
        users = set(U)
        businesses = set(B)

        total = 0

        for user in users:
            capacity = compute_user_capacity(g, user, users, businesses)
            total += capacity

        result = round(total / len(users), 2)

    return result


def is_valid_recommendation(g, U, B):
    if g is None or U is None or B is None:
        return False
    if len(g.nodes) == 0:
        return False
    if len(set(U)) == 0 or len(set(B)) == 0:
        return False

    for u in set(U):
        if u not in g:
            return False

    for b in set(B):
        if b not in g:
            return False

    return True


def compute_user_capacity(g, user, users, businesses):
    user_business = get_user_business_subset(g, user, businesses)
    neighbors = get_neighbor_users(g, user_business, users, user)
    candidates = get_candidate_business(g, neighbors, businesses)

    final_candidates = set()

    for b in candidates:
        if b not in user_business:
            final_candidates.add(b)

    return len(final_candidates) / len(businesses)


def get_user_business_subset(g, user, businesses):
    result = set()

    for n in g.neighbors(user):
        if n in businesses:
            result.add(n)

    return result


def get_neighbor_users(g, user_business, users, original_user):
    result = set()

    for b in user_business:
        for u in g.neighbors(b):
            if u in users and u != original_user:
                result.add(u)

    return result


def get_candidate_business(g, neighbors, businesses):
    result = set()

    for u in neighbors:
        for b in g.neighbors(u):
            if b in businesses:
                result.add(b)

    return result