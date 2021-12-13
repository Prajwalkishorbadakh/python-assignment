#write a program to print all prime number is an interval
a=int(input("enter the staring interval="))
b=int(input("enter the ending interval="))
for n in range(a,b):
    if(n>1):
        for i in range(2,n):
            if(n%i==0):
                break
        else:
            print(n)
