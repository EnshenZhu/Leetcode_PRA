def is_subsequence(single_word: str, target_string: str) -> bool:
    i = 0
    for char in target_string:
        if i < len(single_word) and char == single_word[i]:
            i += 1
    return i == len(single_word)


def num_matching_subseq(s: str, words: list[str]) -> int:
    count = 0
    for word in words:
        if is_subsequence(word, s):
            count += 1
    return count
