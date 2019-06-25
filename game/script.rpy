#Randomized Splash screen
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

    define b = Character("Bruh 1" , color = "#c8ffc8")
    define a = Character("Anne")
    define p = ("Player_name")
    scene black




label start:



    scene bg room





    "You've created a new Ren'py game."

    "Once you add a story, pictures and music, you can release it to the world!"

    $ player_name = renpy.input("What is your name?")

    $ player_name = player_name.strip()
    $ player_name.lower()

label name:


    if player_name == '' :
        $ player_name = "bruh"
        "ERROR. ERROR. NAME NOT DETECTED."
        "INITIATING MALWARE DOWNLOAD"
        jump splashscreen

    if player_name == 'donovan':
        $ player_name = "Donovan"
        "Bruh"

    if player_name == 'anthony':
        $ player_name = "Anthony"
        "Are you a fan of Salad and Doritoes?"

    if player_name == 'ant':
        $ player_name = "Ant"
        "Squish it"

    if player_name == 'eli':
        $ player_name = "Eli"
        "Hey Eli, remember those graphics you were supposed to make?"

    if player_name == 'hunter' :
        $ player_name = "Hunter"
        "Praise Lord Cthulhu!"

    if player_name == 'francine':
        $ player_name = "Francine"
        "Tsukasa sucks lol."
        "KSDKSDKSDKSD It's Joke"

    if player_name == 'credits':
        $ player_name = "Credits"
        jump splashscreen

    if player_name == 'maki' :
        $player_name = "Maki"
        "That's a pretty name!"

    if player_name == 'speachbyte':
        $ player_name = "Speachbyte"
        "I'm soo cool"

    if player_name == 'kyle':
        $ player_name = "Kyle"
        "I'm soo cool!"

    if player_name == 'umi':
        $ player_name = "Umi"
        "That's a beautiful name"

    if player_name == 'restart':
        $ player_name = "Restart"
        jump splashscreen

label keywords:
    $ color = renpy.input("What is your favorite color?")
    $ color.lower()
    if (color.find('monika') != -1) :
        "Hey that's a cool color"
        jump splashscreen
    else :
        "You have a cool taste of color"
        jump act1
