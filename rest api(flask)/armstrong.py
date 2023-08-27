num =int(input("enter your number"))
sum=0
temp=num
while temp>0:
    digite = temp%10
    cube = digite**3
    sum = sum + cube
    temp = temp //10
if sum == num:
    print("its an armstrong")
else:
    print("its not an armstrong")

