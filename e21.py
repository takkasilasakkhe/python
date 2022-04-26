def add(a, b,c,d,e):
    print("ADDING %d + %d + %d + %d + %d" % (a, b,c,d,e)) 
    return a + b+c+d+e
def subtract(a, b):
    print("SUBTRACTING %d - %d" % (a, b)) 
    return a - b
def multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b)) 
    return a * b
def divide(a, b):
    print("DIVIDING %d / %d" % (a, b)) 
    return a / b
print("Let's do some math with just functions!")
age = add(30, 5,14,52,85)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))
 
# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")
what = add(age,0,0,0,subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?") 