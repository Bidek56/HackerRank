def findSubstring(str1, K):
     
    # Store the length of the string
    N = len(str1)
 
    # Initialize a prefix sum array
    pref = [0 for i in range(N)]
 
    # Loop through the string to
    # create the prefix sum array
    for i in range(N):
         
        # Store 1 at the index
        # if it is a vowel
        if (str1[i] == 'a' or
            str1[i] == 'e' or
            str1[i] == 'i' or
            str1[i] == 'o' or
            str1[i] == 'u'):
            pref[i] = 1
 
        # Otherwise, store 0
        else:
            pref[i] = 0
 
        # Process the prefix array
        if (i):
            pref[i] += pref[i - 1]
 
    # Initialize the variable to 
    # store maximum count of vowels
    maxCount = pref[K - 1]
 
    # Initialize the variable
    # to store substring with 
    # maximum count of vowels
    res = str1[0:K]
 
    # Loop through the prefix array
    for i in range(K, N):
         
        # Store the current
        # count of vowels
        currCount = pref[i] - pref[i - K]
 
        # Update the result if current count
        # is greater than maximum count
        if (currCount > maxCount):
            maxCount = currCount
            res = str1[i - K + 1 : i + 1]
 
        # Update lexicographically smallest
        # substring if the current count
        # is equal to the maximum count
        elif (currCount == maxCount):
            temp = str1[i - K + 1 : i + 1]
 
            if (temp < res):
                res = temp
 
    # Return the result
    return res
        
if __name__ == '__main__':
    s = "qwdftr"
    l = 2
    print(findSubstring(s, l))