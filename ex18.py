def print_number(*args):
    arg1,arg2,arg3,arg4=args
    print("arg1: %r" % arg1)
    print("arg2: %r" % arg2)
    print("arg3: %r" % arg3)
    print("arg4: %r" % arg4)
	
def print_value(arg1,arg2,arg3):
    print("arg1: %r" % arg1)
    print("arg2: %r" % arg2)
    print("arg3: %r" % arg3)
def print_hundred(*args):
    arg1,arg2=args
    print("arg1: %r" % arg1)
    print("arg2: %r" % arg2)
def print_code(arg1,arg2):
    print("arg1: %r" % arg1)
    print("arg2: %r" % arg2)
def print_code_again(arg1):
    print("arg1: %r" % arg1)
	
print_number("jan","feb","march","april")
print_value("day","mrng","evng")
print_hundred("mndy","frdy")
print_code("hai","hello")
print_code_again("hyderabad")
