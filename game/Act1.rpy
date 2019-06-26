#Randomized Splash screen


label act1:
    "The time is 11:58 PM, I'm playing GAME NAME with some of my close online friends"

    C "That was a great battle, guys! We made a lot of progress in-game so far."
    show Aspeak1o
    A "*yawns* Yeah, it was really fun. I’m really tired, though."
    hide Aspeak1o
    show Aspeak1c at left
    C "Hey, how are you tired? I’m the one who’s three hours ahead of you and I’m totally energized after that battle!"
    
    P "Sometimes I forget that you live on the east coast, Conrad."
    A "Oh well, It’s past 11 PM. "
    A "I should go to sleep. And so should both of you, too."
    C "No way! There’s gonna be a huge in-game event on Friday. We have to grind as much as we can until then."
    A "If anything, _ and I are the ones who have to grind. You’ve been playing this game non-stop! "
    A "I swear, ever since you graduated most of your free time is spent either being on Discord or killing zombies."
    C "Yeah, but I have a lot more fun playing when I’m with you guys!"
    P "That’s true. I’m always having a good time whenever we’re voice chatting no matter what we’re doing together."
    C "*ping*"
    A "What was that sound?"
    C "Oh, uh- sorry! Just a notification, no biggie."
    C "I guess we’ll have to leave the game here and continue later."
    C "Both of you better be playing tomorrow! It’s going to take a while before you’re both the same level as me. I’m already super prepared for Friday’s event."
    C "Goodnight!"

    "Conrad leaves the call in a hurry"

    A "*yawn* I’m already on the verge of passing out. Goodnight, Con- "
    A "Oh, he’s already gone."
    A "Looks like it’s just you and me, _. "
    A "Conrad really wants us to participate on friday’s event, so we’ll pick up where we left off tomorrow in order to prepare."
    A "I have no idea where that boy gets his energy. It’s barely midnight and I’m already so sleeeeeee-"
    "(Anne starts to mumble, she fell asleep in Voice Chat... again.)"
    menu:
        "Let her sleep.":
            $ sleepscare = "non"
            A "zzzzz"
            "You decide to leave the call."
        "Wake her up.":
            $ sleepscare = "ye"
            A "ahhHHHH"
            "You decide to leave the call before Anne has time to yell at you."

            A "I can’t believe I fell asleep in voice chat again."
            P "Did you get a good night’s sleep?"
            if sleepscare == "non":
                jump goodsleep
            if sleepscare == "ye":
                jump badsleep
label goodsleep:
    A "One of my best nights in weeks!"
    A "I appreciate you letting me sleep, I was really tired last night."
    A "I fell asleep faster than you running away from zombies."
    jump ripconrad
label badsleep:
    A "No thanks to you! Your little stunt last night terrified me!"
    A "Although, I think I scared you more than you scared me."
    A "You ran out of that call faster than me running away from zombies."
label ripconrad:
    A "At least I didn’t fall asleep with Conrad in the call or else he would have tried to jumpscare me."
    A "Last time I fell asleep in voice chat I woke up with a massive headache and the dubstep nightcore version of the WumpCraft OST blasting from Conrad’s end."
    A "Oh well, I don’t really have any plans for today. Speaking of WumpCraft, do you want to play a session?"
    P "Conrad isn’t online yet."
    A "Huh, that’s weird. He’s usually always the first one up and the last one to go to sleep."
    A "We were up pretty late last night, maybe he’s all tired out?"
    A "He did say that he’s already prepared for Friday’s event, so we should try to grind a bit while he’s gone in order to catch up to him in levels."
    P "Yeah, I agree."

    "(An awkward pause)"

    P "Um, should you start the call or should I?"
    A "Oh! Right... I forgot."
    A "Conrad is usually the one who starts all our calls. It’s been a while with just the two of us, I’m not used to it."
    A "You can decide who starts the call."
    menu:
        "You start the call.":
            P "I can start the call."
            A "Oh good! I was hoping you'd do it actually."
            A "I mean it's not like I don't know where the call button is or anything."
        "Let her start the call.":
            A "..."
            P "...?"
            A "I uh, don't know how to start the call."
            "Resisting the urge to laugh, you help Anne out with starting the call."
label ripconradcall:
    P "Ouch! That enemy did a lot of damage."
    A "Here, I have some medicine. I don’t know if it’s enough, though."
    "(Anne heals _ by a small amount)"

    A "I never realized how difficult these enemies were. Usually, Conrad would take care of the tougher enemies and we’d get the EXP and loot."
    A "This would be a lot easier if he was here…"
    A "I keep checking his online status and he’s still offline. That’s a rare sight to see."
    P "Let’s keep going until he gets online."
    A "I’m all out of medicine, so we’ll have to be care- watch out, _!"
    "(A horde of zombies chases after Anne and _. They retreat back to base and kill off some lower level enemies while they wait for Conrad.)"
    "(Most of their game session has been filled with silence with Conrad gone.)"
    P "You’re awfully quiet, Anne."
    A "Hm? Sorry, I’m not really good with starting conversations. That’s always been Conrad’s strong suit."
    P "Yeah, he’s always been the talkative one compared to the two of us."
    A "Yeah..."
    P "…"
    A "…"
    A "… Um, so, We’ve been fighting off these enemies for a while now. It’s getting kind of tedious. What do you want to do now?"
