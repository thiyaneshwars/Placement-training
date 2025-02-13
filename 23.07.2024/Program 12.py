def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while s[:len(prefix)] != prefix:
            prefix = prefix[:len(prefix) - 1]
            if not prefix:
                return ""
    return prefix
