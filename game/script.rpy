# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg cc = "backgrounds/cfv_april_cardcapital.png"
image bg store = "backgrounds/cfv_april_storeroom.png"
image bg park = "backgrounds/cfv_april_park.png"
image bg under = "backgrounds/cfv_april_underground.png"
image bg ffhq = "backgrounds/cfv_april_ffhq.png"
image bg ffhqi = "backgrounds/cfv_april_ffhqinside.png"
image bg ffhqr = "backgrounds/cfv_april_ffhqren.png"
image bg hotel = "backgrounds/cfv_april_bar.png"

image miwa base = "sprites/cfv_april_miwa_basic.png"
image miwa prop = "sprites/cfv_april_miwa_propose.png"
image miwa diss = "sprites/cfv_april_miwa_dissapoint.png"
image miwa think = "sprites/cfv_april_miwa_thinking.png"
image miwa appal = "sprites/cfv_april_miwa_appaled.png"
image miwa angry = "sprites/cfv_april_miwa_angry_defence.png"
image miwa point = "sprites/cfv_april_miwa_angry_offence.png"
image miwa shock = "sprites/cfv_april_miwa_shocked.png"
image miwa embar = "sprites/cfv_april_miwa_embarassed.png"

image kai base = "sprites/cfv_april_kai_base.png"

image misa base = "sprites/cfv_april_misaki_base.png"

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
    
    scene bg cc
    "A shot of a deck being taken from table, and put into a bag."
    
    "Flash"
    
    "Boy" "my deck is gone!"
    #Closeups of Misaki, Kai and Miwa.#
    "And it was such a quiet day too..."
    scene bg cc
    show misa base at left
    mis "What is going on?"
    "Boy" "My deck is missing!"
    mis "Ah, everyone, did anyone see this boy's deck? The clan is..."
    "Boy" " Oracle Think-Tank."
    #Misaki looks shocked
    mis "...Oracle Think-Tank."
    #Miwa ace detective flashes on screen.
    #Shop is visible with kai, misaki and miwa figures.
    show miwa base at left
    show misa base at right
    miw "So this kid was distracted and poof, and someone nicked the deck while he wasn't looking?"
    mis "I saw that the boy was playing, and next thing his deck is stolen."
    miw " And neither you or the assistant-manager saw anything? Anyone leave the shop?"
    mis "No, not at all."
    miw "That's new."
    mis "Ayup."
    show miwa think at left
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
    show miwa prop at left
    miw "Exactly"
    #Misaki realising something
    mis "C'mon!"
    
    #Storeroom background, Misaki figure appears.
    scene bg store with fade
    show miwa shock at left
    show misa base at right
    miw "There's noone here."
    mis "But that's impossible..."
    show miwa think at left
    miw "Hm... Let's see what we can find."
label investigate:    
    #Player has the ability to check things out now: *door, breadcrumbs, the stocks*
    show miwa think at left
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
    show miwa point at left
    miw "Aha! Breadcrumbs! Get me some iodine!"
    mis "What? You mean to check for starch?"
    show miwa base at left
    miw "Indeed, my dear Misaki!"
    #misaki annoyed
    mis "Can't you do something normal? Like, fingerprinting? Or going to the police?"
    show miwa prop at left
    miw "Well, that's elementary, isn't it? The police won't take us seriously at all! And what are we supossed to fingerprint in the first place?"
    mis "Right, but... Miwa, all bread contains starch, so iodine isn't going to solve this case."
    #misaki embarrased
    mis "Besides, those are mine, I had a snack after changing the posters yesterday."
    show miwa diss at left
    miw "Fine."
    $ in_bread = True
    if in_stocks and in_fire and in_bread:
        jump investigateconclude
    else:
        jump investigate
label qstocks:
    #the stocks
    show miwa base at left
    miw "(Misaki is looking at the stocks...)"
    mis "If they stole a deck, who knows what else they've stolen"
    #Misaki looks relieved#
    mis "I can't see anything missing."
    #Miwa smiles
    show miwa prop at left
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
    show miwa embar at left
    miw "Sorry."
    show miwa think at left
    miw "(but we now know the thief didn't leave through here.)"
    $ in_fire = True
    if in_stocks and in_fire and in_bread:
        jump investigateconclude
    else:
        jump investigate
