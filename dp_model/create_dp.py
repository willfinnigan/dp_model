import networkx as nx
from dp_model.dp_class import DP, Unit, DP_Pop


def create_dp_pop(unit_str_list, num, i_tag_str='I-'):
    dp_pop = DP_Pop()
    for i in range(num):
        dp = create_dp(unit_str_list, i_tag_str=i_tag_str)
        dp_pop.append(dp)
    return dp_pop

def create_dp(unit_str_list, i_tag_str='I-'):
    unit_list = _create_units(unit_str_list, i_tag_str)
    graph = _create_graph(unit_list)
    dp = DP(graph)
    return dp

def _create_graph(unit_list):
    graph = nx.Graph()
    for unit in unit_list:
        graph.add_node(unit)

    if len(graph.nodes) >= 2:
        for i in range(len(unit_list) - 1):
            graph.add_edge(unit_list[i], unit_list[i + 1])
    return graph

def _create_units(unit_str_list, i_tag_str):
    unit_list = []
    for unit_str in unit_str_list:
        if i_tag_str in unit_str:
            unit = Unit(unit_str, i_tagged=True)
        else:
            unit = Unit(unit_str)
        unit_list.append(unit)
    return unit_list