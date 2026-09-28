#WAPP TO CHECK GRETHER BETWEEN THREE NUMBER
a=int(input("enter the 1st number"))
b=int(input("enter the 2nd number"))
c=int(input("enter the 3rd number"))
if(a>b and a>c):
    big= a
elif(b>c):
    big= b
else:
    big= c
print("The largest number:",big)

