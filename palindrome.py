#Check whether the given number is Palindrome or not.
num=int(input("Enter The Number"))
temp=num
rev=0
while(num>0):
    rmain=num%10
    rev=rev*10+rmain
    num=num//10
    print(rev)
if(temp==rev):
        print("Number Is Palindrome")
else :
        print("Number is NOt Palindrome")
