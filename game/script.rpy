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
image bg black = "sfx/black.png"

image cg deckgrab  = "sfx/black.png"
image cg yell  = "sfx/cg_stolen.png"
image cg run  = "sfx/black.png"
image cg kai  = "sfx/black.png"
image cg aichi  = "sfx/black.png"

image ikai  = "sfx/fx_kaishock.png"
image imiwa  = "sfx/fx_miwashock.png"
image imisa  = "sfx/fx_misashock.png"
image logo_miwa = Image("sfx/logo_miwa.png")
image logo_kaichi = Image("sfx/logo_kaichi.png")
image ibread = "sfx/black.png"
image istock = "sfx/black.png"
image ifire = "sfx/black.png"
image imagazine = "sfx/black.png"


image miwa base = Image("sprites/cfv_april_miwa_basic.png", xanchor=0.3)
image miwa prop = "sprites/cfv_april_miwa_propose.png"
image miwa diss = "sprites/cfv_april_miwa_dissapoint.png"
image miwa think = "sprites/cfv_april_miwa_thinking.png"
image miwa appal = "sprites/cfv_april_miwa_appaled.png"
image miwa angry = "sprites/cfv_april_miwa_angry_defence.png"
image miwa point = "sprites/cfv_april_miwa_angry_offence.png"
image miwa shock = "sprites/cfv_april_miwa_shocked.png"
image miwa embar = "sprites/cfv_april_miwa_embarassed.png"

image miwa basem = "sprites/cfv_april_miwa_basic_m.png"
image miwa propm = "sprites/cfv_april_miwa_propose_m.png"
image miwa dissm = "sprites/cfv_april_miwa_dissapoint_m.png"
image miwa thinkm = "sprites/cfv_april_miwa_thinking_m.png"
image miwa appalm = "sprites/cfv_april_miwa_appaled_m.png"
image miwa angrym = "sprites/cfv_april_miwa_angry_defence_m.png"
image miwa pointm = "sprites/cfv_april_miwa_angry_offence_m.png"
image miwa shockm = "sprites/cfv_april_miwa_shocked_m.png"
image miwa embarm = "sprites/cfv_april_miwa_embarassed_m.png"

image kai base = "sprites/cfv_april_kai_base.png"
image kai anno = "sprites/cfv_april_kai_annoyed.png"
image kai skep = "sprites/cfv_april_kai_skeptical.png"
image kai conf = "sprites/cfv_april_kai_confused.png"
image kai vcon = "sprites/cfv_april_kai_very_confused.png"
image kai happy = "sprites/cfv_april_kai_happy.png"

image misa base = "sprites/cfv_april_misaki_base.png"
image misa basem = "sprites/cfv_april_misaki_base_m.png"
image misa shock = "sprites/cfv_april_misaki_shocked.png"
image misa shockm = "sprites/cfv_april_misaki_shocked_m.png"
image misa smile = "sprites/cfv_april_misaki_smile.png"
image misa smilem = "sprites/cfv_april_misaki_smile_m.png"
image misa sad = "sprites/cfv_april_misaki_sad.png"
image misa sadm = "sprites/cfv_april_misaki_sad_m.png"
image misa anno = "sprites/cfv_april_misaki_annoyed.png"
image misa annom = "sprites/cfv_april_misaki_annoyed_m.png"
image misa angry = "sprites/cfv_april_misaki_angry.png"
image misa angrym = "sprites/cfv_april_misaki_angry_m.png"

image aichi base = "sprites/cfv_april_aichi_base.png"
image aichi basem = "sprites/cfv_april_aichi_base.png"
image aichi sbasem = "sprites/cfv_april_aichi_base.png"
#aichi shock
#aichi pens
#aichi smile

#kamui base
#kamui yell

#jun base
#jun think

#asaka upset

