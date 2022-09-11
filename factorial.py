#Find the Factorial of given number.
num=int(input("Enter the Number"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("Factorial is =",fact)
