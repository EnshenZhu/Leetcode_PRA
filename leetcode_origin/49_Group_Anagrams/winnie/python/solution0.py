def groupAnagrams(strs):
    word_instance_collection = []
    output_ls = []

    for item in strs:
        word_instance_collection.append(Word(item))

    return output_ls


class Word:
    def __init__(self, word):
        self.component = set(word)
        self.cluster_idx = None

    def set_cluster_idx(self, cluster_idx):
        self.cluster_idx = cluster_idx


# print(groupAnagrams("xxx"))

money = Word("money")
# money.set_cluster_idx((1))

print(money.component)
