class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_val = 0
        tmp = 0
        i = 0
        he = len(s)
        for i in range(k):
            if s[i] in 'aeiou':
                tmp += 1
                if tmp == k:
                    return k
        if tmp > max_val:
            max_val = tmp
        for i in range(k,he):
            if s[i-k] in 'aeiou':
                tmp -= 1
            if s[i] in 'aeiou':
                tmp += 1
            if tmp > max_val:
                max_val = tmp
        return max_val
        
if __name__ == '__main__':
    s = "azerdii"
    l = 5
    sl = Solution()

    print(sl.maxVowels(s, l))