#ren base
#ren smile
#ren regard

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
    $ sleft =  Position(xalign=0.15, yalign=1.0, xanchor=0.3, yanchor=1.0)
    $ middle = Position(xalign=0.5, yalign=0.4, xanchor=0.5, yanchor=0.5)
    $ sleftm = Position(xalign=0.15, yalign=1.0, xanchor=0.6, yanchor=1.0)
    $ sright =  Position(xalign=0.85, yalign=1.0, xanchor=0.6, yanchor=1.0)
    $ srightm = Position(xalign=0.85, yalign=1.0, xanchor=0.6, yanchor=1.0)
    $ scenter = Position(xalign=0.5, yalign=1.0, xanchor=0.3, yanchor=1.0)
    $ scenterm = Position(xalign=0.5, yalign=1.0, xanchor=0.6, yanchor=1.0)
    $ flash = Fade(.25, 0, .75, color="#fff")
    $ in_bread = False
    $ in_stocks = False
    $ in_fire = False
    
    scene bg cc
    show imisa at offscreenleft
    show ikai at offscreenright
    show imiwa at offscreenright
    "A shot of a deck being taken from table, and put into a bag."
    
    "Flash"
    scene cg yell
    "Boy" "my deck is gone!"
    #Closeups of Misaki, Kai and Miwa.#
    show imisa at center with flash
    show ikai at center with flash
    show imiwa at center with flash
    $ renpy.pause(10)
    scene bg black with fade
    "And it was such a quiet day too..."
    scene bg cc with fade
    show misa base at sleft
    mis "What is going on?"
    "Boy" "My deck is missing!"
    show misa basem at sleftm
    mis "Ah, everyone, did anyone see this boy's deck? The clan is..."
    "Boy" " Oracle Think-Tank."
    #Misaki looks shocked
    show misa shock at sleft
    mis "...Oracle Think-Tank."
    #Miwa ace detective flashes on screen.
    scene bg black
    show logo_miwa at middle
    with flash
    $ renpy.pause(30)
    
    #Shop is visible with kai, misaki and miwa figures.
    scene bg cc
    show miwa base at sleft
    show misa basem at sright
    with fade
    miw "So this kid was distracted and poof, and someone nicked the deck while he wasn't looking?"
    mis "I saw that the boy was playing, and next thing his deck is stolen."
    miw " And neither you or the assistant-manager saw anything? Anyone leave the shop?"
    mis "No, not at all."
    miw "That's new."
    mis "Ayup."
    show miwa think
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
    show miwa prop
    miw "Exactly"
    show misa shockm
    mis "C'mon!"
    
    #Storeroom background, Misaki figure appears.
    scene bg store with fade
    show miwa shock at sleft
    show misa shockm at sright
    miw "There's noone here."
    mis "But that's impossible..."
    show miwa think
    show misa basem
    miw "Hm... Let's see what we can find."
label investigate:    
    #Player has the ability to check things out now: *door, breadcrumbs, the stocks*
    show miwa think
    show misa basem
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
    show miwa point at sleft
    miw "Aha! Breadcrumbs! Get me some iodine!"
    show misa shockm
    mis "What? You mean to check for starch?"
    show miwa base at sleft
    miw "Indeed, my dear Misaki!"
    show misa annom
    #misaki annoyed
    mis "Can't you do something normal? Like, fingerprinting? Or going to the police?"
    show miwa prop
    miw "Well, that's elementary, isn't it? The police won't take us seriously at all! And what are we supossed to fingerprint in the first place?"
    show misa basem
    mis "Right, but... Miwa, all bread contains starch, so iodine isn't going to solve this case."
    show misa annom
    mis "Besides, those are mine, I had a snack after changing the posters yesterday."
    show miwa diss
    miw "Fine."
    $ in_bread = True
    if in_stocks and in_fire and in_bread:
        jump investigateconclude
    else:
        jump investigate
label qstocks:
    #the stocks
    show miwa base at sleft
    show misa base at srightm
    miw "(Misaki is looking at the stocks...)"
    mis "If they stole a deck, who knows what else they've stolen"
    #Misaki looks relieved#
    show misa basem at sright
    mis "I can't see anything missing."
    #Miwa smiles
    show miwa prop at sleft
    miw "That's good."
    $ in_stocks = True
    if in_stocks and in_fire and in_bread:
        jump investigateconclude
    else:
        jump investigate
