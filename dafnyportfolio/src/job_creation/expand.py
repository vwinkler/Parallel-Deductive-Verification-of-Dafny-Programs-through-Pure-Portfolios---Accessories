import re
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
    return combine_all_value_options_of_dict(expand_values_of_dict(dict_to_expand))


def expand_value_if_allowed(k, v):
    return [v] if k.startswith("[noexpand]") else expand(v)


def expand_values_of_dict(dict_to_expand):
    result = {}

    for k, v in dict_to_expand.items():
        k, v = expand_key_value_pair(k, v)
        result[k] = v

    return result


def expand_key_value_pair(original_key, original_value):
    search_result = search_for_expand_directive(original_key)
    if has_match(search_result):
        new_key = get_key_without_expand_directive(search_result)
        new_value = [expand(original_value)]
    else:
        new_key = original_key
        new_value = expand(original_value)
    return new_key, new_value


def get_key_without_expand_directive(search_result):
    return search_result.group(1)


def search_for_expand_directive(k):
    return re.search("^\[noexpand\](.*)$", k)


def has_match(match):
    return match is not None


def combine_all_value_options_of_dict(dict_with_expanded_values):
    keys = dict_with_expanded_values.keys()
    values = dict_with_expanded_values.values()
    value_combinations = product(*values)
    return [dict(zip(keys, vc)) for vc in value_combinations]


def resolve_includes(dict_tree):
    if isinstance(dict_tree, dict):
        return resolve_includes_in_dict(dict_tree)
    elif isinstance(dict_tree, list):
        return [resolve_includes(v) for v in dict_tree]
    else:
        return dict_tree


def resolve_includes_in_dict(dict_tree):
    return resolve_includes_in_dict_keep_values(resolve_includes_in_dict_values(dict_tree))


def resolve_includes_in_dict_values(dict_tree):
    dict_with_resolved_values = {k: resolve_includes(v) for k, v in dict_tree.items()}
    return dict_with_resolved_values


def resolve_includes_in_dict_keep_values(dict_with_resolved_values):
    result = dict()
    for key, value in dict_with_resolved_values.items():
        if key.startswith("[include]"):
            assert isinstance(value, dict)
            for inner_key, inner_value in value.items():
                result[inner_key] = inner_value
        else:
            if key not in result:
                result[key] = value
    return result
