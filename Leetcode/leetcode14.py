class Solution:
    def longestCommonPrefix(self, strs):
        index = 0
        prefix = []

        while True:
            for word in strs:

                if index >= len(word):
                    return "".join(prefix)

                char = word[index]
                if char != strs[0][index]:
                    return "".join(prefix)

            prefix.append(char)
            index += 1  

input = Solution()
output = input.longestCommonPrefix(["flower","flow","flight"])     
print(output)
            

        