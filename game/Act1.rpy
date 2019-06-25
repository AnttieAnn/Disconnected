#Randomized Splash screen


label act1:


    "it's around 7:30 PM"
    "I had just finished eating some dinner, and was headed up to my room."
    "It was Monday, so that was when all my friends got together to play games"
    "I walk into my room, and sit down at my desk"

menu:

    "I've got about 30 minutes to kill before my friends are ready, what should i do to kill time?"

    "Watch Anime":

        jump weeb

    "Open discord" :

        jump servers

label servers:
    $ notifschecked = True
    $ weeb = False
    "I see notifictions from a few of my servers."

menu:

    "Which server should I click on first?"

    "The Omnia League":

        jump Omnia

    "MINECRAFT":

        jump minecraft

    "Discord Hack Week" :

        jump DHW


label omnia:
    "This server is pretty neat i ugess, the people in it are cool."
    "But the notification? It was just the server owner pinging all 80+ members while posting a really weird image."
    "It's a bug shooting laser out of his eyes saying 'silence brand'"
    "Why the hell would anyone use an @ everyone on that?"
    "I won't say anything, but I just watch the general channel get mad at the server owner for a bit"
    "I see a majority of these messages are just shitposters saying 'Bruh'"
    "Next thing i know 30 minutes pass, and I see my group chat is ready"
    jump gc1

label minecraft:
    "This is just a placeholder lol"
    jump gc1
label DHW:
    "Discord is holding some kind of contest for it's users."
    "Not gonna enter, it looks really cool, but I don't have the creative bone in my body."
    "I'd love to write a visual novel or something, but I have no idea how to make a story about being on discord."
    "Someone will though, and I bet that it'll be really cool."
    "This server is really funny though, the discord mods had to active a 1- minute slowmode, and people do nothing but complain about it"
    "I should ask Anne if she's entering it, she was always really creative."
    "I know it's a bit early, but let me hit her up and see if she's entering."
    jump anneDM1


label weeb:
    "I put on my favoite anime."
    "It's about this really cute purple haird girl who becomes a graphics designer for video games"
    "In this episode, it looks like she's entering a contest of some kind."
    "I watch the episode, a good half hour passes, and my group chat is ready to go."
    jump gc1

label anneDM1:
    return
label gc1:
    return
