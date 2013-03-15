# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image miwa base = "sprites/cfv_april_miwa_basic.png"
image miwa prop = "sprites/cfv_april_miwa_propose.png"
image miwa diss = "sprites/cfv_april_miwa_dissapoint.png"
image miwa think = "sprites/cfv_april_miwa_thinking.png"
image miwa appal = "sprites/cfv_april_miwa_appaled.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")
define miw = Character('Miwa', color="#bcbcbd")
define mis = Character('Misaki', color="#d9b0e7")
define kai = Character('Kai', color="#09cba4")
define ren = Character('Ren', color="#cb012c")
define jun = Character('Jun', color="#426572")
define ai = Character('Aichi', color="#13568a")
define asa = Character('Asaka', color="#6198db")
define kam = Character('Kamui', color="#ef9a20")


# The game starts here.
label start:
    $ in_bread = False
    $ in_stocks = False
    $ in_fire = False

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"
    
    "A shot of a deck being taken from table, and put into a bag."
    
    "Flash"
    
    "Boy" "my deck is gone!"
    
    #Closeups of Misaki, Kai and Miwa.#
    "And it was such a quiet day too..."
    mis "What is going on?"
    "Boy" "My deck is missing!"
    mis "Ah, everyone, did anyone see this boy's deck? The clan is..."
    "Boy" " Oracle Think-Tank."
    #Misaki looks shocked
    mis "...Oracle Think-Tank."
    #Miwa ace detective flashes on screen.
    #Shop is visible with kai, misaki and miwa figures.
    show miwa base at left
    
    miw "So this kid was distracted and poof, and someone nicked the deck while he wasn't looking?"
    mis "I saw that the boy was playing, and next thing his deck is stolen."
    miw " And neither you or the assistant-manager saw anything? Anyone leave the shop?"
    mis "No, not at all."
    miw "That's new."
    mis "Ayup."
    miw "Let's asume that there's nothing wrong with with your eyesight."
    #map of the shop
    miw "The boy was here when the deck got stolen, right?"
    #boy's location is marked
    mis "Correct."
    miw "You were at you usual spot with the sub-manager, right here near the door."
    #misaki's location is marked
    miw "You can't have seen the cards being stolen because it was behind the wall."
    miw "But you didn't see anybody leave, which means..."
    #The door is marked
    mis "They went into the storeroom?"
    miw "Exactly"
    #Misaki realising something
    mis "C'mon!"
    
    #Storeroom background, Misaki figure appears.
    
    miw "There's noone here."
    mis "But that's impossible..."
    miw "Hm... Let's see what we can find."
label investigate:    
    #Player has the ability to check things out now: *door, breadcrumbs, the stocks*
    menu:
        miw "What shall we take a look at?"
        "Are those breadcrumbs?":
            jump qbread
        "Check the stocks":
            jump qstocks
        "Check the door":
            jump qfireescape

label qbread:
    #miwa determined
    miw "Aha! Breadcrumbs! Get me some iodine!"
    mis "What? You mean to check for starch?"
    #miwa propose
    miw "Indeed, my dear Misaki!"
    #misaki annoyed
    mis "Can't you do something normal? Like, fingerprinting? Or going to the police?"
    miw "Well, that's elementary, isn't it? The police won't take us seriously at all! And what are we supossed to fingerprint in the first place?"
    mis "Right, but... Miwa, all bread contains starch, so iodine isn't going to solve this case."
    #misaki embarrased
    mis "Besides, those are mine, I had a snack after changing the posters yesterday."
    #miwa annoyed
    miw "Fine."
    $ in_bread = True
    if in_stocks and in_fire and in_bread:
        jump investigateconclude
    else:
        jump investigate
label qstocks:
    #the stocks
    miw "(Misaki is looking at the stocks...)"
    mis "If they stole a deck, who knows what else they've stolen"
    #Misaki looks relieved#
    mis "I can't see anything missing."
    #Miwa smiles
    miw "That's good."
    $ in_stocks = True
    if in_stocks and in_fire and in_bread:
        jump investigateconclude
    else:
        jump investigate
label qfireescape:
    #the fireescape
    miw "Can this door open?"
    mis "Miwa, wait!"
    #picture of door opening, fire alarm starts to ring
    mis "Now you've done it!"
    #screen goes black. firealarm cuts off.
    mis "Next time, ask if you can open the Fire exit."
    miw "Sorry."
    miw "(but we now know the thief didn't leave through here.)"
    $ in_fire = True
    if in_stocks and in_fire and in_bread:
        jump investigateconclude
    else:
        jump investigate
label investigateconclude:
    #conclusion
    "They are not here."
    
    #Kai asking who should go with Miwa
    kai "Someone should go with him, the last time I left him to his own devices, I found him tied up by the backstreet boys."
    mis "Tell me why?"
    kai "No."
    kai "Ain't nothing but a headache."
    kai "Shall I go?"
    mis "Hm..."
    menu:
        "I'll go.":
            jump misakiroute
        "Let Kai go":
            jump kairoute
        
label misakiroute:
    
    #Misaki route
    #Visiting Jun
    miw "It's not what it sounds like! Don't go thinking crazy things now!"
    mis "Too late for that."
    #Visiting Ren
    #Misaki comes to the conclusion this was set up by Kai somehow and goes out to murder him.
    ren "Ah? Where is everyone?"
    "Boy" "They left for some reason."
    ren "Really? That's no fun..."
    asa "Ren-sama! Why did you try to get that Tokura girl here anyway?"
    ren "Asaka!"
    ren "Ah, I needed some help with moving furniture!"
    asa ""
    #scene fade
    kai "Maybe it's time you learn the world doesn't revolve around you Tokura!"
    mis "Really, that's rich coming from you!"
    miw "I don't think she needs any help though..."
    kam "I guess you're right."
    kam "Hey, you up for a game?"
    miw "Sure."
    $ persistent.misaki_fin = True
    #check if both endings played, goto secret ending
    if persistent.misaki_fin and persistent.kai_fin:
        jump kaichihoneymoon
    else:
        return
label kairoute:
    
    #Kai's route
    #Meeting with Aichi
    miw "Aha! I see now, it must be his evil twin brother!"
    ai "No way!"
    kai "..."
    #Visiting Ren
    ren "Kai, what a surprise to see you!"
    ai "Ren!"
    ren "And Aichi too, you three are the only ones?"
    kai "Ren, why did you ask that kid to pretend his deck was stolen?"
    ren "Ah, well..."
    ren "I had hoped on visit from a lovely shop assistant."
    kai "I did bring one."
    miw "Hi!"
    ren "Hm? Detective, Shop assistant, you're quite versatile, aren't you?"
    ren "But I had hoped on someone with wider hips."
    kai "She didn't feel like coming."
    ren "Really now?"
    ren "Oh well, at the least we have Aichi and... Of Course..."
    kai "This is Miwa... Taishi. He plays Kagero... Is an Aries... And..."
    kai "Likes long walks along the beach?"
    miw "Really?"
    ren "Shop assistant huh?"
    ren "You'll do, c' mon."
    miw "huh?"

    $ persistent.kai_fin = True
    #check if both endings played, then goto secret ending.
    if persistent.misaki_fin and persistent.kai_fin:
        jump kaichihoneymoon
    else:
        return
    
label kaichihoneymoon:
    "Blabla"
    
    return
