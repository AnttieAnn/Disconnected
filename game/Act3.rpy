label act3:
    show Staying with fade
    define SSV = ("Soft-Spoken Voice")
    "You knock on Anne's door a few times. When there's no answer, you open it yourself."
    "You notice most of the drawers are open and Anne's bags are half packed."
    show Cidleo
    C "Leaving already?"
    hide Cidleo
    show Cidlec
    "His voice catches Anne by surprise. She stares at you and Conrad before responding."
    show Cidlec at midtoright
    show Aspeak2o at left with dissolve
    A "I was planning on it, but then I had to think a few things out."
    hide Aspeak2o
    show Aspeak2c at left
    hide Cidlec
    show Cidleo at right
    C "I'm really sorry about everything."
    hide Cidleo
    show Cidlec at right
    hide Aspeak2c
    show Aspeak2o at left
    A "There's no need to apologize."
    A "This scholarship is important to you."
    hide Aspeak2o
    show Aarmsf2d at left
    A "At first, I didn't get why you didn't tell us that you wouldn't be able to talk to us as often instead of disappearing."
    hide Aarmsf2d
    show Aarmsf2u at left
    A "But now, I understand how difficult a decision that must have been."
    hide Aarmsf2u
    hide Cidlec

    "Anne's expression turns serious"
    show Aspeak2o
    A "[P], do you remmeber when I told you that I wasn't sure what I wanted to do after high school?"
    A "I told my aunt about it while we were here."
    hide Aspeak2o
    show Aarmsf2u
    A "I asked her for advice on what to do since she's successful."
    A "She suggested that I try out working for her over the summer."
    A "She said that, if I do good job and I like it, it could be a permanent position."
    A "The pay is decent and she said that I can live with her until I find a place of my own."
    show Aarmsf2u at midtoleft
    show Cidleo at right with dissolve
    C "Woah, that's great news! That's an amazing opportunity for you, Anne!"
    hide Cidleo
    show Cidlec at right
    hide Aarmsf2u
    show Aarmsf2d at left
    A "I'm not sure if I want to accept it, though"
    hide Cidlec
    show Cspeako at right
    C "Are you kidding? You'd be crazy not to accept it!"
    hide Cspeako
    show Cidleo at right
    C "Er, well... I guess I'm not being considerate, am I?"
    C "What's giving you second thoughts?"
    hide Cidleo
    show Cidlec at right
    A "This would be a drastic change for my life. I'd have to go through training, move across the country."
    hide Cidlec
    hide Aarmsf2d
    show Aarmsb2d
    A "and..."
    "She looks at you and Conrad"
    P "... And you wouldn't be able to talk to us as often."
    A "Yeah, exactly..."
    hide Aarmsb2d
    show Aarmsb2d at midtoleft
    show Cidle at right with dissolve
    C "This is a big decision for you. Don't let us affect your decision."
    hide Aarmsb2d
    show Aarmsf2u at left
    A "No, it's alright! I'd like to hear what both of you think."
    hide Cidle
    show Csmileo at right
    C "I guess if it were up to me, I'd accept it in a heartbeat"
    hide Csmileo
    show Cidle at right
    C "I can't really compare my situation to yours, though"
    hide Cidle
    show Cidleo at right
    C "I always knew I wanted to keep playing football after high school, so accepting my scholarship was a big no-brainer to me."
    hide Cidleo
    show Cidle at right
    C "But I'll admit that afterwards I had some second thoughts. Especially after I stop talking to both of you..."
    C "And ESPECIALLY after I found out that I hurt you."
    hide Cidle
    show Csmilec at right
    C "But now that I have both of you supporting me, all of the stress I had from training and moving to a different state is nothing anymore."
    C "I'm glad I accepted my offer, and I feel like you should accept yours."
    hide Csmilec
    show Cidle at right
    C "Those are just my two cents. I dont know about you or [P], though."
    hide Cidle
    hide Aarmsf2u

    menu:
        "You should accept the offer.":
            show Aarmsf2u
            P "You should accept the offer"
            A "Do you really think I should?"
            hide Aarmsf2u
            show Ahappy2o
            A "Thank you, both of you."
            A "I haven't decided what I want to do yet, but hearing what both of you helps with my deciision."
            hide Ahappy2o


        "You should think about this longer.":
            show Aarmsf2u
            P "You should think about this longer"
            A "Yeah, you're right."
            A "It's a really great opportunity, but I'm still having some second thoughts."
            hide Aarmsf2u
            show Ahappy2o
            A "Thank you, both of you."
            A "I haven't decided what I want to do yet, but hearing your words of support really helps with my decision."
            hide Ahappy2o

    show Ahappy2c at midtoleft
    show Cidleo at right with dissolve
    C "No problem. We're here for you, Anne."
    hide Ahappy2c
    hide Cidleo
    "A silence filled the air for a moment. Not an uncomfortable one, but one of coneplation"
    show Aarmsf2u at left
    show Cidlec at right
    A "I just realized, all this time together and we haven't really gotten to say hello for the first time and actually spend quality time together"
    hide Cidlec
    show Cidleo at right
    C "My flight leaves in a few days and I'm assuming you and [P] will have to leave soon as well."
    hide Cidleo
    show Cidlec at right
    P "We should make the most out of the time we have left."
    hide Cidlec
    show Cidleo at right
    C "Yeah, there's a bunch of theme parks and tourist attractions I'm sure both of you would be interested-"
    hide Cidleo
    show Cidlec at right

    A "*chuckles* I don't think that's what [P] meant."
    A "We should make the most out of being able to spend time with each other while we can"
    hide Aarmsf2u
    show Ahappy2o at left
    A "Even though the circumstances are a little sad, there's a part of me that's actually really happy with how everything turned out."
    A "We got to see each other, even if we're still going to go apart after this. That means more than anything to me."
    hide Ahappy2o
    show Ahappy2c at left
    hide Cidlec
    show Csmileo at right
    C "Same here."

    scene black with fade
    hide Staying
    "The next few days are spent with all three of you reminiscing and catching up in everything."
    "You have a great time together but have to get ready preparing to leave."
    "Today is the day of your flight back to California. Conrad's departure is today as well."
    show Aport with fade
    "You arrive at the airport with Conrad."

    show Csmilec
    C "What are the odds of us leaving on the same day, huh?"
    hide Csmilec
    show Cspeako
    C "When's your flight back to San Francisco?"
    hide Cspeako
    show Cspeakc
    P "In about a couple hours. I just wanted to be early."
    show Cspeako
    hide Cspeakc
    C "Yeah, that seems like you. My flight leaves in about half an hour."
    hide Cspeako
    SSV "Guess I have half an hour to say my sappy goodbyes, then."#Soft-Spoken voice
    "You and Conrad turn around to see who's speaking to you."
    show Asas2 with dissolve
    "It's Anne!"
    hide Asas2
    show Asas2 at midtoleft
    show Csmilec at right
    C "Anne! What are you doing here?"
    hide Csmilec
    show Cspeakc at right
    P "Are you flying back to Glendale?"
    A "No, but me not flying is part of the reason why I came"
    A "I decided that I want to stay here. I'm going to accept my aunt's offer and wanted to tell you both before I do."
    hide Asas2
    show Aarmsf2u at left
    A "But that's not the only reason I'm here."
    hide Cspeakc
    hide Aarmsf2u
    show Ahappy2o
    "Anne starts to smile brightly"
    hide Ahappy2o
    show Asad2c
    A "I wanted to say goodbye to both of you in person before you both go."
    A "I can't believe you're going to college, Conrad."
    hide Asad2c
    show Aarmsf2u
    A "*chuckles* And to think, just a few years ago you were this hopeless boy getting wrecked by zombies on WumpCraft"
    show Aarmsf2u at midtoleft
    show Csmilec at right with dissolve
    C "Now I'm going to be a hopeless boy getting wrecked by exams in college!"
    hide Csmilec
    show Csmileo at right
    C "I have to say, though. It's pretty funny how I'm moving to California at the same time you're moving to Florida."
    C "I guess we're destined to always have the timezone curse."
    hide Csmileo
    show Cspeakc at right
    A "I didn't realize your college is in California. Brilliant!"
    hide Cspeakc
    show Csmileo at right
    C "That's about the hundredth time I've heard you say 'brilliant' since you came here."
    C "Keep it up and you'll have to change your Discord username to '@BrilliantAnne.'"
    hide Csmileo
    show Cspeakc at right
    hide Aarmsf2u
    show Asas2 at left
    A "One 'brilliant' reference is enough. The username is a bit too on the nose."
    A "So [P], what are you planning to do once you go back home?"
    hide Asas2
    hide Cspeakc

    menu:
        "Maybe I'll get a job like Anne.":
            show Asas2 at left
            show Cspeakc at right
            P "Maybe I'll get a job like you"
            hide Asas2
            show Ahappy2o at left
            A "Brilliant! If you ever need some extra cash, I could probably put in a recomendation to my aunt to hire you."
            hide Ahappy2o
            show Ahappy2c at left
            hide Cspeakc
            show Csmileo at right
            C "*laughs* The image of [P] running aroud and taking orders from your aunt just seems really funny to me."
            hide Csmileo
            show Cspeako at right
            C "But hey, that's a great idea. You know we'll always have your back no matter what you decide."
            hide Cspeakc
            show Csmilec at right
            C "And don't hesitate to reach out to us!"

        "Maybe I'll go to college like Conrad.":
            show Asas2 at left
            show Cspeakc at right
            P "Maybe I'll go to college like Conrad."
            hide Cspeakc
            show Csmileo at right
            C "Hey, that's pretty cool! Maybe we'll end up at the same college. I could put a good word in to my coach and have us on the same football team!"
            hide Csmileo
            show Cspeakc at right
            hide Asas2
            show Ahappy2o at left
            A "*laughs*"
            A "The image of [P] running around and trying to be an athlete just seems really funny to me."
            A "But hey, that's a great idea. You know we'll always support your decision no matter what."
            hide Ahappy2o
            show Ahappy2c at left
            hide Cspeakc
            show Csmilec at right
            C "And don't hesitate to reach out to us!"

        "I'm not really sure what I want to do, yet":
            show Asas2 at left
            show Cspeakc at right
            P "I'm not really sure what I want to do, yet."
            hide Asas2
            show Ahappy2o at left
            A "That's totally fine. You know we'll always have your back no matter what you decide."
            hide Ahappy2o
            show Ahappy2c at left
            hide Cspeakc
            show Csmilec at right
            C "I couldn't have said it better myself!"
            hide Csmilec
            show Csmilec at right
            C "If you ever need help with whatever you want to do after all of this, don't hesitate to reach out to us!"
    hide Ahappy2c
    show Ahappy2o at left
    A "Conrad's right. Just because we're all going in different directions in life doesn't mean we have to cut each other out completely."
    hide Ahappy2o
    show Asas2 at left
    A "I'm probably going to be really busy helping my aunt."
    hide Csmilec
    show Cspeako at right
    C "And training's going to be crazy for me for the next four years..."
    C "But I won't ghost on all of you like I did last time. I'll make sure of it."
    hide Cspeako
    show Csmileo at right
    C "I'll be sure to update you guys whenever I can."
    hide Csmileo
    show Cspeakc at right
    hide Asas2
    show Ahappy2o at left
    A "Brilliant! I'll do it, too."
    hide Ahappy2o
    show Ahappy2c at left
    P "I'm looking forward to the future. And I'm glad I'll get to share it with you both."
    hide Cspeakc
    hide Ahappy2c

    "An annoucement for Conrad's flight departing soon rings across the airport lobby."

    "You all look at each other a bit saddened that your reunion had to be cut short"
    show Csmileo
    C "Looks like I'll have to go right now."
    hide Csmileo

    "Conrad stays still for a moment as if he's unsure about what he should do next"
    "Suddenly, Anne leaps onto him for a bear hug!"
    show Csmilec
    C "Ack! Tackled! Foul play!"
    hide Csmilec
    "Conrad and Anne started to laugh as Anne starts to loosen her grip."
    "You start to laugh as well at the other two's childish antics and then decided to join in for a group hug."
    "Somehow, all the sadness you felt about leaving started to drift away during that hug."
    show Cspeakc at right
    show Ahappy2o at left
    A "Both of you have a safe trip back home!"
    hide Ahappy2o
    hide Cspeakc
    "Anne was the first one to break the hug."
    show Aarmsf2u
    A "Hey! Before you go, I have something to give you."
    hide Aarmsf2u
    "Anne reaches into her purse and pulls out an alligator keychain and hands it to Conrad"
    show Aarmsf2u
    A "I got this at the gift shop when [P] and I first landed here."
    hide Aarmsf2u
    show Aarmsf2d
    A "I know it's pretty weird giving you a souvenir from the city you grew up in, but i wanted you to have something to remmember this moment."
    hide Aarmsf2d
    show Aarmsf2u
    A "The Alligator looks really cool and as if it's prepared for anything that stands in its way!"
    hide Aarmsf2u
    show Ahappy2o
    A "It kind of reminded me of you."
    hide Ahappy2o

    "Conrad smiles and hooks up the keychain to his bag."
    show Csmileo
    C "I'll keep it with me always, Anne."
    hide Csmileo
    show Csmileo
    C "I'll text you guys right before I have to depart, I'm glad we got to see each other."
    hide Csmileo
    show Csmilec
    P "Same here."
    show Csmilec at midtoright
    show Ahappy2o at left with dissolve
    A "Who knows, maybe one day the stars will align for us to meet up in real life again some day for some reason!"
    hide Ahappy2o
    show Ahappy2c at left
    P "I'll be looking forward to then."
    hide Ahappy2c
    hide Csmilec

    "Conrad carries his bags and gives you and Anne one last look before he goes to catch his flight."
    "You carry your bags too, planning to go to check-in. But before you can go, Anne stops you."

    show Aarmsf2u
    A "Don't think I forgot about you, silly!"
    A "Do me a favor and hold out your wrist."
    hide Aarmsf2u
    "You hesitantly hold out your wrist as Anne wraps a bracelet around it."
    "It has some kind of stone attached on it."

    show Ahappy2o
    A "Brilliant! It looks great on you."
    hide Ahappy2o
    show Aarmsf2u
    A "While I was buying stuff at the gift shop, I saw this hanging by the counter."
    A "The cashier told me that it's a moonstone, the state stone of Florida."
    hide Aarmsf2u
    show Asas2
    A "I looked it up on my phone and apparently it's a healing stone that's supposed to help bring calm, peace, and balance."
    hide Asas2
    show Ahappy2o
    A "All of those descriptions fit you pretty well, so I decided to get it for you!"
    hide Ahappy2o
    "Anne presses on her necklace. To your surprise, it lights up!"
    show Aarmsf2u
    A "I also got a little something for myself, too!"
    A "It's the orange necklace I got from the gift shop when we arrived here."
    P "It shines brightly, just like you."
    hide Aarmsf2u
    show Aarmsf2d
    A "D-do you really think so?"
    A "If I'm being totally honest, I only got it because the smiley face looked cute..."
    hide Aarmsf2d
    show Ahappy2o
    A "But I'm glad we were each able to have something that fits each of us."
    A "This way, we each have something to remember this moment."
    A "Not that I'll ever forget this moment, but it's always nice to have a souvenir!"

    hide Ahappy2o
    show Aarmsf2u
    A "Have a safe trip home, [P]"
    hide Aarmsf2u
    "You say goodbye to Anne and head towards baggage check-in."
    "You glance at the bracelet Anne gave you. You find it difficult to hold back a smile."
    "You recieve a notification from Discord."
    "Conrad pinned a message to your DM."
    "It was the DM you sent to him a month ago!"
    if ConDM == "Person":
        P "Hey, Conrad"
        P "Sorry to bother you."
        P "I just wanted to make sure you're okay."
        P "You haven't been talking to us all day and I was just worried that something must have happened"
        P "Somehow talking to you always seems to make my day a little brighter. I don't know what I'd do without you."
        P "Just know that you're one of my closest friends."
        P "Text me back when you can. I miss you"
        jump ConType
    if ConDM == "Humor":
        P "Heyo, Conrad!"
        P "I hope I didn't interrupt you dying in WumpCraft for the millionth time, haha."
        P "But seriously, everything's ok right?"
        P "You're starting to make me worried. I need you to bring me into another laughing fit. You always knew how to do that."
        P "Just know that you're one of my closest friends."
        P "Text me back when you can, I miss making fun of you."
        jump ConType

    if ConDM == "Seri":
        P "Conrad?"
        P "Hey, I hope I'm not bothering you."
        P "I just wanted to make sure everything's alright."
        p "I'm really worried about you. You haven't been online all day and I just wanted to make sure everythign was alright."
        P "You mean alot to me... I have no idea what I would do if something were to happen to you"
        P "Just know that you're one of my closest friends."
        P "Message me back when you can. I miss talking to you"

    if ConDM == "Fl":
        P "Hey, Con~"
        P "I hope I'm not distracting you. You always had a way of distracting me when i least expected it."
        P "But seriously, is everything okay?"
        P "It feels weird not hearing from you. You'd always talk nonstop about WumpCraft but you would talk about this one girl... something else... the girl again..."
        P "but that's beside the point"
        P "Just know that you're one of my closest friends."
        P "Slide into my DMs when you can. I miss hanging out with you."
