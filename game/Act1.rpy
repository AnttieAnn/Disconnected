#Randomized Splash screen


label act1:
    $ AHP = 0
    "The time is 11:58 PM, and you're playing GAME NAME with some of your close online friends"
    show Csmileo
    C "That was a great battle, guys! We made a lot of progress in-game so far."
    hide Csmileo
    show Aspeak1o
    A "*yawns* Yeah, it was really fun. I’m really tired, though."
    hide Aspeak1o
    #Anne close her mouth
    show ABspeak1c at midtoleft
    show Cspeako at right with dissolve
    C "How are you tired? I’m the one who’s three hours ahead of you and I’m totally energized after that battle!"
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
    C "No way! There’s gonna be a huge in-game event on Friday. We have to level grind as much as we can until then."
    hide Aspeak1c
    hide Csmileo
    show Cspeakc at right
    show Aspeak1o at left
    A "If anything, [P] and I are the ones who have to level grind. You’ve been playing this game non-stop! "
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
            A "ahhHHHH"
            show Aangry1
            A "[P]?? What the hell?!?"
            hide Aangry1
            "You decide to leave the call before Anne has time to yell at you."

    show Aarmsb1d
    A "I can’t believe I fell asleep in voice chat again."
    show Aarmsb1u
    P "Did you get a good night’s sleep?"
    hide Aarmsb1u
    hide Aarmsb1d
    if sleepscare == "non":
        $ AHP -= 1
        #subtract asshole point
        jump goodsleep
    if sleepscare == "ye":
        $ AHP += 1
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
    A "He did say that he’s already prepared for Friday’s event, so we should try to level grind a bit while he’s gone in order to catch up to him in levels."
    show Aspeak1c
    P "Yeah, I agree."
    hide Aspeak1c
    hide Aspeak1o

    P "..."
    show Aarmsf1u
    P "Um, should you start the call or should I?"
    A "Oh! Right... I forgot."
    A "Conrad is usually the one who starts all our calls. It’s been a while with just the two of us, I’m not used to it."
    A "You can decide who starts the call."
    hide Aarmsf1u

    menu:
        "You start the call.":
            show Aarmsf1u
            P "I can start the call."
            hide Aarmsf1u
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
    "A horde of zombies chases after Anne and you. They retreat back to base and kill off some lower level enemies while they wait for Conrad."
    "Most of their game session has been filled with silence with Conrad gone."
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
            P "How's the weather?"
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
            show Aspeak1c
            P "We should go back to the caves."
            hide Aspeak1c
            show Aarmsf1d
            A "Are you sure, I'd love to mine some materials but remember what Conrad would say?"
            hide Aarmsf1d
            show Aarmsf1u
            A "'Don't mine at night, even if you're feelin kinda brave. Nothing will change if you just wait until day."
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
    if AHP == 1:
        jump ahole1
    if AHP == -1:
        jump location2
label ahole1:
    P "Okay so Los Angeles negative, my bad."
