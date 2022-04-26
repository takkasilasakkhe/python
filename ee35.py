def bear_room():
    print("There is a bear here.") 
    print("The bear has a bunch of honey.") 
    print("The fat bear is in front of another door.") 
    print("How are you going to move the bear?") 
        print("The bear has moved from the door. You can go through it now.")
             bear_moved = True 
        
        elif next == "taunt bear" and bear_moved:
            dead1("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:

            print(bear_moved = False
    while True:
        next = input("> ")
        if next == "take honey":
            dead1("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
        "I got no idea what that means.") 
def start():
	print("You are in a dark room.")
	print("There is a door to your right and left.")
	print("Which one do you take?")
next = input("> ")
if next == "left":
	bear_room()
elif next == "right":
	cthulhu_room()
else:
	dead("You stumble around the room until you starve.")
	start()

def cthulhu_room():
	print("Here you see the great evil Cthulhu.")
	print("He, it, whatever stares at you and you go insane.")
	print("Do you flee for your life or eat your head?") 
next = input("> ")
if "flee" in next:
	start()
elif "head" in next:
	dead("Well that was tasty!")
else:
	cthulhu_room()

