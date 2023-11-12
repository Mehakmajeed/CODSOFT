
def add(x, y):
   return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Select operation of choice")
print("Add numbers 1")
print("Subtract numbers 2 ")
print("Multiply numbers 3")
print("Divide numbers 4")

ch = input("Enter your choice of operation ")
x = int(input("Enter first number "))
y= int(input("Enter second number "))
if ch == 1:
   print(x,"+",y, "=", add(x,y))
elif ch == 2:
     print(x ,"-", y, "=", subtract(x,y))
 
elif ch == 3:
      print(x ,"*", y, "=", multiply(x,y))
 
elif ch == 4:
      print(x, "/", y, "=", divide(x,y))
else:
    print("input not valid")