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

    define C = Character("Conrad" , color = "#7289DA")
    define A = Character("Anne" , color = "#ff7f50")
    define P = Character("Player_name" , color = "#3cd070")
    scene black




label start:



    scene bg room



    "You've created a new Ren'py game."

    "Once you add a story, pictures and music, you can release it to the world!"

    $ P = renpy.input("What is your name?")

    $ P = P.strip()
    $ P.lower()

label name:


    if P == '' :
        $ P = P.title()
        "ERROR. ERROR. NAME NOT DETECTED."
        "INITIATING MALWARE DOWNLOAD"
        jump splashscreen

    if P == 'Donovan':
        $ P = P.title()
        "Bruh"

    if P == 'Anthony':
        $ P = P.title()
        "Are you a fan of Salad and Doritoes?"

    if P == 'Ant':
        $ P = P.title()
        "Squish it"

    if P == 'Eli':
        $ P = P.title()
        "Hey Eli, remember those graphics you were supposed to make?"

    if P == 'Hunter' :
        $ P = P.title()
        "Praise Lord Cthulhu!"

    if P == 'Francine':
        $ P = P.title()
        "Tsukasa sucks lol."
        "KSDKSDKSDKSD It's Joke"

    if P == 'Credits':
        $ P = P.title()
        jump splashscreen

    if P == 'Maki' :
        $ P = P.title()
        "That's a pretty name!"

    if P == 'Speachbyte':
        $ P = P.title()
        "I'm the coolest"

    if P == 'Kyle':
        $ P = P.title()
        "I'm the coolest!"

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
