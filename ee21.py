def add(a,b,c):
    print("adding %d + %d + %d" % (a,b,c))
    return a + b + c
def subtract(a,b,c,d):
    print("subtracting %d - %d - %d - %d " %(a,b,c,d))
    return a - b - c - d 
def multiply(a,b):
    print("multiplying %d * %d" %(a,b))	
    return a * b
def divide(a,b,c):
    print("dividing %d / %d / %d" % (a,b,c))
    return ((a / b) / c )

print("let's do some match with just functions")
age = add(4, 5, 3)
height = subtract(47, 9, 3, 2)
weight = multiply(60, 3)
iq = divide(90, 2, 3)

print("age: %d, height: %d, weight: %d, iq: %d" % (age,height,weight,iq))

print("here is a puzzle")
what = add(age,0,subtract(height,0,1,multiply(weight,divide(iq,1,2))))
print("that become:", what, "can you do it by hand?")