label location2:
    hide Ahappy1c
    show Ahappy1o
    A "Second, a couple hours away is pretty close considering that we only use discord to talk."
    A "I think it's a really cool coincidence that's all."
    A "Plus Conrad lives all the way out in Orlando, imagine how long of a drive THAT would be."
    hide Ahappy1o
    show Aarmsb1u
    A "Speaking of Conrad, where the heck is he?"
    P "That's weird, he's usually spamming our DMs right now."
    show Aarmsb1d
    hide Aarmsb1u
    A "Should I send him a message?"
    hide Aarmsb1d
    menu:
            "Nah, he's probably busy.":
                show Aarmsb1u
                P "Nah, he's probably busy."
                P "That, or he's sleeping still, since we last heard from him around 3 AM his time."
                hide Aarmsb1u
                show Aarmsb1d
                A "I don't know, it's weird. Conrad always dedicates his evening to gamer time."
                A "AND he always spends it with us, unless he's playing that stupid battle royale game."
                hide Aarmsb1d
                show Aangry1
                A "Man I HATE games where it's just 100 people fighting to the death."
                hide Aangry1
                show Aarmsb1d
                A "Anyway, I'm just worried him. I can't remember the last time he didn't at least DM us a good morning message."
                hide Aarmsb1d

            "Yeah you should, maybe something's wrong.":
                show Aarmsb1u
                P "Yeah you should, maybe something's wrong."
                hide Aarmsb1u
                show Aarmsb1d
                A "I can't remember the last time that he didn't at least DM us a good morning message."
                A "I almost never DM anyone privately, I don't really know what to say."
                hide Aarmsb1d
                show Aangry1
                A "You know what, this is dumb. I don't know what to say."
                hide Aangry1
    menu:
            "I'll DM him if you want.":
                $ AHP = AHP - 1
                show Aarmsb1u
                P "I can DM him."
                A "Are you okay with doing that?"
                P "Yeah, I'll tell you when he replies"
                hide Aarmsb1u
                "You open your Direct Message history with Conrad, it's mostly blank."

            "We'll probably hear from him tomorrow.":
                show Aarmsb1u
                P "We'll probably hear from him tomorrow."
                hide Aarmsb1u
                show Aarmsb1d
                A "Yeah I guess..."
                hide Aarmsb1d
                show Aarmsb1u
                A "Well I'm really tired, I'm gonna go to bed."
                A "Good night [P]!"
                hide Aarmsb1u
                "Anne left the call."
                "Despite telling Anne you didn't want to DM Conrad, something is compelling you to do so."
                "You have no idea why, but you open up your direct message history with Conrad. It's mostly blank."
    "What kind of message will you send Conrad?"
    menu:
        "Personal":
            "You send Conrad a sweet DM, detailing how personal the relationship between you to it, and how much it means to you."
        "Humorous":
            "You send Conrad a funny DM, filled with jokes and puns."
        "Serious":
            "You send Conrad a very formal DM. Addressing your concern regarding his absence."
        "Flirty":
            "You send Conrad a very flirty DM. Complete with emojis of hearts and fruit."
    "You wrote more than you intended, but are happy with what you sent."
