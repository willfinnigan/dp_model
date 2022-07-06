
def get_i_tagged_pop(dp_pop):
    i_tagged_pop = []
    for dp in dp_pop:
        if dp.is_i_tagged():
            i_tagged_pop.append(dp)
    return i_tagged_pop

def get_count_dict(i_tagged_pop):
    count_dict = {l: 0 for l in range(1, 8)}
    for dp in i_tagged_pop:
        count_dict[dp.num_units()] += 1
    return count_dict

