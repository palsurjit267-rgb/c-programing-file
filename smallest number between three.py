#WAPP TO CHECK SMALLEST NUMBER BETWEEN THREE NUMBER
a=int(input("enter the 1st number:"))
b=int(input("enter the 2nd number:"))
c=int(input("enter the 3rd number:"))
if(a<b and a<c):
  small= a
elif(b<c):
  small= b
else:
    small= c
print("the smallest number is:",small)
   
