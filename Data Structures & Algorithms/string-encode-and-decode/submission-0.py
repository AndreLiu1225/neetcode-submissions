class Solution:
    # we need to store the length of each string so that we know
    # how many positions to loop through the encoded string
    def encode(self, strs: List[str]) -> str:
        delimiter = "#"
        encoded = ""

        for s in strs:
            length = len(s)
            encoded += str(length)
            encoded += delimiter
            encoded += s

        
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        idx = 0

        while idx < len(s):
            delimiter_pos = s.find("#", idx)
            length = int(s[idx:delimiter_pos])
            word = s[delimiter_pos + 1 : delimiter_pos + 1 + length]
            res.append(word)
            idx = delimiter_pos + 1 + length
        
        return res