a=input().split()
num1=a[0]
num2=a[1]
num3=a[2]
if num1>num2 and num1>num3:
    print(num1)
elif num2<num1 and num2<num3:
    print(num2)
else:
    print(num3)
