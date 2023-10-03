def armstrong():
n=int(input("enter no:")) x=n
sum=0 while(n!=0):
i=n%10sum=sum+i*i*i
n=n//10
if(x==sum):
print("the number is armstrong")
else:
print("the number is not armstrong") armstrong()
def palindrome():
n=int(input("enter no:"))
b=n
rev=0
while n>0:
rev=rev*10+n%10
n=n//10
print('the reverse is:',rev)
if b==rev:
print('the number is a palindrome') else:
print('the number is not a palindrome') palindrome()
