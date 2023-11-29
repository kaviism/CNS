import math
def row(s,key):
    temp = []
    for i in key:
        if i not in temp:
            temp.append(i)
    k = ""
    for i in temp:
        k += i
    k = sorted(k)
    arr = [['' for i in range(len(k))] for j in range(int(len(s) / len(k)))]
    d = 0
    for i in k:
        h = k.index(i)
        for j in range(len(k)):
            arr[j][h] = s[d]
            d += 1
    plain_text = ""
    for i in arr:
        for j in i:
            plain_text += j
    return plain_text

msg = "hello world"
key = "abc"
print(row(msg, key))