label qfireescape:
    #the fireescape
    miw "Can this door open?"
    show misa shockm
    mis "Miwa, wait!"
    #picture of door opening, fire alarm starts to ring
    show misa angrym
    mis "Now you've done it!"
    #screen goes black. firealarm cuts off.
    show misa annom
    mis "Next time, ask if you can open the Fire exit."
    show miwa embar
    miw "Sorry."
    show miwa think
    miw "(but we now know the thief didn't leave through here.)"
    $ in_fire = True
    if in_stocks and in_fire and in_bread:
        jump investigateconclude
    else:
        jump investigate
label investigateconclude:
    #conclusion
    #mis "Let's give up, there's nothing here..."
    scene bg cc
    show kai base at sleft
    with fade
    show miwa dissm at offscreenright
    show misa basem at offscreenright
    kai "And?"
    show miwa dissm at sright with move
    miw "Dead end..."
    #Misaki sad
    show misa sadm at sright 
    show miwa base at scenter
    with move
    miw "Hey..."
    show miwa prop
    miw "Don't worry! We'll find the thief."
    show kai skep
    kai "Miwa."
    kai "Maybe you're better off looking for the thief outside."
    #miwa mirrored
    show miwa basem at scenterm
    miw "Good plan!"
    show miwa thinkm at sleftm
    show kai base at center
    with move
    miw "Where should I start...hm..."
    #hide miwa with disolve
    show miwa thinkm at offscreenleft with move
    kai "Tokura!"
    show misa basem
    show kai base at sleft with move
    #Kai asking who should go with Miwa
    kai "Someone should go with him, the last time I left him to his own devices, I found him tied up by the backstreet boys."
    show misa smilem
    mis "Tell me why?"
    kai "No."
    show kai annoy
    kai "Ain't nothing but a headache."
    show kai base
    kai "Shall I go?"
    show misa basem
    mis "Hm..."
    menu:
        "I'll go.":
            jump misakiroute
        "Let Kai go":
            jump kairoute
        