label investigateconclude:
    #conclusion
    #mis "Let's give up, there's nothing here..."
    scene bg cc with fade
    kai "And?"
    show kai base at left
    show miwa diss at right
    miw "Dead end..."
    #Misaki sad
    show misa base at right
    show miwa base at center with move
    miw "Hey..."
    show miwa prop at center
    miw "Don't worry! We'll find the thief."
    kai "Miwa."
    kai "Maybe you're better off looking for the thief outside."
    #miwa mirrored
    show miwa prop at center
    miw "Good plan!"
    show miwa think at left
    show kai base at center
    with move
    miw "Where should I start...hm..."
    hide miwa with disolve
    kai "Tokura!"
    show kai base at left with move
    #Kai asking who should go with Miwa
    show misa base at right
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
    scene bg park
    mis "Miwa, I'm coming with you!"
    miw "Ah?"
    miw "Oh, I didn't realise you'd want to find this guy too"
    Misaki looks sad
    miw "(Damnit...)"
    miw "(They don't have many expressions, but a sad one is the last I would like to see on their faces...)"
    miw "Let's do our best."
    mis "Yeah..."
    mis "Do you have any idea where to look?"
    show miwa shock
    miw "Ah..."
    show miwa think
    miw "Oracle Think-Tank is pretty expensive these days, isn't it?"
    show misa base
    mis "Yeah, it's a pretty popular clan. That kid had some SPs in his deck as well."
    miw "Alright, there might be a place where I think they might know something..."
    scene bg under with fade
    #Visiting Jun
    show miwa base center
    show misa base left
    miw "This is the spot."
    mis "This place... they hold underground fights here, don't they?"
    mis "How did you find it in the first place?"
    jun "Miwa!"
    show miwa shock at center
    jun "I haven't seen you around lately!"
    jun "Did you mind being tied up that much?"
    mis "Oh, I suposse that answers my question."
    show miwa appal at center
    miw "What? "
    extend "No!"
    show miwa appal at center
    miw "It's not what it sounds like!"
    extend "Don't go thinking crazy things now!"
    #Misaki looks amused
    mis "Too late for that."
    jun "You really have the best friends."
    jun "But if you've come to deliver another one of his girlfriends, he isn't here right now."
    miw "I'm not, don't worry."
    miw "Where to start explaining..."
    #screen fades to black for a bit
    miw "So, we figured you might know something..."
    jun "Hm..."
    jun "I haven't heard of any decks being pawned yet,"
    extend "and frankly noone here plays Think-tank."
    jun "But, "
    extend "the Foo-Fighters recruited a real Think-tank heavy weight recently."
    jun "You might want to ask them if they know anything."
    miw "I see..."
    miw "Thanks!"
    jun "Just visit more often, will you?"
    miw "Right."
    miw "Let's go!"
    hide miwa
    hide misa
    jun "He didn even answer me, did he?"
    
    #Visiting Ren
    scene bg ffhqi with fade
    miw "Now, let's see if we can find that guy..."
    mis "Ah!"
    miw "What is it?"
    mis "Look"
    #boy is shown
    miw "No way."
    
    #Misaki comes to the conclusion this was set up by Kai somehow and goes out to murder him.
    ren "Ah? Where is everyone?"
    "Boy" "They left for some reason."
    ren "Really? That's no fun..."
    asa "Ren-sama! Why did you try to get that Tokura girl here anyway?"
    ren "Asaka!"
    ren "Ah, I needed some help with moving furniture!"
    ren "I can't ask that of you, my dear..."
    asa "What? I'm an expert a moving things!"
    ren "Really?"
    asa "Why yes, I'm like,"
    extend "a genuine moverella!"
    ren "Oh, well in that case..."
    #scene fade
    scene bg cc with fade
    mis "Kai Toshiki!"
    extend "Did you think you could get away with this?"
    kai "Why the hell are you yelling at me, Tokura?"
    mis "You knew about this, you!"
    kam "What the hell?"
    miw "I'm not really sure what is going on either..."
    kam "..."
    kam "Want me to hold him while you punch him?"
    show miwa prop
    miw "Aren't you a little short for that?"
    kam "That's what you think."
    kai "Maybe it's time you learn the world doesn't revolve around you Tokura!"
    mis "Really, that's rich coming from you!"
    miw "I don't think she needs any help though..."
    kam "I guess you're right."
    kam "Hey, you up for a game?"
    miw "Sure."
    hide scene bg cc with fade
    "Thankfully, Kai and Misaki got past their misunderstanding eventually."
    "Man, this day was strange..."
    "Congratulations, you've finished Misaki's route!"
    $ persistent.misaki_fin = True
    #check if both endings played, goto secret ending
    if persistent.misaki_fin and persistent.kai_fin:
        jump kaichihoneymoon
    else:
        return
