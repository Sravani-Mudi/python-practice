#def greet():
 #   print("Hello Python")

#greet()

#Addition Using Function
#def add():
#    a = 10
 #   b = 20
  #  result = a + b
   # print("Addition =", result)

#add()

#Parameters
#def add(a, b):
 #   result = a + b
  #  print("Addition =", result)

#add(50, 30)

#return 

#def add(a, b):
 #   result = a + b
  #  return result

#answer = add(10, 50)

#print("Addition =", answer)

#Default Parameters
#def greet(name="Sravani"):
 #   print("Hello", name)

#greet()
#greet("Ravi")

#Keyword Arguments
#def student(name, age):
 #   print("Name:", name)
  #  print("Age:", age)

#student(age=20, name="Sravani")

#Variable-Length Arguments
#def add(*numbers):
 #   total = 0

  #  for num in numbers:
   #     total = total + num

    #print("Total =", total)


#add(10, 20, 30)
#add(5, 10, 15, 20)

#Local Variables & Global Variables
# def display():
#     x = 10
#     print("Local value:", x)

# display()

# x = 100

# def display():
#     print("Global value:", x)

# display()

#Recursive Function
def countdown(n):
    if n == 0:
        print("Finished")
    else:
        print(n)
        countdown(n - 1)

countdown(5)
