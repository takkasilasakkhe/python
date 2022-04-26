from sys import argv
script,user_name=argv
prompt='>'
print("hi %s, i'm the %s script" %(user_name,script))
print("i'd like to ask you a few questions")
print("do you like sports?")
likes=input(prompt)
print("what's your favorite hobby?")
favourite=input(prompt)
print("do you like travelling?")
like=input(prompt)
print("what is your dream job?")
dream=input(prompt)
print("do you prefer tea or coffee?")
prefer=input(prompt)
print("what kind of sarees do you have?")
sarees=input(prompt)
print("what is your love language")
loves=input(prompt)
print("how many kids do you have")
kids=input(prompt)


print("what is your biggest strength")
biggest=input(prompt)
print("what is your favourite food?")
food=input(prompt)
print("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.%r nice, %r thand how en %r then %r and again %r then %r  and finally %r 
 """ % (likes,favourite,like,dream,prefer,sarees,loves,kids,biggest,food))