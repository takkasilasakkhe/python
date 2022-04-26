gvalue = 0

def set_value(x):
    global gvalue;
    gvalue = x
   


def print_value():
    print(gvalue)    
	

set_value(3)

set_value(5)
print_value()