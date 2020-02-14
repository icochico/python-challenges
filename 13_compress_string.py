
# aabcccccaaa -> a2b1c5a3
# 1. Go through the string and detect consecutive equal characters. 
# 2. Store count of the number of consecutive characters that are equal 
# 2. Generate a string that is the result of the initial scanning+ count 

def compress(text: str) -> str:

    count = 0
    compressed = ""
    char = ''
    for i in range(len(text)):
        if count == 0:
            char = text[i]
            count += 1
        elif char == text[i]:
            count += 1
        else:
            compressed += char + count
            count = 1
            char = text[i]
        
    compressed += char + count
    
    return compressed



