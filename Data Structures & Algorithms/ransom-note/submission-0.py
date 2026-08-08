class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_freq = defaultdict(int)

        for ch in ransomNote:
            ransom_freq[ch] += 1

        magazine_freq = defaultdict(int)

        for ch in magazine:
            magazine_freq[ch] += 1

        for char, freq in ransom_freq.items():
            if magazine_freq.get(char, 0) < freq:
                return False

        return True