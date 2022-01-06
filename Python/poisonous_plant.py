siz = int(input())
arr = list(map(int, input().split(' ')))
day = 0
ref = []
ite = [i for i in range(1, len(arr))]
while 1:
    for i in ite:
        if arr[i] > arr[i-1]:
            ref.append(i)
    if len(ref) == 0:
        print(day)
        break
    ite.clear()
    temp = 0
    lgt = len(ref)
    for j in range(lgt):
        pos = ref[j] - temp
        arr.pop(pos)
        if len(ite) > 0 and pos != len(arr) and pos != ite[-1]:
            ite.append(pos)
        elif len(ite) < 1 and pos != len(arr):
            ite.append(pos)
        temp += 1
    if len(ite) > 0 and ite[-1] == len(arr):
        ite.pop()
    ref = []
    day += 1