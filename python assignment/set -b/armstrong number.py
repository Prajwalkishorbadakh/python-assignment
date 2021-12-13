#write a python program ti check armstrong number
number=int(input("enter the number="))
sum=0
number1=number
while(number1>0):
    digit=number1%10
    sum=sum+digit*digit*digit
    number1=int(number1//10)
if(number==sum):
    print("number is armstrong")
else:
    print("number is not armstrog")
