class Solution(object):
    def numberOfSpecialChars(self, word):
        small=set()
        capital=set()
        for char in word:
            if char>='a' and char<='z':
                small.add(char)
            else:
                capital.add(char)
        count=0
        for char in small:
            if char.upper() in capital:
                count+=1
        return count
        