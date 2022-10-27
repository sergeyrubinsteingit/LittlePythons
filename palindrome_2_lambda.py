# -*- coding: utf-8 -*-
from unidecode import unidecode

verify_palindrome = lambda the_phrase_: the_phrase_ == the_phrase_[::-1]

phrases_: list = [
    53.35, 125,
    r"Was it a cat I saw?",
    r"À l'étape, épate-la !",
    r"The sooner the better...",
]
for ix_, phrase_ in enumerate(phrases_):
    phrase_ = '%s' % phrase_ # Converts to string.
    phrase_ = unidecode(phrase_, 'utf-8') # Replaces non-English characters with English ones.
    phrase_ = ''.join(chrt_ for chrt_ in phrase_ if chrt_.isalpha() or chrt_.isnumeric()).lower() # Removes
                                                            # everything but letters and digits from string.
    is_isnot: str = ' is' if verify_palindrome(phrase_) else ' is not' # Sets a suitable join for the resulting message.
    print(str(phrases_[ix_]) + is_isnot + ' a palindrome')
