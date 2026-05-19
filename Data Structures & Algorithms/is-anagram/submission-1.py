class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_list = [0] * 26
        for i in s:
            my_list[ord(i)-ord('a')] = my_list[ord(i)-ord('a')] + 1
        for j in t:
            my_list[ord(j)-ord('a')] = my_list[ord(j)-ord('a')] -1

        return all(x == 0 for x in my_list)