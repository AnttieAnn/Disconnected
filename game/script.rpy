#Randomized Splash screen
label PrePrep :
    jump AnneI

label splashscreen:
    scene black
    with Pause(1)

    $ randomnum = renpy.random.randint(1,10)

    if randomnum >5 :
        show text "Omnia Studios Presents . . ." with dissolve
        with Pause(2)

        hide text with wipeleft
        with Pause(1)

    if randomnum == 2 :
        show text "Bruh" with dissolve
        with Pause(2)

        hide text with wipeleft
        with Pause(1)

    if randomnum == 3:
        show text "Attention Gamers. . ." with dissolve
        with Pause(2)

        hide text with wipeleft
        with Pause(1)

    if randomnum == 4 :
        return

    if randomnum == 5:
        show text "I-It's not like Omnia Studios WANTS to Present this... Baka..." with dissolve
        with Pause(2)
    return

    define C = Character("Conrad" , color = "#c8ffc8")
    define A = Character("Anne")
    define P = ("Player_name")
    scene black




label start:



    scene bg room


    "You've created a new Ren'py game."

    "Once you add a story, pictures and music, you can release it to the world!"

    $ P = renpy.input("What is your name?")

    $ P = P.lower()

label name:

    $ Aholepoints = 0
    if P == '' :
        $ P = P.title()
        "ERROR. ERROR. NAME NOT DETECTED."
        "INITIATING MALWARE DOWNLOAD"
        jump splashscreen

    if P == 'donovan':
        $ P = P.title()
        "Bruh"

    if P == 'anthony':
        $ P = P.title()
        "Are you a fan of Salad and Doritoes?"

    if P == 'ant':
        $ P = P.title()
        "Squish it"

    if P == 'eli':
        $ P = P.title()
        "Hey Eli, remember those graphics you were supposed to make?"

    if P == 'hunter' :
        $ P = P.title()
        "Praise Lord Cthulhu!"

    if P == 'francine':
        $ P = P.title()
        "Tsukasa sucks lol."
        "KSDKSDKSDKSD It's Joke"

    if P == 'credits':
        $ P = P.title()
        jump splashscreen

    if P == 'maki' :
        $ P = P.title()
        "That's a pretty name!"

    if P == 'speachbyte':
        $ P = P.title()
        "I'm soo cool"

    if P == 'kyle':
        $ P = P.title()
        "I'm soo cool!"

    if P == 'umi':
        $ P = P.title()
        "That's a beautiful name"

    if P == 'restart':
        $ P = P.title()
        jump splashscreen
    $ P = P.title()

label keywords:
    $ color = renpy.input("What is your favorite color?")
    $ color.lower()
    if (color.find('monika') != -1) :
        "Hey that's a cool color"
        jump splashscreen
    else :
        "You have a cool taste of color"
        jump act1
