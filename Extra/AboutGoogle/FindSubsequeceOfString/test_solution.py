"""
Pytest tests for LeetCode 792 - Number of Matching Subsequences.

Run with:
    pytest test_solution.py -v
"""

import pytest

from solution1 import is_subsequence, num_matching_subseq


# ---------------------------------------------------------------------------
# is_subsequence
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "word, s, expected",
    [
        ("ace", "abcde", True),
        ("bb", "abcde", False),
        ("", "abcde", True),
        ("", "", True),
        ("abcde", "abcde", True),
        ("abcdef", "abcde", False),
        ("aab", "aaab", True),
        ("aabb", "aab", False),
        ("cab", "abc", False),
    ],
)
def test_is_subsequence(word, s, expected):
    assert is_subsequence(word, s) is expected


# ---------------------------------------------------------------------------
# num_matching_subseq
# ---------------------------------------------------------------------------

def test_example_1():
    s = "abcde"
    words = ["a", "bb", "acd", "ace"]
    assert num_matching_subseq(s, words) == 3


def test_example_2():
    s = "dsahjpjauf"
    words = ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]
    assert num_matching_subseq(s, words) == 2


def test_no_matches():
    s = "abcde"
    words = ["xyz", "edcba", "ba"]
    assert num_matching_subseq(s, words) == 0


def test_all_match():
    s = "abcde"
    words = ["a", "ab", "abc", "abcd", "abcde", ""]
    assert num_matching_subseq(s, words) == 6


def test_empty_words_list():
    assert num_matching_subseq("abcde", []) == 0


def test_duplicate_words_each_counted():
    s = "abcde"
    words = ["a", "a", "a"]
    assert num_matching_subseq(s, words) == 3


def test_single_character_s():
    s = "a"
    words = ["a", "b", ""]
    assert num_matching_subseq(s, words) == 2


def test_word_longer_than_s_not_counted():
    s = "abc"
    words = ["abcd"]
    assert num_matching_subseq(s, words) == 0