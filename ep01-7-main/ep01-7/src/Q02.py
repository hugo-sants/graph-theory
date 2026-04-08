import networkx as nx

def get_business(g: nx.MultiGraph) -> dict[str, list[str]]:
    result = None

    if g is not None and g.number_of_nodes() != 0:
        result = {}

        business_nodes = get_business_nodes_with_attrs(g)

        for node, attrs in business_nodes:
            add_business_to_city(node, attrs, result)

    return result


def get_business_nodes_with_attrs(g: nx.Graph):
    result = []

    for node, data in g.nodes(data=True):
        if data.get("type") == "business":
            result.append((node, data))

    return result


def add_business_to_city(node: str, attrs: dict, result: dict) -> None:
    city = attrs.get("city")

    if city not in result:
        result[city] = []

    result[city].append(node)