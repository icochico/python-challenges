# Given a string s, detect if it's palindrome
# A string is palindrome when reading it forward or backwards results in the same sequence of characters
# e.g. "abba", "civic", "radar"

# Requirements
# - Assume the strings in input can have arbitrary length
# - Assume no spaces
# - Assume lowercase and uppercase characters are the same letter

# solution in O(n) time
def is_palindrome_1(s: str) -> bool:

    # sanitiziation
    s = s.lower()

    # create reverse of the string
    s_rev = s[::-1]

    return s == s_rev

# alternative solution in O(n) time
def is_palindrome_2(s: str) -> bool:

    # sanitiziation
    s = s.lower()

    for i in range(len(s)):
        if s[i] != s[len(s)-1-i]:
            return False
    
    return True
if __name__ == '__main__':
    print(is_palindrome_1("abba"))
    print(is_palindrome_1("radar"))
    print(is_palindrome_1("cactus"))
    print(is_palindrome_2("abba"))
    print(is_palindrome_2("radar"))
    print(is_palindrome_2("cactus"))