label ConType:
    "Conrad is typing..."
    show Csmileo
    C "I was just reading that message again before my plane takes off."
    hide Csmileo
    show Cidleo
    C "I didn't realized how many messages you and Anne sent me since I disappeared. I've only got around to reading through all of them today."
    C "I wish I read this a lot sooner."
    hide Cidleo
    if ConDM == "Person":
        show Csmileo
        C "[P], you truly mean a lot to me."
        C "You're one of my closest friends and I'm grateful that you're a part of my life."
        hide Csmileo
        show Csmilec
        C "Your message was pretty sappy. Maybe even more sappy than all of Anne's messages, if that's even possible."
        hide Csmilec
        jump ConEnd

    if ConDM == "Humor":
        show Csmileo
        C "I know we like to make fun of each other a lot, [P]."
        C "But I want you to know that you're one of my closest friends."
        hide Csmileo
        show Csmilec
        C "Your message made me laugh. That was definitely refreashing after reading all of Anne's sappy messages."
        hide Csmilec
        jump ConEnd

    if ConDM == "Seri":
        show Csmileo
        C "You're one of my closest friends, [P]."
        C "No amount of distance or inactivity will ever change that."
        hide Csmileo
        show Csmilec
        C "I don't think I've ever seen you this serious. I'ts a huge contrast from all of Anne's sappy messages."
        hide Csmilec
        jump ConEnd

    if ConDM == "Fl":
        show Csmileo
        C "You're more than a friend, [P]"
        hide Csmileo
        show Csmilec
        C "N-not that way! What I'm trying to say is that you're one of my closest friends."
        C "You have quite a way with words. You should try sending Anne one of these. She'll probably send you one of her sappy messages in response."
        hide Csmilec
        jump ConEnd

label ConEnd:
    show Cidle
    C "I wanted to pin your messages so I can read it back whenever I need a quick smile."
    hide Cidle
    show Cspeako
    C "It's probably going to be a long while until the next time I check Discord, but don't hesitate in staying in touch."
    hide Cspeako
    show Csmileo
    C "I'll try to message you back whenever I manage to get the time."
    hide Csmileo
    show Csmilec
    C "Take care, [P]."
    scene black with dissolve
    hide Aport
    hide Csmilec
    "Conrad sends a selfie of him in his plane to the group DM with Anne with a caption"
    "It's an alligator emoji follow by a plus sign with an orange emoji follow by another plus sign with a moon emoji and it would all equal an Airplane emoji with a blue heart emoji next to it"
    "He has a bright smile while holding up his alligator keychain!"
    "Anne reacts with a bunch of smiley face emojis."
    "You pin that image to the group DM."
    "Conrad goes offline."
    "You smile to yourself as you put your phone away."
    "Your lives are going to be busier from now on and you won't be able to talk as much."
    "But the memories you've shared together, online and offline, will stay with you forever."

    jump credits

    #Cue credits
