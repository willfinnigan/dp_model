class Unit:
    def __init__(self, name, i_tagged=False):
        self.name = name
        self.i_tagged = i_tagged

    def __repr__(self):
        return self.name


class DP():
    def __init__(self, graph):
        self.graph = graph
        self.edges = list(self.graph.edges)

    def is_i_tagged(self):
        for node in self.graph.nodes:
            if node.i_tagged is True:
                return True
        return False

    def num_units(self):
        return len(self.graph.nodes)

    def __repr__(self):
        return f"Dp-{self.num_units()}"


class DP_Pop(list):

    def get_i_tagged_pop(self):
        i_tagged_pop = DP_Pop()
        for dp in self:
            if dp.is_i_tagged():
                i_tagged_pop.append(dp)
        return i_tagged_pop

    def get_count_dict(self):
        count_dict = {l: 0 for l in range(1, 8)}
        for dp in self:
            count_dict[dp.num_units()] += 1
        return count_dict



