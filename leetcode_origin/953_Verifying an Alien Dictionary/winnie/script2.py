class Solution:
    def isAlienSorted(self, words, order) -> bool:
        def compareTwo(word1, word2):
            for minor in range(min(len(word1), (len(word2)))):
                if d[word1[minor]] > d[word2[minor]]:
                    break
                elif d[word1[minor]] < d[word2[minor]]:
                    return False

            if word1.startswith(word2):
                return False
            else:
                return True

        d = {}
        for index, c in enumerate(order):
            d[c] = index

        for major in range(1, len(words)):
            return compareTwo(words[major - 1], words[major])


# print(isAlienSorted(words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz"))
# print(isAlienSorted(words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"))
# print(isAlienSorted(words=["apap", "app"], order="abcdefghijklmnopqrstuvwxyz"))
print(Solution().isAlienSorted(
    words=["fxasxpc", "dfbdrifhp", "nwzgs", "cmwqriv", "ebulyfyve", "miracx", "sxckdwzv", "dtijzluhts", "wwbmnge",
           "qmjwymmyox"],
    order="zkgwaverfimqxbnctdplsjyohu"))
