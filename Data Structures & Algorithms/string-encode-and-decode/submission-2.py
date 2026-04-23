class Solution:
    # algorithm: encoded string='len(s1)#s1len(s2)#s2...'
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + '#' + s
        return encoded_string 

    def decode(self, s: str) -> List[str]:
        decoded_list = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            string_length = int(s[i:j])
            i = j+1
            j = i + string_length
            decoded_list.append(s[i:j])
            i = j

        return decoded_list