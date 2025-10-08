def group_anagrams(strs):
    groups = dict()

    for i in strs:
        key = "".join(sorted(i))
        if key not in groups:
            groups[key] = []
        groups[key].append(i)

    return groups.values()
