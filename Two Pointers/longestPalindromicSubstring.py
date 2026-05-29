class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        def expand_from_center(left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left -= 1
                right += 1

            return s[left+1:right]

        longest = ""    
        for i in range(len(s)):
            even_p = expand_from_center(i,i+1)
            odd_p = expand_from_center(i,i)
            if len(odd_p) > len(longest):
                longest = odd_p
            if len(even_p) > len(longest):
                longest = even_p
        return longest