#Transition effect
    scene black with fade
    scene bg room with fade
    "A week passes, you haven't heard back from Conrad"
    "Anne hasn't messaged you at all..."
    "Until... right now!" #We need to add discord sound effects.
    show Aspeak1o
    A "Hey [P]! It's been a while."
    hide Aspeak1o
    show Aarmsb1d
    P "We uh, missed the event on Friday. I'm really surprised that Conrad hasn't reached out to either of us."
    hide Aarmsb1d
    show Ahappy1o
    A "Kinda hard to think that we played games together almost every day for 3 years!"
    hide Ahappy1o
    show Asas1
    A "Do you remember how we all first met?"
    hide Asas1
    menu:
        "No not really.":
            show Asas1
            P "No, not really."
            hide Asas1
            show Aangry1
            A "Hey! how could you forget!?!"
            P "It’s been a long time since then."
            hide Aangry1
            show Aspeak1o
            A "Yeah, and we’ve changed a lot since then, haven’t we?"
            hide Aspeak1o
            show Ahappy1o
            A "Conrad was stuck on this boss fight and was trying to get some advice from this Discord server we were all in."
            hide Ahappy1o
            show Ashrug1
            A "*chuckles* It’s funny thinking back on how Conrad would dive headfirst into random caves to fight enemies head-on without any help."
            A "No wonder he had such a hard time with the game back then."
            P "That sounds like Conrad, alright."
            hide Ashrug1
            show Aspeak1o
            A "It was pretty late at night, so you and I were the only other people online and tried to help him out."
            hide Aspeak1o
            show Aarmsb1u
            A "He made a group DM so he could screenshare the game for us and we’d give him advice on how to defeat enemies."
            hide Aarmsb1u
            show Ahappy1o
            A "Eventually, he was able to get the hang of it and wanted us to keep playing together."
            A "We made a pretty great team in-game! We complemented each other’s strengths and weaknesses really well."
            hide Ahappy1o
            show Aarmsb1u
            A "Conrad was the brave one. He’d always try to defeat every enemy he encountered."
            hide Aarmsb1u
            show Ashrug1
            A "He’d always get hurt, so I’d be the one to heal him."
            hide Ashrug1
            show Aarmsb1u
            P "And whenever you and Conrad got lost, I’d be the one to guide us back on track."
            A "We started playing more and more sessions after that."
            A "It started to become a daily routine for us. We’d come online to play a session with him and then afterwards we’d talk about anything and everything."
            A "I can’t really pinpoint the exact time it happened, but…"
            hide Aarmsb1u
            show Ahappy1o
            A "Somewhere along the way, we became friends."
            hide Ahappy1o

        "Yeah of course!":
            show Asas1
            P "Yeah of course!"
            hide Asas1
            show Ahappy1o
            A "Oh yeah, it was a pretty special moment so I wouldn't expect you to forget."
            hide Ahappy1o
            show Aarmsb1u
            A "But you better not be lying about remembering, it's pretty important information!"
            hide Aarmsb1u
            show Aarmsb1d
            A "Important to me at least.."
            hide Aarmsb1d
    menu:
        "Our friendship grew gradually.":
            show Aarmsb1u
            P "Our friendship grew gradually."
            A "Yeah, that's what I was thinking, as we continued to play more and more together, and of course use discord to talk more and more, we became closer."
            hide Aarmsb1u
            show Ahappy1o
            A "And the closer we got, it became clear that we were all meant to be friends."
            hide Ahappy1o
        "We all became friends overnight.":
            show Aarmsb1u
            P "We all became friends overnight."
            hide Aarmsb1u
            show Ahappy1o
            A "Yeah, it's almost like we were all meant to be together."
            hide Ahappy1o
    show Aspeak1o
    A "Anyway, there's really no point in playing without Conrad, we need his help to clear the next boss."
    A "So we'll just wait until he comes back."
    hide Aspeak1o
    scene black with dissolve
    scene bg room with dissolve
    "1 month later..."
    "You are receiving a call from Anne on discord!"
    "Accept the call?"
    menu:
        "Accept call":
            "You answered the discord call."
            show Aarmsb1u
            A "H-hey!!"
            A "It's Anne."
            A "Uh, you knew that, discord shows you who's calling."
            A "I don't know why I said who I was."
            A "A-anyway! I need to tell you something."
            hide Aarmsb1u
            show Aarmsb1d
            A "I'm uh, really worried about Conrad."
            A "Like maybe he's okay and we're overreacting."
            A "B-but I want to go make sure he's okay."
            A "So uh, how do I explain this?"
            hide Aarmsb1d
            show Aarmsb1u
            A "I uh, went snooping around his friend list, specifically the mutual ones that him and I share."
            A "And it turns out, I'm friends with one of his close friends."
            hide Aarmsb1u
            show Aarmsb1d
            A "Just a total coincidence, but I hit her up and she hasn't heard from him in a while either."
            hide Aarmsb1d
            show Aarmsb1u
            A "So she's gonna take me to her."
            hide Aarmsb1u
            show Aarmsb1d
            A "I'm uh, going to Orlando"
            hide Aarmsb1d
            jump annexplain

        "Reject call.":
            "You don't answer the discord call."
            "You have recieved a message from Anne!"
            show Aarmsb1u
            A "Hey [P]! Give me a call when you can please!!"
            A "I uh, have something really important to tell you."
            hide Aarmsb1u
            jump CallBackLoop

