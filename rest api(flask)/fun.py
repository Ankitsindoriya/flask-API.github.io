def sum(a,b):
    return a+b


def avg(a,b):
    return (a+b)/2

def is_armstrong(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        cube = digit ** 3
        sum = sum + cube
        temp = temp // 10
    if sum == num:
        print("It's an Armstrong number")
        return True
    else:
        print("It's not an Armstrong number")
        return False

# Take input from the user
num = int(input("Enter your number: "))
is_armstrong(num)
