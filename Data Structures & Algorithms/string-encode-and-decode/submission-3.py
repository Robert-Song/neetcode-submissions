class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string))
            encoded += "|"
            encoded += string
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        strlen = ""
        i = 0
        while(i < len(s)):
            char = s[i]
            if (char == "|"):
                decoded.append(s[i+1 : i+int(strlen)+1])
                i += int(strlen)+1
                strlen = ""
                continue
            strlen += str(char)
            i += 1
        return decoded



            
