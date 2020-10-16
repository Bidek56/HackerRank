def findSubstring(s, k):

    #fetch all substrings
    string_is = s
    sub = k
    length = len(string_is)
    sub_ar = [string_is[i:j+1] for i in range(length) for j in range(i,length)]
    print(sub_ar)

    #fetch substrings of a length = 5
    sub_ar_is = []
    for each in sub_ar:
        if len(each) == k:
            sub_ar_is.append(each)
    print(sub_ar_is)
    data_dict = {}
    data = ['a','e','i','o','u']
    for each in sub_ar_is:
        count = 0
        for each_is in data:
            count = count + each.count(each_is)

        if count:
            data_dict.update({each:count})

    # print(data_dict)
    # print("Substring is: ", max(data_dict, key=data_dict.get))
    if len(data_dict.keys()):
        return max(data_dict, key=data_dict.get)
    else:
        return "Not found!"
        
if __name__ == '__main__':
    s = "qwdftr"
    
    l = 2
    print(findSubstring(s, l))