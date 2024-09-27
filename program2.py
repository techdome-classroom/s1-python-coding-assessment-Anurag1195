def decode_message(s: str, p: str) -> bool:
    memo = {}

    def match(i, j):
        if i == len(s) and j == len(p):
            return True
        if j == len(p):
            return False
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        if j < len(p) and p[j] == '*':
            if match(i, j + 1) or (i < len(s) and match(i + 1, j)):
                memo[(i, j)] = True
                return True
        
        if i < len(s) and j < len(p) and (p[j] == '?' or p[j] == s[i]):
            if match(i + 1, j + 1):
                memo[(i, j)] = True
                return True
        
        memo[(i, j)] = False
        return False

    return match(0, 0)
