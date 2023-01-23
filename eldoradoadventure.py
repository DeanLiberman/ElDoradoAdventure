gold = 0







print "With a blurry head, you arise to your feet atop cracked ruins of the city of gold"
print "El Dorado. Be it your lust for gold or your lust for adventure, you know not why"
print "you ended up here, save for that you are. Or at least it would seem. For a city"
print "of gold, you do not seem to see anything save for mossy covered cracked stone"
print "beneath your feet."

print "All of a sudden, a rumbling occurs beneath your feet, sending you down into"
print "the lower ruins below!"

def eastroom():
    gold = 0
    print "The eastern room contains a bronze statue with golden hair."
    print "At least, the statue's hair LOOKS gold."
    print "In any event, the statue has a bowl at its feet containing pieces upon pieces"
    print "of gold! Along with some crummy old sign, but who cares about that?!"
    print "You can TAKE SOME GOLD, READ THE SIGN, or GO BACK WEST."
    
    decision = raw_input("> ")
    if decision == "TAKE SOME GOLD" or decision == "Take Some Gold" or decision == "Take Some Gold":
        next = raw_input("> ")
        if "0" in next or "1" in next or "2" in next or "3" in next or "4" in next or "5" in next or "6" in next or "7" in next or "8" in next or "9" in next:
            how_much = int(next)
        
        if how_much != 36:
            print "You should have read the sign!"
            print "The walls collapse upon you for your greed and/or illiteracy."
            print "GAME OVER"
            exit(1)
        if how_much == 36:
            print """You grab 36 pieces of gold. To your disappointment(but not your surprise), they turn out to be chocolate wrapped in golden foil. From the indentation you made in the bowl, you can make out an inscription at the bottom of the statue.
        
        
        MIGUEL - THE BLONDE HAIRED GOD OF EL DORADO
        
        
        
        
        
        """
        eastroom()
        
    elif decision == "READ THE SIGN" or decision == "Read The Sign" or decision == "read the sign":
        print "'To avoid being crushed by the wall of shame, take exactly '36' pieces of gold to skirt the blame.'"
        eastroom()
    elif decision == "GO BACK WEST" or decision == "Go back west" or decision == "go back west.":
        centerroom()
        



def centerroom():

    
    print "You land atop a soft pile of hay."
    print "From the light that trickles in from above, you see that from this center room"
    print "you can GO NORTH, GO SOUTH, GO EAST, or GO WEST."
    
    direction = raw_input("> ")
    if direction == "GO SOUTH" or direction == "Go South" or direction == "go south":
        southroom()

    if direction == "GO NORTH" or direction == "Go North" or direction == "go north":
        northroom()
    if direction == "GO WEST" or direction == "Go West" or direction == "go west":
        westroom()
    if direction == "GO EAST" or direction == "Go East" or direction == "go east":
        eastroom()
        
def westroom():
    print "You arrive in the western room, to find nothing but a DISCARDED PLACARD lying on"
    print "the mossy floor."
    print "You can INSPECT THE PLACARD or GO BACK EAST."
    
    decision = raw_input("> ")
    if decision == "INSPECT THE PLACARD" or decision == "Inspect the placard" or decision == "inspect the placard":
        print """ From the discarded center of the placard, you can just barely make out the inscription...
        
        
        TULIO - THE BLACK HAIRED GOD OF EL DORADO
        
        
        """
        westroom()
    elif decision == "GO BACK EAST" or decision == "Go back east" or decision == "go back east":
        centerroom()
        
    else: westroom()
        
def northroom():
    print "You arrive at a dead end that contains nothing save a bronze statue of a woman holding an armadillo."
    print "You can GO BACK SOUTH or INSPECT THE STATUE."
    decision = raw_input("> ")
    if decision == "INSPECT THE STATUE" or decision == "Inspect The Statue" or decision ==   "Inspect the statue":
    
        print """ 
    
    
    CHEL - THE SLY TRICKSTER GODDESS OF EL DORADO
    
    
    """
        return northroom()
    elif decision == "GO BACK SOUTH" or decision == "go back south" or decision == "Go Back South":
        centerroom()
    
