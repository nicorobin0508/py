def rev():
n=int(input("enter no:"))
rev=0
while n>0:
rev=rev*10+n%10
n=n//10
print('the reverse is:',rev)
rev()
