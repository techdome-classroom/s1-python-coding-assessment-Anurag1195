def decode_message(s: str, p: str) -> bool:
    memo = {}

    def match(i, j):
        if i == len(s) and j == len(p):
            return True
        if j == len(p):
            return False
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        # Handle the case where the current key character is `*`
        if j < len(p) and p[j] == '*':
            # Try two possibilities:
            # 1. `*` matches zero characters (move to the next key character)
            # 2. `*` matches at least one character (move to the next message character)
            if match(i, j + 1) or (i < len(s) and match(i + 1, j)):
                memo[(i, j)] = True
                return True
        
        # Handle the case where the current key character is `?`
        if i < len(s) and j < len(p) and (p[j] == '?' or p[j] == s[i]):
            if match(i + 1, j + 1):
                memo[(i, j)] = True
                return True
        
        # If no match, store False in the memo
        memo[(i, j)] = False
        return False

    # Start matching from the beginning of both the message and the key
    return match(0, 0)
