a = input()
'''print(a.lower())        #Lowercase
print(a.upper())        #Uppercase
print(a.title())        #Title
print(a.islower())
print(a.isupper())
print(a.istitle())
print(a.isalpha())'''
#print(a.capitalize())
#print(a.swapcase())
#print(a.casefold())
#print(a.replace(a[-1], "r"))
#print(a.replace('i', 'r',2))
#print(a.count(n))


#Concatenation
'''a = "Tesla"
b = "Mithila"
c = a + " + "+b
print(c)'''


#String format:
name = "Tesla"
food = "Chiken"
age = "2"
#tem_string ="I am {}. I love to eat {}.I am {} years old".format(name, food, age)
tem_string ="I am {2}. I love to eat {0}.I am {1} years old".format(food, age, name)
print(tem_string)
print("Hello World!")

