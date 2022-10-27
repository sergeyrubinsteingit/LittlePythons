# -*- coding: utf-8 -*-
import re
from unidecode import unidecode

phrases_: list = [
    125, 282,
    r"Was it a cat I saw?",
    r"À l'étape, épate-la !",
    r"The sooner the better...",
]
for ix_, phrase_ in enumerate(phrases_):
    phrase_ = unidecode(phrase_.__str__(),'utf-8') # Replaces non-English characters with English ones. Converts to
    # string.
    phrase_ = re.compile('[^a-zA-Z0-9]').sub('', phrase_).lower() # Removes everything but letters and digits;
    # Converts to lowercase : IMPORTANT!
    for letter_ in range(0, phrase_.__len__()-1):
        if phrase_[0] != phrase_[int(phrase_.__len__()-1)]: # Search for the 1st mismatch between the characters in
            # string.
            break # If found, breaks the loop.
        else:
            phrase_.replace(phrase_[0], '') # Deletes first character in the string.
            phrase_.replace(phrase_[int(phrase_.__len__() - 1)], '') # Deletes last character.
    is_isnot_: str = ' is a ' if phrase_[0] == phrase_[int(phrase_.__len__() - 1)] else ' is not a ' # Sets a correct
    # joint for the answer sentence.
    print(str(phrases_[ix_]) + is_isnot_ + r'palindrome') # Prints the answer.
