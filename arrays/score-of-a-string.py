def scoreOfString(s: str):
    # extra space solution
    # ascii_scores = {char:ord(char) for char in s}
    result = 0
    
    for i in range(len(s)-1):
        # result += abs(ascii_scores[s[i]]-ascii_scores[s[i+1]])
        # w/o extra space
        result += abs(ord(s[i])-ord(s[i+1]))
    
    return result

res = scoreOfString('zaz')
print(res)
    