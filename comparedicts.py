

def get_key_diffs(s1, s2):
    same_keys = s1.intersection(s2)
    keys_only_d1 = s1.difference(s2)
    keys_only_d2 = s2.difference(s1)

    return same_keys, keys_only_d1, keys_only_d2


def compare_list_of_dicts(d1, d2, d1_name, d2_name, same_keys, result):
    for main_k in same_keys:
        val1 = {k: i[k] for i in d1[main_k] for k in i}
        val2 = {k: i[k] for i in d2[main_k] for k in i}

        s1 = set(val1.keys())
        s2 = set(val2.keys())

        same_keys, keys_only_d1, keys_only_d2 = get_key_diffs(s1, s2)

        for k in s1.union(s2):
            new_key = f"{main_k}.{k}"
            if k in same_keys and val1[k] != val2[k]:
                result[new_key] = {d1_name: val1[k], d2_name: val2[k]}
            elif k in keys_only_d1:
                result[new_key] = {d1_name: val1[k], d2_name: 'null'}
            elif k in keys_only_d2:
                result[new_key] = {d1_name: 'null', d2_name: val2[k]}


def compare_nested_dicts(d1, d2, result, d1_name='dict1', d2_name='dict2'):
    """Takes two dictionaries and return a dictionary of differences"""

    s1 = set(d1.keys())
    s2 = set(d2.keys())

    same_keys, keys_only_d1, keys_only_d2 = get_key_diffs(s1, s2)

    for k in keys_only_d2:
        for i in d2[k]:
            for k1, v in i.items():
                new_key = f"{k}.{k1}"
                result[new_key] = {d1_name: "null", d2_name: v}

    for k in keys_only_d1:
        for i in d1[k]:
            for k1, v in i.items():
                new_key = f"{k}.{k1}"
                result[new_key] = {d2_name: "null", d1_name: v}

    compare_list_of_dicts(d1, d2, d1_name, d2_name, same_keys, result)

    return result


if __name__ == "__main__":
    # dict_1 = {"key1": "val1", "key2": "val2", "key4": "val4", "key6": [{"k10": "v13"}, {"k11": "v11"}]}
    # dict_2 = {"key1": "val1", "key2": "val2", "key4": "val4", "key6": [{"k10": "v5"}]}
    #
    dict_1 = {"Tom":[{"subject-1":"english"}],"Harry":[{"subject-1":"english"},{"subject-2":"maths"}, {"subject-3":"gym"}]}
    dict_2 = {"Tom":[{"subject-1":"english"}],"Harry":[{"subject-1":"english"},{"subject-2":"science"}],"Reggie":[{"subject-1":"maths"}]}
    result = {}
    print(compare_nested_dicts(dict_1, dict_2, result))
