#Randomized Splash screen


label act1:

    "The time is 11:58 PM, I'm playing GAME NAME with some of my close online friends"
    show Csmileo
    C "That was a great battle, guys! We made a lot of progress in-game so far."
    hide Csmileo
    show Aspeak1o
    A "*yawns* Yeah, it was really fun. I’m really tired, though."
    hide Aspeak1o
    #Anne close her mouth
    show ABspeak1c at midtoleft
    show Cspeako at right with dissolve
    C "Hey, how are you tired? I’m the one who’s three hours ahead of you and I’m totally energized after that battle!"
    hide Cspeako
    show Cspeakc at right
    P "Sometimes I forget that you live on the east coast, Conrad."
    hide ABspeak1c
    show Aspeak1o at left
    A "Oh well, It’s past 11 PM. "
    A "I should go to sleep. And so should both of you, too."
    hide Aspeak1o
    show Aspeak1c at left
    hide Cspeakc
    show Csmileo at right
    C "No way! There’s gonna be a huge in-game event on Friday. We have to grind as much as we can until then."
    hide Aspeak1c
    hide Csmileo
    show Cspeakc at right
    show Aspeak1o at left
    A "If anything, [P] and I are the ones who have to grind. You’ve been playing this game non-stop! "
    A "I swear, ever since you graduated most of your free time is spent either being on Discord or killing zombies."
    hide Aspeak1o
    show Aspeak1c at left
    hide Cspeakc
    show Cspeako at right
    C "Yeah, but I have a lot more fun playing when I’m with you guys!"
    hide Cspeakp
    show Cspeakc at right
    P "That’s true. I’m always having a good time whenever we’re voice chatting no matter what we’re doing together."
    hide Cspeakc
    hide Cspeako
    hide Aspeak1c
    "*ping*"
    show Aarmsb1u
    A "What was that sound?"
    hide Aarmsb1u
    show Aarmsb1u at midtoleft
    show Cidleo at right with dissolve
    C "Oh, uh- sorry! Just a notification, no biggie."
    hide Aarmsb1u
    hide Cidleo
    show Cspeako
    C "I guess we’ll have to leave the game here and continue later."
    hide Cspeako
    show Csmilec
    C "Both of you better be playing tomorrow! It’s going to take a while before you’re both the same level as me. I’m already super prepared for Friday’s event."
    C "Goodnight!"
    hide Csmilec
    "Conrad leaves the call in a hurry"

    show Aarmsb1d
    A "*yawn* I’m already on the verge of passing out. Goodnight, Con- "
    hide Aarmsb1d
    show Aarmsb1u
    A "Oh, he’s already gone."
    A "Looks like it’s just you and me, [P]. "
    hide Aarmsb1u
    show Aarmsf1u
    A "Conrad really wants us to participate on friday’s event, so we’ll pick up where we left off tomorrow in order to prepare."
    A "I have no idea where that boy gets his energy. It’s barely midnight and I’m already so sleeeeeee-"
    hide Aarmsf1u
    "(Anne starts to mumble, she fell asleep in Voice Chat... again.)"
    menu:
        "Let her sleep.":
            $ sleepscare = "non"
            A "zzzzz"
            "You decide to leave the call."
        "Wake her up.":
            $ sleepscare = "ye"
            show Aangry1
            A "ahhHHHH"
            hide Aangry1
            "You decide to leave the call before Anne has time to yell at you."

    show Aarmsb1d
    A "I can’t believe I fell asleep in voice chat again."
    show Aarmsb1u
    P "Did you get a good night’s sleep?"
    hide Aarmsb1u
    hide Aarmsb1d
    if sleepscare == "non":
        $ Aholepoints = Aholepoints - 1
        #subtract asshole point
        jump goodsleep
    if sleepscare == "ye":
        $ Aholepoints = Aholepoints + 1
        #add asshole points
        jump badsleep
label goodsleep:
    show Ahappy1o
    A "One of my best nights in weeks!"
    A "I appreciate you letting me sleep, I was really tired last night."
    A "I fell asleep faster than you running away from zombies."
    hide Ahappy1o
    jump ripconrad
label badsleep:
    show Aangry1
    A "No thanks to you! Your little stunt last night terrified me!"
    A "Although, I think I scared you more than you scared me."
    A "You ran out of that call faster than me running away from zombies."
    hide Aangry1

