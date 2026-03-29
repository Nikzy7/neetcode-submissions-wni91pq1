class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_of_s = dict()

        for ch in s:
            freq_of_s[ch] = freq_of_s.get(ch,0) + 1

        for ch in t:
            current_available_count = freq_of_s.get(ch,0)
            
            if current_available_count <= 0:
                return False
            else:
                freq_of_s[ch] -= 1
                
        for ch,freq in freq_of_s.items():
            if freq != 0:
                return False
            
        return True