def cal_sum_sub(a, b):
    sum = a+b
    if a>b:
     difference = a-b
    else:
       difference = b-a

    return f"Sum of two variables is: {sum}, Difference of two variables is: {difference}"

a= int(input("Enter first variable: ")) 
b= int(input("Enter second variable: ")) 
print(cal_sum_sub(a,b))
