def compare_words(word_a: str, word_b: str):
    yes_not: str = 'not an' if sorted(word_a) != sorted(word_b) else 'an'
    print('This is ' + yes_not + ' anagram')


if __name__ == '__main__':
    compare_words('elvis', 'lives')
