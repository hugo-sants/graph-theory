import networkx as nx

def find_business(g: nx.MultiGraph, uid: str) -> list[str]:
    result = None

    if g is not None and uid is not None and g.has_node(uid):
        visited = set()
        queue = []
        all_businesses = set()

        visited.add(uid)
        queue.append(uid)

        user_businesses = set()

        for b in g.neighbors(uid):
            user_businesses.add(b)

        bfs_collect_businesses(g, queue, visited, all_businesses)

        final_list = []

        for b in all_businesses:
            if b not in user_businesses:
                final_list.append(b)

        result = final_list

    return result


def bfs_collect_businesses(g, queue, visited, business_set):
    while len(queue) > 0:
        user = queue.pop(0)

        for business in g.neighbors(user):
            if business not in visited:
                visited.add(business)
                business_set.add(business)

            for reviewer in g.neighbors(business):
                if reviewer not in visited:
                    visited.add(reviewer)
                    queue.append(reviewer)