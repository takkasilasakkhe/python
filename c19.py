def sweets_and_fruits(sweets_count, fruits_count):
    print("you have %d sweets" % sweets_count)
    print("you have %d fruits" % fruits_count)
	
print("we can just give the function numbers directly")
sweets_and_fruits(10,50)

print("and we can use variables from our script")
amount_of_sweets = 80
amount_of_fruits = 100 

sweets_and_fruits(amount_of_sweets, amount_of_fruits)

print("we can also use math inside")
sweets_and_fruits(10 + 2, 20 + 5)

print("finally we combine both, variables and math")
sweets_and_fruits(amount_of_sweets + 200, amount_of_fruits + 700)