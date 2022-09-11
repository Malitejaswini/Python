#Check whether the given number is Prime Number or not.
num=int(input("Enter the number"))
prime=True
for i in range(2,num):
    if(num%i==0):
        prime=False
if prime:
    print("Number is Prime")
else:
    print("Number is not prime")
