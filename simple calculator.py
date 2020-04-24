def addition(x, y):
    return x + y
def subtract(x,y):
    return x-y
def division(x,y):
    return x/y
def multiply(x,y):
    return x*y
print("select operation")
print("1.addition")
print("2.subtraction")
print("3.Division")
print("4.Multiplication")

choice=input("select operation 1/2/3/4:")

num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))

if choice=="1":
    print("sum of", num1 ,"and", num2 ,"is", addition(num1,num2))
if choice=="2":
    print("The subtraction of",num1, "and", num2, "is", subtract(num1,num2))
if choice=="3":
    print("The division of", num1, "and",num2, "is", division(num1,num2))
if choice=="4":
    print("The multiplication of", num1, "and",num2, "is", multiply(num1,num2))