label kairoute:
    
    #Kai's route
    #Meeting with Aichi
    scene bg park
    show miwa prop at right
    miw "Aha! I see now, it must be his evil twin brother!"
    ai "No way!"
    kai "..."
    #Visiting Ren
    scene bg ffhqi
    ren "Kai, what a surprise to see you!"
    ai "Ren!"
    ren "And Aichi too, you three are the only ones?"
    kai "Ren, why did you ask that kid to pretend his deck was stolen?"
    ren "Ah, well..."
    ren "I had hoped on visit from a lovely shop assistant."
    kai "I did bring one."
    show miwa base at right
    miw "Hi!"
    ren "Hm? Detective, Shop assistant, you're quite versatile, aren't you?"
    ren "But I had hoped on someone with wider hips."
    kai "She didn't feel like coming."
    ren "Really now?"
    ren "Oh well, at the least we have Aichi and... Of Course..."
    kai "This is Miwa... Taishi. He plays Kagero... Is an Aries... And..."
    kai "Likes long walks along the beach?"
    show miwa diss at center
    miw "Really?"
    ren "Shop assistant huh?"
    ren "You'll do, c' mon."
    show miwa shock at center
    miw "huh?"
    #ren ""
    #miw ""
    "Ren is a little strange, but we had fun."
    "Kinda had muscleaches next day though..."
    "Man, this day was strange..."
    "Congratulations, you've finished Kai's route!"

    $ persistent.kai_fin = True
    #check if both endings played, then goto secret ending.
    if persistent.misaki_fin and persistent.kai_fin:
        jump kaichihoneymoon
    else:
        return
    
label kaichihoneymoon:
    "You've finished both endings, I guess I should give you what you came for..."
    "Alright, I'm ready."
    scene bg hotel with fade
    ai "Ah"
    ai "Kai-kun"
    kai "Aichi,"
    extend "what the hell are you wearing?"
    ai "Kai-kun! That should be obvious!"
    #kai-kun looks disturbed now
    ai "Despite me identifying like a boy, I look like a girl, so therefore I like dressing like one!"
    ai "Kai-kun, don't you know anything about gender-politics?"
    kai "Eh..."
    ai "I knew I should've gone to Ren-san with this."
    ai "At the least he's mature enough to... deal with my needs."
    kai "W-what?"
    ai "Sayonara, Kai-kun!"
    #aichi goes off-screen
    kai "What?"
    #pause
    ai "Kai-kun?"
    #aichi moves on screen
    ai "April-fools, Kai-kun!"
    kai "What...?"
    ai "April-fools!"
    kai "This was fake."
    extend " Good."
    ai "I didn't scare you too much, did I?"
    kai "No. You didn't."
    extend " But."
    extend "What was this about Ren being more mat-"
    ai "Ah, Kai-kun?"
    ai "Would you mind if I... slip into something more comfortable?"
    kai "-ure, what?"
    ai "I would like to go change into my regular clothes now,"
    extend "this is really embarassing to wear in public..."
    kai "Eh."
    kai "Yes, you do that!"
    #Aichi leaves
    kai "(What the flying fuck?)"
    
    hide scene bg hotel with fade
    "Happy April Fools, everyone!"
    "Credits: Story/Programming/Art: Wolthera (wolthera.tumblr.com) (go congratulate her, April the first is her birthday!)"
    "Testing:"
    ""
    
    return
