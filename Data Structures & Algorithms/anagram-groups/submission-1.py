class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for words in strs:
            key = ''.join(sorted(words))
            if key in dict:
                dict[key].append(words)
            else:
                dict[key] = [words]
        return list(dict.values()) 