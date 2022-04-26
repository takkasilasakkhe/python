age = int(input("enter age"))
print(age)

sex = input("enter sex(M or F)")
print(sex)
ms = input("enter ms(Y or N)")
print(ms)
if sex=='F':
    print("you will work in only urban areas")
elif sex=='M' and age>=20 and age<=40:
    print("this employee can work anywhere")
elif sex=='M' and age>40 and age<=60:
    print("this employee will work only in urban areas")
else:
    print("ERROR")