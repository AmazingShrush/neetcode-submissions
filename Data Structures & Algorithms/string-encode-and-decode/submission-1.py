class Solution:

    def encode(self, strs: List[str]) -> str:
        deli='#'
        encoded=''
        for i in range(len(strs)):
            encoded += str(len(strs[i]))+deli+strs[i]
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        
        while i < len(s):
            # Find the delimiter '#'
            j = i
            while j < len(s) and s[j] != '#':
                j += 1
            
            # Get the length of the next string
            length = int(s[i:j])
            
            # Move past the '#'
            i = j + 1
            
            # Extract the string
            decoded.append(s[i:i + length])
            
            # Move to the next length prefix
            i += length
            
        return decoded