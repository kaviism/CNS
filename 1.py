# To write a python program for Ceaser cipher encryption 

P="Var"
lst1 = list(chr(i) for i in range(97,123))
k = list(lst1.index(j) for j in lst1)
plaintext = [lst1.index(i.casefold()) for i in P if i.casefold() in lst1]
cipher = [x+2 for x in plaintext]
print("".join(lst1[m] for m in cipher if m in k))
