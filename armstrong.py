
#Check whether the given number is Armstrong or not.
num=int(input("Enter The Number ="))
temp=num
total=0
while(temp>0):
    rev=temp%10
    total=total+rev**3
    temp=temp//10
if(total==num):
    print("Number is ARMSTRONG")
else :
    print("Number is not ARMSTRONG")
