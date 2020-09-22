list_1 = list(input())
k = 0
c = 1
for item in list_1[1::2]:
    b = list_1[c]
    d = list_1[k]
    list_1[k] = b
    list_1[c] = d
    k += 2
    c += 2
print(list_1)

