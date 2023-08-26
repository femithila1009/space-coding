#Simple Problem solving string sorting
#input: x3b4U5i2
#output: bbbiiUUUUUxxx

'''a = input()
res = ""
for i in range(0, len(a), 2):
    print(f"{a[i]} {a[i+1]}")
    res = res + a[i] * int(a[i + 1])
    result = sorted(res, key = str.casefold)
    res_str = "".join(result)
print(res_str)'''

#Palindrome String checking
'''a = input("Enter the word : ")
if a == a[: : -1]:
    print("Yes")
else:
    print("No")'''

#String Reversing
'''a = input()
a = a.split()
res = ""
for i in a:
    res += i[: : -1] + " "
print(res)'''