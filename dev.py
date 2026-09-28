##    *
##  * * *
##* * * * *
l=int(input("Enter length: "))
for i in range(1,l+1):
    for k in range(l-i):
        print(" ",end=" ")
    for j in range(i*2-1):
        print("*",end=" ")
    print() 
