class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for word in strs:
            length=len(word)
            s = s + str(length) + "#" + word
        return s


    def decode(self, s: str) -> List[str]:
        i=0
        result = []
        while i<len(s):
            j = s.find("#",i)
            length=int(s[i:j])
            word = s[j+1:j+1+length]
            result.append(word)
            i=1+j+length
        return result