def southroom():
    wronganswers = 0
    rightanswers = 0
    
    


    print "As you fumble around in the dark of the southern room, you hear a voice boom!"
    print "I am the Lord of El Dorado!"
    print "... the voice claims."
    print "If you wish to proceed further, you must answer me these questions three!"
    print "Throughout these ruins ye should have gathered the names of the triumvitrate of gods of El Dorado!"
    print "If ye have that knowledge, then STEP FORWARD to be tested!"
    print "But be warned, if ye answer but even one question incorrectly, doom(or a game over state) await thee!"
    print "In a somewhat more modest tone, the voice says 'If you are not yet prepared, you can always BACK OUT for now.'"

    decision = raw_input(">")
    if decision == "BACK OUT" or decision == "Back Out" or decision == "Back Out":
        print "A giant stone hand grabs you, and tosses you back to the center of the ruins!"
        centerroom()
    else:
        print "Very Well Mortal! I hope you are prepared!" 
        

    print "What is the mortal name of the blonde haired hero in 'The Road to El Dorado?"
    answer = raw_input(">")
    if answer == "Miguel" or answer == "miguel" or answer == "MIGUEL":
            rightanswers += 1
    else: wronganswers +=1
        
    if wronganswers >= 1:
        print "With your incorrect trivia answer, a loud terrible voice booms from the nether!"
        print "You have failed the test of El Dorado!"
        print "You hear a terrible rumbling, or mayhaps a tumbling."
        print "In any bloody event the sound isn't particularly appealing."
        print "The golden shimmering light arounds you fades to black."
        print "Leaving you in the eternal abyssal darkness."
        print "Until a catapult ejects you from the ruins, stamping a red 'loser' atop your"
        print "forehead, leaving you flushed and embarassed and very much not rich with gold."
        exit(1)
    
    print "What is the mortal name of the black haired hero in 'The Road to El Dorado?"
    answer = raw_input(">")
    if answer == "Tulio" or answer == "tulio" or answer == "TULIO":
            rightanswers += 1
    else: wronganswers +=1
        
    if wronganswers >= 1:
        print "With your incorrect trivia answer, a loud terrible voice booms from the nether!"
        print "You have failed the test of El Dorado!"
        print "You hear a terrible rumbling, or mayhaps a tumbling."
        print "In any bloody event the sound isn't particularly appealing."
        print "The golden shimmering light arounds you fades to black."
        print "Leaving you in the eternal abyssal darkness."
        print "Until a catapult ejects you from the ruins, stamping a red 'loser' atop your"
        print "forehead, leaving you flushed and embarassed and very much not rich with gold."
        
    print "What is the mortal name of the sly native girl in 'The Road to El Dorado?"
    answer = raw_input(">")
    if answer == "Chel" or answer == "chel" or answer == "CHEL":
            rightanswers += 1
    else: wronganswers +=1
        
    if wronganswers >= 1:
        print "With your incorrect trivia answer, a loud terrible voice booms from the nether!"
        print "You have failed the test of El Dorado!"
        print "You hear a terrible rumbling, or mayhaps a tumbling."
        print "In any bloody event the sound isn't particularly appealing."
        print "The golden shimmering light arounds you fades to black."
        print "Leaving you in the eternal abyssal darkness."
        print "Until a catapult ejects you from the ruins, stamping a red 'loser' atop your"
        print "forehead, leaving you flushed and embarassed and very much not rich with gold."
        
    if rightanswers >= 3:
        print "Congratulations, you passed the test of El Dorado!"
        print "With a less portent of doom kind of rumbling, the ceiling opens before you"
        print "Revealing rows and rows and columns of gold bars."
        print "Actual gold bars, not the chocolate pieces you may have found earlier."
        print "With a pumped fist and a taut lasso, you scale the walls to fill your pockets!"
        print "EL DORADO ADVENTURE - GOOD ENDING."
        exit(1)
centerroom()
