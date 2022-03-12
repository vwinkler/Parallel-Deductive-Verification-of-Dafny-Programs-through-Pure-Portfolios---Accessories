from itertools import product


def expand(dict_tree):
    if isinstance(dict_tree, dict):
        return expand_dict(dict_tree)
    elif isinstance(dict_tree, list):
        return [expanded_value for value in dict_tree for expanded_value in expand(value)]
    else:
        return [dict_tree]


def expand_dict(dict_to_expand):
    keys = dict_to_expand.keys()
    values = dict_to_expand.values()
    expanded_values = [expand(v) for v in values]
    value_combinations = product(*expanded_values)
    return [dict(zip(keys, vc)) for vc in value_combinations]
