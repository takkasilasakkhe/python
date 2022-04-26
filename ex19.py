def apples_and_mangoes(apples_count, mangoes_count):
    print("you have %d apples!" % apples_count)
    print("you have %d mangoes!" % mangoes_count)
	
print("we can just give the numbers directly:")
apples_and_mangoes(40,50)

print("and,we can use values from our script:")
amount_of_apples = 10
amount_of_mangoes = 20

apples_and_mangoes(amount_of_apples, amount_of_mangoes)

print("also use math inside:")
apples_and_mangoes(20 + 10, 9 + 4)

print("finally we can combine the values and math:")
apples_and_mangoes(amount_of_apples + 2000, amount_of_mangoes + 500)
	
