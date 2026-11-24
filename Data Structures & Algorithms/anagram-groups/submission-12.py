class Solution:
    # custom frozen hashset for key
    # input : string, output : character counter coalesced into tuple
    def charCount2tuple(self, inputStr: str) -> Tuple[int]:
        charCount = [0] * 26
        for char in inputStr:
            charCount[ord(char) - 97] += 1
        return tuple(charCount)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        anagram2index = {}

        for string in strs:
            keyHash = self.charCount2tuple(string)
            if(keyHash in anagram2index):
                output[anagram2index[keyHash]].append(string)
            else: 
                anagram2index[keyHash] = len(output)
                output.append([string])
        return output