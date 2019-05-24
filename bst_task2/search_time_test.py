import random
import time
from linkedbst import LinkedBST
import sys


def form_dict(filename):
    """
    Returns dictionary from file as a list.
    :param filename:
    :return:
    """
    with open(filename, 'r', encoding="utf-8", errors="ignore") as f:
        words_dict = [word.strip() for word in f]
    return words_dict


def form_random_words(word_dict):
    """
    Returns lost of 10000 random words from dict
    :param word_dict: list
    :return: list
    """
    random_words = []
    for x in range(10000):
        rnd_word = random.choice(word_dict)
        random_words.append(rnd_word)
    return random_words


def search_list(dictionary, words_set):
    """
    Returns time of searching set of words in dictionary.
    :param dictionary: list
    :param words_set: set
    :return: float
    """
    start = time.time()
    for word in words_set:
        if word in dictionary:
            continue
    return time.time() - start


def search_bts(tree, words_set):
    """
    Returns time of searching set of words in unbalansed binary search tree.
    :param tree: LinkedBST
    :param words_set: set
    :return: float
    """
    start = time.time()
    for word in words_set:
        tree.find(word)
    return time.time() - start


def search_balanced_bts(tree, words_set):
    """
    Returns time of searching set of words in balansed binary search tree.
    :param tree: LinkedBST
    :param words_set: set
    :return: float
    """
    tree.rebalance()
    start = time.time()
    for word in words_set:
        tree.find(word)
    return time.time() - start


def main():
    """
    Running the functions for research
    """
    sys.setrecursionlimit(10000)
    diction = form_dict('words.txt')
    rand_set = form_random_words(diction)
    bst = LinkedBST()
    for item in set(diction):
        bst.add(item)
    print('Time for search in list: ')
    print(search_list(diction, rand_set))
    print('Time for search in unbalanced binary search tree: ')
    print(search_bts(bst, rand_set))
    print('Time for search in balanced binary search tree: ')
    print(search_balanced_bts(bst, rand_set))


if __name__ == '__main__':
    main()