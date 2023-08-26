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
    print(f"Hello! I am {name}. I am {age} years old. My favourite is {flower}.")
intro("Habiba", 34, "Tube rose")
intro("Nasrin", 27, "Rose")
intro("Mithila", 21, "Sunflower")
intro()'''