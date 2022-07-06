from dp_model.create_dp import create_dp_pop
from dp_model.hydrolyze import Hydrolyzer

def run_simulation(initial_dp_str, rounds, pop_num, i_tag_str='I-', hydrolysis_proba=1, weights=[0, 1, 1, 1, 1, 1, 1]):
    dp_pop = create_dp_pop(initial_dp_str, pop_num, i_tag_str=i_tag_str)
    hydrolyser = Hydrolyzer(hydrolysis_proba=hydrolysis_proba, weights=weights)
    # default behaviour is prob for doing hydrolysis is 1, and 0 chance of no edge being selected.

    for i in range(rounds):
        dp_pop = hydrolyser.hydrolyse_pop(dp_pop)
        i_tagged_pop = dp_pop.get_i_tagged_pop()
        count_dict = i_tagged_pop.get_count_dict()
        print(f"Round {i + 1}: {count_dict}")


if __name__ == '__main__':
    pop_num = 10000
    rounds = 5
    initial_dp_str = ['I-G', 'G', 'G', 'G', 'G', 'G', 'G']

    run_simulation(initial_dp_str, rounds, pop_num, hydrolysis_proba=1, weights=[0, 1, 1, 1, 1, 1, 1, 1])
