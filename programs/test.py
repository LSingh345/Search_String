class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        return " ".join(list(reversed([x for x in s.split(' ') if x != ""])))
