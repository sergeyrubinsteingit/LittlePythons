import sys


def compare_words(word_a: str, word_b: str):
    # Compares 2 words and produces 2 boolean lists
    # like [True, True, True, True, True,], [True, False, True, True, True,]
    # e.g.  [1, 1, 1, 1, 1,], [1, 0, 1, 1, 1,]
    match_1: list = [chars_ in word_a for chars_ in word_b]
    match_2: list = [chars_ in word_b for chars_ in word_a]
    # Summarizes contents of aforesaid lists
    # and compares the results with one of the
    # word's length; in case of equality between them
    # the expressions are anagrams, otherwise they're not.
    is_isnot: str = 'not an' if sum(match_1) != len(word_a) or sum(match_2 ) != len(word_a) else 'an'  # Sets a correct
    # joint for the answer sentence.
    print('This is ' + is_isnot + ' anagram.')     # Prints the result to console.
    sys.exit(0)


if __name__ == '__main__':
    compare_words('elvis', 'lives')
