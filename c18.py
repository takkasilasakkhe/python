# this one takes three arguments
def print_name(arg1,arg2,arg3):
    print("arg1: %r, arg2: %r, arg3: %r" % (arg1,arg2,arg3))
# below line takes two arguments
def print_pass(*args):
    arg1,arg2=args
    print("arg1: %r" % arg1)
    print("arg2: %r" % arg2)
# this one takes only one arguments
def print_pop(arg1):
    print("arg1: %r" % arg1)
# this one takes no arguments
def print_none():
    print("nothing")
	
print_name("cat","dog","horse")
print_pass("blue","red")
print_pop("mobile")
print_none()


