class Solution:
    def isMatch(self, message: str, key: str) -> bool:
        memo = {}
        
        def match(i, j):
            if i == len(message) and j == len(key):
                return True
           
            if j == len(key):
                return False
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            if j < len(key) and key[j] == '*':
                if match(i, j + 1) or (i < len(message) and match(i + 1, j)):
                    memo[(i, j)] = True
                    return True
            
           
            if i < len(message) and j < len(key) and (key[j] == '?' or key[j] == message[i]):
                if match(i + 1, j + 1):
                    memo[(i, j)] = True
                    return True
            
            memo[(i, j)] = False
            return False
        
        return match(0, 0)
