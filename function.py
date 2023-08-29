# Writing my first code in function
'''def greeting():                                  #def =  defining function
    print("Hello, Good Morning! How are you?")
greeting()                                          #greeting() = calling function
greeting()'''

#Parameters vs Argument in function
'''def mul(a,b):                           #def mul(a,b) = a,b parameter
    print(f"The multipling of {a} and {b} = {a*b} ")
mul(3,5)                                            #mul(3,5) = 3,5 argument
mul(19,4)
mul(11,5)'''

#Default parameters vs key argument
'''def intro(name = "Tesla", age = 2, flower = "rose" ):
    print(f"Hello! I am {name}. I am {age} years old. My favourite is flower {flower}.")
intro("Habiba", 34, "Tube rose")
intro("Nasrin", 27, "Rose")
intro()
intro()'''

#Print vs Return
#print = fixed 
#return = modify possible
'''def mul(a,b):
    print(a*b)
mul(4,6)'''

#return
'''def mul (a,b):
    return a * b
result = mul (9,5)
result += 5
result1 = mul(9,5)*2
print(result)
print(result1)'''

#Problems:
#1 - Function with no argument and no return value in python
'''def greeting():
    print("Hello Habiba! How are you?")
greeting()'''

#2 - Funtion with no argument but have a return value in python
'''def num():
    a = int(input())
    b = int(input())
    return a * b 
result = num()
print(result - 5 +10)'''

# 3 - Function with argument but no return value in python
'''def num(a,b,c):
   result = (a + b ) // c
   result1 = (a*c-b)
   result2 = (a + b + c)
   print(result)
   print(result1)
   print(result2)
num(15,9,2)'''

# 4 - Function with argument and return value 
'''def blender(a,b):
    result = f"Blend of {a} and {b}. The spicy powder are ready!"
    return result
ingri = blender("Turmaric","Red chilli")
ingri2 = blender("Ginger", "Onion")
print(ingri)
print(ingri2)'''

