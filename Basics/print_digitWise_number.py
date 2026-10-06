num = int(input("Enter 3 didgit number:"))

hundred = num // 100
tens =(num // 10) % 10
ones = num % 10

print("Hundred = ", hundred)
print("Tens = ",tens)
print("Ones = ",ones)