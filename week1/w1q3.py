list = []

print("Enter 20 numberes: ")

for i in range(20):
    num = int(input(f"Enter number {i + 1}: "))
    list.append(num)

print("Numbers divisible by 5 are: ")
for num in list:
    if num % 5 ==0:
        print(num)
