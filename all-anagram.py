from collections import Counter
class Solution:
    def isAnagram(self,c1, c2):
        for c in "abcdefghijklmnopqrstuvwxyz":
            if c1[c] != c2[c]:
                return False
        return True
    
    def findAnagrams(self,s, p):
        range_list = []
        c1 = Counter(s[:len(p)])
        c2 = Counter(p)
        if self.isAnagram(c1,c2):
            range_list.append(0)
        for i in range (1, len(s)-len(p) +1):
            c1[s[i-1]] -= 1
            c1[s[i + len(p)-1]] += 1 

            if self.isAnagram(c1,c2):
                range_list.append(i)
        return range_list

    

if __name__ == "__main__":
    main_string = "abbascbsanbaanaabba"
    sub_string = "ab"
    s = Solution()
    ans = s.findAnagrams(main_string,sub_string)
    print(ans)

            
