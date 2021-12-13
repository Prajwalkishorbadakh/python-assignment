#write a  python program  to find armstrong number in an interval
a=int(input("starting number="))
b=int(input("ending number="))
for i in range(a,b):
    n=i;
    s=0
    while(n>0):
        d=n%10
        s=s+d*d*d
        n=int(n//10)
        if(s==i):
            print(i)
            
        
        
