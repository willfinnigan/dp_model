import random
import networkx as nx
from dp_model.dp_class import DP, DP_Pop


class Hydrolyzer():

    def __init__(self, hydrolysis_proba=1, weights=[0]):
        self.hydrolysis_proba = hydrolysis_proba
        self.default_weight = 1
        self.weights = weights

    def hydrolyse(self, dp):
        if self._can_not_hydrolyse(dp):
            return [dp]

        choices = [None] + dp.edges
        weights = self._assign_weights_to_choices(choices)
        edge_to_break = random.choices([None]+dp.edges, weights=weights)[0]
        new_dps = self._do_hydrolysis(dp, edge_to_break)
        return new_dps


    def hydrolyse_pop(self, dp_pop):
        new_pop = DP_Pop()
        for dp in dp_pop:
            new_pop += self.hydrolyse(dp)
        return new_pop

    def _do_hydrolysis(self, dp, edge_to_break):
        dp.graph.remove_edge(edge_to_break[0], edge_to_break[1])
        new_graphs = [dp.graph.subgraph(c).copy() for c in nx.connected_components(dp.graph)]

        new_dps = DP_Pop()
        for graph in new_graphs:
            new_dps.append(DP(graph))

        return new_dps

    def _assign_weights_to_choices(self, choices):
        weights = self.weights
        if len(weights) < len(choices):
            weights += [self.default_weight]*(len(choices)-len(self.weights))
        elif len(weights) > len(choices):
            weights = weights[0:len(choices)]

        return weights

    def _can_not_hydrolyse(self, dp):
        if len(dp.edges) == 0:
            return True
        elif random.uniform(0, 1) > self.hydrolysis_proba:
            return True

        return False



