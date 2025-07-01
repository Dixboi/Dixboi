class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        https://neetcode.io/problems/anagram-groups
        '''

        group = defaultdict(list)

        for string in strs:
            count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            for character in string:
                count[ord(character) - ord("a")] += 1

            group[tuple(count)].append(string)

        return group.values()
        
