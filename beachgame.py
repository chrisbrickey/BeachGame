print """
You find yourself looking out over a cliff at the beach and ocean below.
You see your friends playing at the beach.
There's a rocky trail down the side of the cliff leading to the beach.
You also see a shed nearby.
"""

enough_snacks = False

def cliff():
    choice = raw_input("Do you head down the TRAIL or look in the SHED? ")

    if choice == "TRAIL":
        trail()
    elif choice == "SHED":
        shed()
    else:
        dead("The wind swept you off the cliff.")

def dead(why):
    print why, "GAME OVER"
    exit ()

def trail():
    dead ("A crazy goat ate your clothes and you have to find your way home naked.")

def shed():
    print "Inside the shed you see a HANG GLIDER and a shelf of delicious SNACKS."

    choice = raw_input("Do you use the HANG GLIDER to fly down to your friends or do you gather some SNACKS? ")

    if choice == "HANG GLIDER":
        hang_glide(0)
    elif choice == "SNACKS":
        snacks()
    else:
        dead("You alerted the owner of the shed. She calls the authorities.")

def hang_glide(select):
    print "You glide down to the beach and join your friends near the water."

    if select >= 5:
        print "Beach Party!  YOU WIN"
        exit()
    else:
        dead ("Then they discover that you did not bring enough snacks and they send you home.")

def snacks():
    select = input("How many snacks will you take?")
    choice = raw_input("Now, do you take the TRAIL or HANG GLIDE down to your friends?" )

    if choice == "TRAIL":
        trail()
    elif choice == "HANG GLIDE":
        hang_glide(select)
    else:
        dead("You alerted the owner of the shed. She calls the authorities.")

cliff()
