class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for words in strs:
            key_list = [0]*26
            for letters in words:
                key_list[ord(letters)-ord("a")] += 1
            key_tuple=tuple(key_list)
            if key_tuple in dict:
                dict[key_tuple].append(words)
            else:
                dict[key_tuple] = [words]
        return list(dict.values())