 # -*- coding: utf-8 -*-
import re
from unidecode import unidecode

phrases_: list = [
    125, 676,
    r"Was it a cat I saw?",
    r"À l'étape, épate-la !",
    r"The sooner the better...",
]
for ix_, phrase_ in enumerate(phrases_):
    phrase_ = str(phrase_) # Converts non-string to string
    print('A phrase to verify: ' + str(phrase_))
    phrase_ = unidecode(phrase_, 'utf-8')  # Replaces non-English characters with English ones
    phrase_ = re.compile('[^a-zA-Z0-9]').sub('', phrase_).lower()   # Converts an expression to string
    # without spaces in, using Regex. Converts to lowercase : IMPORTANT!
    is_isnot: str = ' is not' if str(phrase_) != str(phrase_)[::-1] else ' is' # Compares between
                                # this string and its reversed version; sets a joint for resulting sentence.
    print('"' + str(phrases_[ix_]) + '"' + is_isnot + f' a palindrome\n') # Prints the answer to console.
