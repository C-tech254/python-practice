#variables are containers for storing data values

x = 6
y = "Lydia"
print(x)
print(y)


# this are called variable names

myvar ="Charles"
my_Var ="Charles"   
print(myvar) 
print(my_Var)



#creating a variable outside a funtion and using it inside the funtion
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()