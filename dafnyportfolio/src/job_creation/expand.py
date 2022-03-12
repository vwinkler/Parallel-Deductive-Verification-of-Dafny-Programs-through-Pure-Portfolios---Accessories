from itertools import product


def expand(dict_tree):
    if isinstance(dict_tree, dict):
        return expand_dict(dict_tree)
    elif isinstance(dict_tree, list):
        return [expanded_value for value in dict_tree for expanded_value in expand(value)]
    else:
        return [dict_tree]


def process(dict_tree):
    dict_tree = expand(dict_tree)
    dict_tree = resolve_includes(dict_tree)
    return dict_tree

def expand_dict(dict_to_expand):
    keys = dict_to_expand.keys()
    values = dict_to_expand.values()
    expanded_values = [expand(v) for v in values]
    value_combinations = product(*expanded_values)
    return [dict(zip(keys, vc)) for vc in value_combinations]


def resolve_includes(dict_tree):
    if isinstance(dict_tree, dict):
        return resolve_includes_in_dict(dict_tree)
    elif isinstance(dict_tree, list):
        return [resolve_includes(v) for v in dict_tree]
    else:
        return dict_tree


def resolve_includes_in_dict(dict_tree):
    result = {k: resolve_includes(v) for k, v in dict_tree.items()}
    for key, value in dict_tree.items():
        if key.startswith("[include]"):
            assert isinstance(value, dict)
            for inner_key, inner_value in value.items():
                result[inner_key] = inner_value
            del result[key]
    return result
