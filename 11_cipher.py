# A substitution cipher is a simple way to obfuscate a string by replacing the letters 
# given a mapping. Each letter in the cipher replaces the corresponding letter in the 
# alphabet (i.e. m replaces occurrences of a, p replaes occurrences of b. etc.)
# So a word like "abs" becomes mpu

import string
from collections import Counter

def has_dup(input: str) -> bool:
    count = Counter(input)
    for key in count:
        if count[key] > 1:
            return True
        
def solution(word, cipher):
    
    # original alphabet
    alphabet = string.ascii_lowercase
    
    # validate input 
    if len(cipher) != len(alphabet):
        return ""
    
    # check duplicate letters in cipher
    if has_dup(cipher):
        return ""
    
    enc_word = ""
    for c in word:
        
         if c not in alphabet:
                return ""
        
         idx = alphabet.index(c)
         match = cipher[idx]
         enc_word += match
    
    return enc_word