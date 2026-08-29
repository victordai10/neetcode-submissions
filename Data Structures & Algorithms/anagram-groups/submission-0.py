class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)
        for s in strs:
            # for each word get the mapping and then append the word to the mapped key
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            anagramMap[tuple(count)].append(s)
        
        return list(anagramMap.values())