label CallBackLoop:
menu:
    "Call Anne back":
        "You decide to Call Anne back."
        jump AnneCall
        label AnneCall:
        show Aarmsb1u
        "Ringing..."
        A "H-hey!!"
        A "You uh, didn't answer the first time, sorry if I interuppted something.."
        A "It's Anne."
        A "Uh wait, you knew that, discord shows you who's calling."
        A "I don't know why I said who I was."
        A "A-anyway! I need to tell you something."
        hide Aarmsb1u
        show Aarmsb1d
        A "I'm uh, really worried about Conrad."
        A "Like maybe he's okay and we're overreacting."
        A "B-but I want to go make sure he's okay."
        A "So uh, how do I explain this?"
        hide Aarmsb1d
        show Aarmsb1u
        A "I uh, went snooping around his friend list, specifically the mutual ones that him and I share."
        A "And it turns out, I'm friends with one of his close friends."
        hide Aarmsb1u
        show Aarmsb1d
        A "Just a total coincidence, but I hit her up and she hasn't heard from him in a while either."
        hide Aarmsb1d
        show Aarmsb1u
        A "So she's gonna take me to him."
        hide Aarmsb1u
        show Aarmsb1d
        A "I'm uh, going to Orlando"
        hide Aarmsb1d
        jump annexplain
        "You decide to Call Anne back."
        show Aarmsb1u
        A "H-hey!!"
        A "You uh, didn't answer the first time, sorry if I interuppted something.."
        A "It's Anne."
        A "Uh wait, you knew that, discord shows you who's calling."
        A "I don't know why I said who I was."
        A "A-anyway! I need to tell you something."
        hide Aarmsb1u
        show Aarmsb1d
        A "I'm uh, really worried about Conrad."
        A "Like maybe he's okay and we're overreacting."
        A "B-but I want to go make sure he's okay."
        A "So uh, how do I explain this?"
        hide Aarmsb1d
        show Aarmsb1u
        A "I uh, went snooping around his friend list, specifically the mutual ones that him and I share."
        A "And it turns out, I'm friends with one of his close friends."
        hide Aarmsb1u
        show Aarmsb1d
        A "Just a total coincidence, but I hit her up and she hasn't heard from him in a while either."
        hide Aarmsb1d
        show Aarmsb1u
        A "So she's gonna take me to him."
        hide Aarmsb1u
        show Aarmsb1d
        A "I'm uh, going to Orlando"
        hide Aarmsb1d
        jump annexplain
    "Don't call Anne back.":
        "You decide not to call Anne back."
        "Some time passes."
        "Will you call her back now?"
        menu:
            "Call Anne back.":
                jump AnneCall
            "Ignore her.":
                "The plot won't advance until you call her back..."
                "If you just want to waste time to see what the outcome is, then sorry to disappoint but it's nothing."
                jump CallBackLoop



label annexplain:
    show Aarmsb1d
    A "I need to find out if Conrad is okay."
    A "I have a place to stay, I've got a really cool Aunt out there."
    A "I'm really nervous, but I couldn't send anyone else to find him for me, I want to find him and make sure that he's okay."
    hide Aarmsb1d
    menu:
        "I'll go with you!":
            show Aarmsb1u
            P "I'll go with you!"
            hide Aarmsb1u
            show Ahappy1o
            A "Oh thank goodness you said that. I was trying to find a way to ask you to come."
            hide Ahappy1o
            show Ahappy1c
            A "Are you sure? It's a pretty long flight."
            hide Ahappy1c
            "You recall some money that you have left over from selling some of your old consoles"
            show Aarmsb1u
            P "I have enough money to get out there, we should be fine."
            hide Aarmsb1u
            show Ahappy1o
            A "That, means a lot to me, that you would agree to come with."
            hide Ahappy1o

        "Well, good luck with that.":
            show Aarmsb1u
            P "Well, good luck with that."
            hide Aarmsb1u
            show Aarmsb1d
            A "..."
            hide Aarmsb1d
            show Aarmsb1u
            A "Wait! I need to ask you something."
            hide Aarmsb1u
            show Aarmsb1d
            A "I-Is there anyway that you could uh, come with me?"
            P "..."
            A "..."
            A "I don't wanna be out there alone."
            hide Aarmsb1d
            show Asas1
            hide Ahappy1o
            A "I can even cover the cost for your ticket!"
            hide Aarmsb1d
            "You recall some money that you have left over from selling some of your old consoles"
            "You were going to spend that money to get a figurine of your favorite anime character but..."
            P "Alright, I'll go with you."
            hide Asas1
            show Ahappy1o
            A "R-Really!?"
            P "No need to pay, I have money left over."
            A "That, means a lot to me, that you would agree to come with me."
            hide Ahappy1o
    show Aarmsb1u
    A "Uh there's a few flights tomorrow"
    A "You could probably stay with us."
    hide Aarmsb1u
    show Aspeak1o
    A "Just uh, meet me in Florida I guess." #I wanna add a better transition into act 2
    hide Aspeak1o
    scene black with dissolve
    jump act2
#End of Act 1
