class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]

        for words in strs:
            while not words.startswith(prefix):
                prefix = prefix[:-1]

                if prefix == "":
                    return ""

        return prefix