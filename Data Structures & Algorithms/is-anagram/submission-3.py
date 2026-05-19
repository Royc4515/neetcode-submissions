class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False 
        #idea: indexing all chars into a list, run on one list will
        my_list = [0] * 26
        #for every char occurence in s add 1 to the char index, for every occurence in t decrement 1 from the char index
        for i, j in zip(s, t):
            my_list[ord(i)-ord('a')] += 1
            my_list[ord(j)-ord('a')] -= 1

        return all(x == 0 for x in my_list) #if both has same chars exactly the list should be zeroed