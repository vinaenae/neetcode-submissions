class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for i, word in enumerate(strs):
            anagram["".join(sorted(word))].append(i)
        output_lst = [[] for _ in anagram]
        for ind, word_indexes in enumerate(anagram.values()):
            for i in word_indexes:
                output_lst[ind].append(strs[i])
        return output_lst


