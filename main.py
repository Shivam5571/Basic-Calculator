print("Welcome to My Calculator")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

print("Select Operations")

print("1. Add")
print("2. Subtract")
print("3. Multiply")    
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

a1 = int(input("Enter first number: "))
b2 = int(input("Enter second number: "))

if choice =='1':
    print("Result:", add(a1,b2))
elif choice =='2':
    print("Result: ",subtract(a1,b2))
elif choice =='3':
    print("Result: ", multiply(a1,b2))
elif choice =='4':
    print("Result: ", divide(a1,b2))
else:
    print("Invalid Input")

git init
