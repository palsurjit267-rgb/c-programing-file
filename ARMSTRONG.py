#TO CHECK WHETHER A PROGRAM IS ARMSTRONG OR NOT
n=int(input("enter a number:"))
temp = n
sum = 0
while(n>0):
    digit=n%10
    sum=sum + digit ** 3
    n = n//10
if temp == sum:
    print("the numbrt is armstrong number  ")
else:
    print("thr number is not armstrong number ")
    
