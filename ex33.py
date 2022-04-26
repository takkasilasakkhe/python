i = 15
numbers = []
while i < 21:
    print("At the top i is %d" % i) 
    numbers.append(i)
    i = i + 1
    print("Numbers now: ", numbers) 
    print("At the bottom i is %d" % i) 
print("The numbers: ") 
for num in numbers:
    print(num) 
if numbers[3]==18:
    print("knowing i am going to add the verify value:%d" % numbers[3])
else:
    print(" no transaction")       



