a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

if(a > b):
    largest = a
elif(b > a):
    largest = b
else:
    largest = "Both numbers are equal"

print("Largest number is: ",largest)