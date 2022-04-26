def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses!" % cheese_count) 
    print("You have %d boxes of crackers!" % boxes_of_crackers) 
    print("Man that's enough for a party!") 
    print("Get a blanket.\n") 
    
# first code runs here for values cheese_count=20,boxes_of_crackers=30
print("We can just give the function numbers directly:") 
cheese_and_crackers(1+19, 30)

# second code runs here for values amount_of_cheese=10 and amount_of_crackers=50
print("OR, we can use variables from our script:") 
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# third code
print("We can even do math inside too:") 
cheese_and_crackers(40 + 20, 5 + 6)

# fourth code
print("And we can combine the two, variables and math:") 
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)