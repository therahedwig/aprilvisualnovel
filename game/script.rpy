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


# The game starts here.
label start:
    $ in_bread = False
    $ in_stocks = False
    $ in_fire = False
    $ misaki_fin = False
    $ kai_fin = False

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"
    
    "A shot of a deck being taken from table, and put into a bag."
    
    "Flash"
    
    "Boy" "my deck is gone!"
    
    #Closeups of Misaki, Kai and Miwa.#
    "And it was such a quiet day too..."
    "Misaki" "What is going on?"
    "Boy" "My deck is missing!"
    "Misaki" "Ah, everyone, did anyone see this boy's deck? The clan is..."
    "Boy" " Oracle Think-Tank."
    #Misaki looks shocked
    "Misaki" "...Oracle Think-Tank."
    #Miwa ace detective flashes on screen.
    #Shop is visible with kai, misaki and miwa figures.
    show miwa base at left
    
    "Miwa" "So this kid was distracted and poof, and someone nicked the deck while he wasn't looking?"
    "Misaki" "I saw that the boy was playing, and next thing his deck is stolen."
    "Miwa" " And neither you or the assistant-manager saw anything? Anyone leave the shop?"
    "Misaki" "No, not at all."
    "Miwa" "That's new."
    "Misaki" "Ayup."
    "Miwa" "Let's asume that there's nothing wrong with with your eyesight."
    #map of the shop
    "Miwa" "The boy was here when the deck got stolen, right?"
    #boy's location is marked
    "Misaki" "Correct."
    "Miwa" "You were at you usual spot with the sub-manager, right here near the door."
    #misaki's location is marked
    "Miwa" "You can't have seen the cards being stolen because it was behind the wall."
    "Miwa" "But you didn't see anybody leave, which means..."
    #The door is marked
    "Misaki" "They went into the storeroom?"
    "Miwa" "Exactly"
    #Misaki realising something
    "Misaki" "C'mon!"
    
    #Storeroom background, Misaki figure appears.
    "Miwa" "(Misaki is looking at the stocks...)"
    "Misaki" "If they stole a deck, who knows what else they've stolen"
    #Misaki looks relieved#
    "Misaki" "I can't see anything missing."
    #Miwa smiles
    "Miwa" "That's good."
    "Misaki" "But how did they leave?"
    
    #Player has the ability to check things out now: *door, breadcrumbs, the stocks*
    menu:
        "Are those breadcrumbs?":
            jump qbread
        "check the stocks again":
            jump qstocks
        "check the fireescape":
            jump qfireescape

label qbread:
    "Miwa" "Aha! Breadcrumbs! Get me some iodine!"
    "Misaki" "What? You mean to check for starch?"
    "Miwa" "Indeed, my dear Misaki!"
    "Misaki" "Can't you do something normal? Like, fingerprinting? Or going to the police?"
    "Miwa" "Well, that's elementary, isn't it? The police won't take us seriously at all! And what are we supossed to fingerprint in the first place?"
    "Misaki" "Right, but... Miwa, all bread contains starch, so iodine isn't going to solve this case."
    "Misaki" "Besides, those are mine, I had a snack after changing the posters yesterday."
    "Miwa" "Fine."
    $ in_bread = True
label qstocks:
    #the stocks
    $ in_stocks = True
label qfireescape:
    #the fireescape
    $ in_fire = True
label investigateconclude:
    #conslusion
    "They are not here."
    
    #Kai asking who should go with Miwa
    menu:
        "I'll go.":
            jump misakiroute
        "Let Kai go":
            jump kairoute
        
label misakiroute:
    
    #Misaki route
    #Visiting Jun
    #Visiting Ren
    #Misaki comes to the conclusion this was set up by Kai somehow and goes out to murder him.
    $ misaki_fin = True
    #check if both endings played, goto secret ending
label kairoute:
    
    #Kai's route
    #Meeting with Aichi
    #Visiting Ren
    "Ren" "Kai, what a surprise to see you!"
    "Aichi" "Ren...."
    "Ren" "And Aichi too, you three are the only ones?"
    "Kai" "Ren, why did you ask that kid to pretend his deck was stolen?"
    "Ren" "Ah, well..."
    "Ren" "I had hoped on visit from a lovely shop assistant."
    "Kai" "I did bring one."
    "Miwa" "Hi!"
    "Ren" "Hm? Detective, Shop assistant, you're quite versatile, aren't you?"
    "Ren" "But I had hoped on someone with wider hips."
    "Kai" "She didn't feel like coming."
    "Ren" "Really now?"
    "Ren" "Oh well, at the least we have Aichi and... Of Course..."
    "Kai" "This is Miwa... Taishi. He plays Kagero... Is an Aries... And..."
    "Kai" "Likes long walks along the beach?"
    "Miwa" "Really?"
    "Ren" "Shop assistant huh?"
    "Ren" "You'll do, c' mon."
    "Miwa" "huh?"

    $ kai_fin = True
    #check if both endings played, then goto secret ending.
    
label kaichihoneymoon:
    "Blabla"
    
    return