label misakiroute:
    scene bg park
    show miwa base at scenter
    show misa base at sleft
    mis "Miwa, I'm coming with you!"
    show miwa shockm at scenterm
    miw "Ah?"
    show miwa basem
    miw "Oh, I didn't realise you'd want to find this guy too"
    #Misaki looks sad
    show misa sad
    show miwa thinkm
    miw "(Damnit...)"
    miw "(They don't have many expressions, but a sad one is the last I would like to see on their faces...)"
    show miwa propm
    miw "Let's do our best."
    mis "Yeah..."
    show misa anno
    mis "Do you have any idea where to look?"
    show miwa shockm
    miw "Ah..."
    show miwa thinkm
    miw "Oracle Think-Tank is pretty expensive these days, isn't it?"
    show misa base
    mis "Yeah, it's a pretty popular clan. That kid had some SPs in his deck as well."
    miw "Alright, there might be a place where I think they might know something..."
    scene bg under with fade
    #Visiting Jun
    show miwa base at scenter
    show misa base at sleft
    miw "This is the spot."
    show miwa basem at scenterm
    mis "This place... they hold underground fights here, don't they?"
    mis "How did you find it in the first place?"
    jun "Miwa!"
    show miwa shock at scenter
    jun "I haven't seen you around lately!"
    jun "Did you mind being tied up that much?"
    show misa anno
    mis "Oh, I suposse that answers my question."
    show miwa appalm at scenterm
    miw "What? "
    extend "No!"
    miw "It's not what it sounds like!"
    extend " Don't go thinking crazy things now!"
    show miwa angrym
    show misa smile
    #Misaki looks amused
    mis "Too late for that."
    jun "You really have the best friends."
    jun "But if you've come to deliver another one of his girlfriends, he isn't here right now."
    show misa base at scenter
    show miwa embar
    miw "I'm not, don't worry."
    show miwa think
    miw "Where to start explaining..."
    #screen fades to black for a bit
    scene bg black with fade
    $ renpy.pause(10)
    scene bg under
    show misa base at sleft
    show miwa prop at scenter
    with fade
    miw "So, we figured you might know something..."
    show miwa base
    jun "Hm..."
    jun "I haven't heard of any decks being pawned yet,"
    extend "and frankly noone here plays Think-tank."
    jun "But, "
    extend "the Foo-Fighters recruited a real Think-tank heavy weight recently."
    jun "You might want to ask them if they know anything."
    show miwa think
    miw "I see..."
    show miwa basem at scenterm
    miw "Thanks!"
    jun "Just visit more often, will you?"
    miw "Right."
    show miwa propm
    miw "Let's go!"
    show miwa basem at offscreenleft with move
    show misa basem at offscreenleft with move
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
    "Boy" "Ah, you guys?!"
    miw "Your deck was stolen, huh?"
    miw "You know what I think?"
    miw "your deck wasn stolen in the first place!"
    "Boy" "-tchk"
    miw "Instead, you took your deck with you!"
    miw "Misaki, nor the submanager would have suspected you of stealing your own deck!"
    mis "How dare you! I can't believe we favour the same clan!"
    "Boy" "Very nice, Detective."
    "Boy" "But tell me, what would be my motive?"
    miw "Well that's-"
    miw "Uhm..."
    mis "Suzugamori Ren..."
    mis "But that means!"
    #misaki runs off
    miw "Hey, where you going to?"
    #Miwa runs off after her
    #Misaki comes to the conclusion this was set up by Kai somehow and goes out to murder him.
    ren "Ah? Where is Misakki?"
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
    #hide scene bg cc with fade
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
    scene bg black
    "You've finished both endings, I guess I should give you what you came for..."
    "Alright, I'm ready."
    scene bg hotel with fade
    ai "Ah"
    ai "Kai-kun"
    show kai base at left
    #show aichi sbasm at right
    kai "Aichi,"
    show kai skep
    extend "what the hell are you wearing?"
    ai "Kai-kun! That should be obvious!"
    show kai anno
    #kai-kun looks disturbed now
    ai "Despite me identifying like a boy, I look like a girl, so therefore I like dressing like one!"
    ai "Kai-kun, don't you know anything about gender-politics?"
    show kai conf
    kai "Eh..."
    ai "I knew I should've gone to Ren-san with this."
    ai "At the least he's mature enough to... deal with my needs."
    show kai vcon
    kai "W-what?"
    ai "Sayonara, Kai-kun!"
    #aichi goes off-screen
    kai "What?"
    #pause
    ai "Kai-kun?"
    #aichi moves on screen
    ai "April-fools, Kai-kun!"
    show kai conf
    kai "What...?"
    ai "April-fools!"
    show kai skep
    kai "This was fake."
    show kai base
    extend " Good."
    ai "I didn't scare you too much, did I?"
    show kai skep
    kai "No. You didn't."
    extend " But."
    show kai anno
    extend "What was this about Ren being more mat-"
    ai "Ah, Kai-kun?"
    ai "Would you mind if I... slip into something more comfortable?"
    show kai conf
    kai "-ure, what?"
    ai "I would like to go change into my regular clothes now,"
    extend "this is really embarassing to wear in public..."
    show kai vcon
    kai "Eh."
    show kai base
    kai "Yes, you do that!"
    #Aichi leaves
    show kai vcon
    kai "(What the flying fuck?)"
    
    #hide scene bg hotel with fade
    scene bg black
    centered "Happy April Fools, everyone!"
    centered "Credits: Story/Programming/Art: Wolthera (wolthera.tumblr.com)
               (go congratulate her, April the first is her birthday!)"
    centered "Sound:"
    centered "Testing:"
    centered ""
    
    return
