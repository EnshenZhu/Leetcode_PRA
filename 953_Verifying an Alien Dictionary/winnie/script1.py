def isAlienSorted(words, order) -> bool:
    d = {}
    for index, c in enumerate(order):
        d[c] = index

    for major in range(1, len(words)):
        for minor in range(min(len(words[major]), len(words[major - 1]))):
            if d[words[major][minor]] > d[words[major - 1][minor]]:
                break
            elif d[words[major][minor]] < d[words[major - 1][minor]]:
                return False

        if len(words[major]) < len(words[major - 1]):
            return False

    return True


# print(isAlienSorted(words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz"))
# print(isAlienSorted(words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"))
# print(isAlienSorted(words=["apap", "app"], order="abcdefghijklmnopqrstuvwxyz"))
print(isAlienSorted(
    words=["fxasxpc", "dfbdrifhp", "nwzgs", "cmwqriv", "ebulyfyve", "miracx", "sxckdwzv", "dtijzluhts", "wwbmnge",
           "qmjwymmyox"],
    order="zkgwaverfimqxbnctdplsjyohu"))
