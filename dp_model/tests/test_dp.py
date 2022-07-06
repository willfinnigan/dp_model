import networkx as nx
import pytest

from dp_model.create_dp import create_dp
from dp_model.hydrolyze import Hydrolyzer


class TestDP():

    def test_dp_unit_is_nodes_in_graph(self):
        unit_str_list = ['G']
        dp = create_dp(unit_str_list)
        assert 'G' in list(dp.graph.nodes)[0].name

    def test_dp_multiple_units_of_same_name_are_different_nodes_in_graph(self):
        unit_str_list = ['G', 'G']
        dp = create_dp(unit_str_list)
        assert list(dp.graph.nodes)[0] != list(dp.graph.nodes)[1]

    def test_there_are_edges_between_nodes(self):
        unit_str_list = ['G', 'G']
        dp = create_dp(unit_str_list)
        edge = list(dp.graph.edges)[0]
        assert [edge[0].name, edge[1].name] == unit_str_list

    def test_can_create_7dp(self):
        unit_str_list = ['I-G', 'G', 'G', 'G', 'G', 'G', 'G']
        dp = create_dp(unit_str_list)
        assert len(dp.graph.nodes) == 7


class TestHydrolyzer():

    def test_weights_created_as_defaults(self):
        hydrolyzer = Hydrolyzer()
        weights = hydrolyzer._assign_weights_to_choices([None, 1,2,3,4,5])
        assert weights == [0, 1, 1, 1, 1, 1]

    def test_weights_combine_default_with_set(self):
        hydrolyzer = Hydrolyzer(weights=[0, 2, 3])
        weights = hydrolyzer._assign_weights_to_choices([None, 1,2,3,4,5])
        assert weights == [0 ,2, 3, 1, 1, 1]

    def test_hydrolysis_chance_3_to_2_and_1(self):
        hydrolyzer = Hydrolyzer(weights=[0, 1, 0, 0])
        dp = create_dp(['I-G', 'G', 'G'])
        new_dps = hydrolyzer.hydrolyse(dp)
        assert [len(new_dps[0].graph.nodes), len(new_dps[1].graph.nodes)] == [1, 2]

    def test_hydrolysis_chance_3_to_1_and_2(self):
        hydrolyzer = Hydrolyzer(weights=[0, 0, 1, 0])
        dp = create_dp(['I-G', 'G', 'G'])
        new_dps = hydrolyzer.hydrolyse(dp)
        assert [len(new_dps[0].graph.nodes), len(new_dps[1].graph.nodes)] == [2, 1]

    def test_hydrolysis_of_1_gives_1(self):
        hydrolyzer = Hydrolyzer()
        dp = create_dp(['I-G'])
        new_dps = hydrolyzer.hydrolyse(dp)
        assert [len(new_dps[0].graph.nodes)] == [1]






