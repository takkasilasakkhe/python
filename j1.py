gvalue = 0

def set_value(x):
    global gvalue;
    gvalue = x
    print(gvalue)


def print_value():
    print(gvalue)    
	

set_value(3)
print_value()
set_value(5)
print_value()