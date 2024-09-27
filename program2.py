class Solution:
    def isMatch(self, message: str, key: str) -> bool:
        memo = {}
        
        def match(i, j):
            # If we've reached the end of both the message and the key, it's a match
            if i == len(message) and j == len(key):
                return True
            # If we've reached the end of the key but not the message, or vice versa, it's not a match
            if j == len(key):
                return False
            
            # If this state has been computed before, return it from the memo
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Handle the case where the current key character is `*`
            if j < len(key) and key[j] == '*':
                # Try two possibilities:
                # 1. `*` matches zero characters (move to the next key character)
                # 2. `*` matches at least one character (move to the next message character)
                if match(i, j + 1) or (i < len(message) and match(i + 1, j)):
                    memo[(i, j)] = True
                    return True
            
            # Handle the case where the current key character is `?`
            if i < len(message) and j < len(key) and (key[j] == '?' or key[j] == message[i]):
                if match(i + 1, j + 1):
                    memo[(i, j)] = True
                    return True
            
            # If no match, store False in the memo
            memo[(i, j)] = False
            return False
        
        # Start matching from the beginning of both the message and the key
        return match(0, 0)