label ripconrad:
    show Aarmsb1u
    A "At least I didn’t fall asleep with Conrad in the call or else he would have tried to jumpscare me."
    hide Aarmsb1u
    show Aangry1
    A "Last time I fell asleep in voice chat I woke up with a massive headache and the dubstep nightcore version of the WumpCraft OST blasting from Conrad’s end."
    hide Aangry1
    show Aspeak1o
    A "Oh well, I don’t really have any plans for today. Speaking of WumpCraft, do you want to play a session?"
    show Aspeak1c
    P "Conrad isn’t online yet."
    hide Aspeak1c
    A "Huh, that’s weird. He’s usually always the first one up and the last one to go to sleep."
    A "We were up pretty late last night, maybe he’s all tired out?"
    A "He did say that he’s already prepared for Friday’s event, so we should try to grind a bit while he’s gone in order to catch up to him in levels."
    show Aspeak1c
    P "Yeah, I agree."
    hide Aspeak1c
    hide Aspeak1o

    "(An awkward pause)"
    show Aarmsf1u
    P "Um, should you start the call or should I?"
    A "Oh! Right... I forgot."
    A "Conrad is usually the one who starts all our calls. It’s been a while with just the two of us, I’m not used to it."
    A "You can decide who starts the call."
    hide Aarmsf1u

    menu:
        "You start the call.":
            P "I can start the call."
            show Ahappy1o
            A "Oh good! I was hoping you'd do it actually."
            hide Ahappy1o
            show Aspeak1o
            A "I mean it's not like I don't know where the call button is or anything."
            hide Aspeak1o

        "Let her start the call.":
            show Aarmsf1u
            A "..."
            P "...?"
            hide Aarmsf1u
            show Aarmsf1d
            A "I uh, don't know how to start the call."
            hide Aarmsf1d
            "*Resisting the urge to laugh, you help Anne out with starting the call.*"

label ripconradcall:
    P "Ouch! That enemy did a lot of damage."
    show Aspeak1o
    A "Here, I have some medicine. I don’t know if it’s enough, though."
    hide Aspeak1o

    "(Anne heals [P] by a small amount)"
    show Aarmsb1u
    A "I never realized how difficult these enemies were. Usually, Conrad would take care of the tougher enemies and we’d get the EXP and loot."
    hide Aarmsb1u
    show Aarmsb1d
    A "This would be a lot easier if he was here…"
    hide Aarmsb1d
    show Aarmsb1u
    A "I keep checking his online status and he’s still offline. That’s a rare sight to see."
    P "Let’s keep going until he gets online."
    hide Aarmsb1u
    show Aspeak1o
    A "I’m all out of medicine, so we’ll have to be care- watch out, [P]!"
    hide Aspeak1o
    "(A horde of zombies chases after Anne and [P]. They retreat back to base and kill off some lower level enemies while they wait for Conrad.)"
    "(Most of their game session has been filled with silence with Conrad gone.)"
    P "You’re awfully quiet, Anne."
    show Aarmsf1d
    A "Hm? Sorry, I’m not really good with starting conversations. That’s always been Conrad’s strong suit."
    P "Yeah, he’s always been the talkative one compared to the two of us."
    A "Yeah..."
    P "…"
    hide Aarmsf1d
    show Aarmsf1u
    A "…"
    hide Aarmsf1u
    show Aspeak1o
    A "… Um, so, We’ve been fighting off these enemies for a while now. It’s getting kind of tedious. What do you want to do now?"
    hide Aspeak1o
menu:
        "Start a conversation.":
            show Aspeak1c
            P "How's the weather"
            show Aspeak1o
            A "Well it says it's gonna rain for at least few minutes, probably a few more in game days."
            hide Aspeak1o
            P "No I meant in real life."
            hide Aspeak1c
            show Aarmsb1u
            A "Oh!"
            P "..."
            hide Aarmsb1u
            show Aarmsb1d
            A "It's uh, nice, a little hot even though it's the middle of the night."
            P "That's nice."
            hide Aarmsb1d

        "Suggest fighting some enemies.":
            P "We should go back to the caves."
            show Aarmsf1d
            A "Are you sure, I'd love to mine some materials but remember what Conrad would say?"
            hide Aarmsf1d
            show Aarmsf1u
            A "'Don't mine at night, even if you're feelin kinda brave'"
            hide Aarmsf1u
            show Ahappy1o
            A "But you know what? We can at least go after some of the stronger enemies in there, we should have an easier time since I have this fancy blue sword now."
            hide Ahappy1o
            "Despite having a fancy sword, you did not have an easier time with enemies."
            "Minutes Later..."
            show Aarmsf1d
            A "Well that didn't end well."
            A "Man I'm really tired after that."
            hide Aarmsf1d

label location:
    show Aspeak1o
    A "Hey you live pretty close to me right?"
    hide Aspeak1o
    show Aspeak1c
    P "I mean, San Francisco is a couple hours away. LA."
    hide Aspeak1c
    show Ahappy1o
    A "Okay first of all, I live in Glendale." #She isn't offended here, use her playful/happy emotes.
    hide Ahappy1o
    show Ahappy1c
if Aholepoints == 1:
    jump ahole1
if Aholepoints == -1:
    jump location2
label ahole1:
    P "Okay so Los Angeles negative, my bad."
    #jump
label location2:
    A "Second,"
