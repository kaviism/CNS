# To write a python program for row column transposition encryption.

import math
def row(s, key):
    temp = []
    for i in key:
        if i not in temp:
            temp.append(i)
    k = "".join(temp)

    print("The key used for encryption is:", k)
    b = math.ceil(len(s) / len(k))

    if b < len(k):
        b += len(k) - b
    arr = [['_' for _ in range(len(k))] for _ in range(b)]

    i = 0
    j = 0
    for h in range(len(s)):
        arr[i][j] = s[h]
        j += 1
        if j > len(k) - 1:
            j = 0
            i += 1
    print("The message matrix is:")
    for i in arr:
        print(i)
    kk = sorted(k)

    cipher_text = ""
    for i in kk:
        h = k.index(i)
        for j in range(len(arr)):
            cipher_text += arr[j][h]

    print("The cipher text is:", cipher_text)

msg = "This is the message to be encrypted"
key = "encryptionkey"
row(msg, key)
