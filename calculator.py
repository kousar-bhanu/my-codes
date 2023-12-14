#Function to perform addition
def add(x,y):
    return x+y
#Function to perform subtraction
def subtract(x,y):
    return x-y
#Function to perform multiplication
def multiply(x,y):
    return x*y
#Function to perform division
def divi(x,y):
    return x/y if y!= 0 else "cannot divide by zero"

print("Simple Calculator")
print("Choose operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

#Take user input for operation choice
choice = input("Enter choice (1/2/3/4): ")
#Take user input two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result=None
#Perform the calculation based on user's choice
if choice == '1':
    result = add(num1, num2)
elif choice == '2':
    result = subtract(num1, num2)
elif choice =='3':
    result = multiply(num1, num2)
elif choice == '4':
    result = divide(num1, num2)  
else:
    print("Invalid input")

#Display the result
if result is not None:
    print("Result:",result)     

