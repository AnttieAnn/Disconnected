label act2:
    show Aplane with dissolve
    define Pilot = ("Pilot")
    "As you check in your baggage, you receive a notification from  Discord."
    show Ahips1
    "It's a message from Anne"
    A "Hey [P]! I'm leaving my flight now."
    hide Ahips1
    show Ahappy1o
    A "Uh the first class plane is really nice, I wish you had let me pay for your ticket lol."
    A "We can keep talking if ya want so you don't get bored."
    hide Ahappy1o
    show Aspeak1o
    A "Oh wait, actually, you better put your phone in airplane mode."
    A "I'll hear from ya in a few hours."
    hide Ahappy1o
    show Aspeak1o
    "You board the plane, and the intercom speaks."
    hide Aspeak1o
    Pilot "Thank you for flying with Omnia Airlines, please remember to put your phone into airplane mode."
    "Your moral compass tells you to put your phone into airplane mode, but."
    "There's an in game event for this game you play on your phone, and it requires the internet.."
    menu:
        "Put phone into airplane mode":
            $ Airplanemode = "ye"
            "You put your phone in airplane mode."
            "+1 brownie points for being a good person."
            Pilot "This is your pilot speaking, we will be taking off momentarily."
            "You decide to doze off and take a nap..."
            show Aplane with fade
            "A few hours later.."
            Pilot "This is your pilot speaking, just letting you know that this was the smoothest flight of my career, and that we will  be touching down in Orlando momentaily"

        "Keep internet on.":
            $ Airplanemode = "non"
            "You decide that your weeaboo rhythm game is much more important than the safety of you and the passengers."
            "-1 brownie points for being an awful person."
            "I hope you feel bad."
            "This is your pilot speaking, we will be taking off momentarily."
            "The plane takes off, the scenery out the window is beautiful, but you would rather stare at your stupid game."
            "Eventually, the plane is so high up that you no longer have a signal."
            "Not sure what you expected to happen."
            "Without technology to keep you occupied, you being to doze off.." #add in cool fade transition
            show Aplane with fade
            "A few hours later"
            Pilot "This is your pilot speaking, due to devices not being shut off or put in airplane mode, we are being forced to make a stop on the ground."
            "Please remain seated."
            "Some time passes, and eventually after many delays, the plane is back up in the air, and you arrive in Orlando."

    if Airplanemode == "ye":
        $ AHP -= 1
        jump planedone
    if Airplanemode == "non":
        $ AHP += 100
        jump planedone


label planedone:
        scene black with dissolve
        show Aport with dissolve
        "You exit the plane, spend 50 minutes searching for your luggage, and are now in the lobby."
        "You open up your discord, to see several messages from Anne."
        show Aspeak1o
        A "Just arrived in Orlando! ✈️"
        A "Your flight should be arriving a little later than mine."
        hide Aspeak1o
        show Ahappy1o
        A "I’ll take a quick nap at the airport lobby so I don’t miss you."
        A "Or actually, maybe I should go check out the gift shop to see if I can find anything to surprise you!"
        hide Ahappy1o
        show Aarmsf1d
        A "Oops! Guess I ruined the surprise…"
        hide Aarmsf1d
        show Aarmsf1u
        A "Oh well, since you already know that I’m going to get you something I’ll let you choose what gift I get for you."
        A "It’s the least I could do since you came all the way here to help me out!"
        hide Aarmsf1u
        show Aspeak1o
        A "There’s a cool-looking alligator keychain. The alligator’s jaws also double as a bottle opener! It’s really handy."
        A "But there’s also a cute necklace of an orange with a smiley face on it!"
        A "I actually can't stand oranges, they remind me of this one really annoying character from an anime I watched."
        A "But this necklace is pretty cool. It even lights up when you click on it! It’s really bright."
        hide Aspeak1o
        show Aarmsf1u
        A "I can’t decide. Which would you like me to buy?"
        menu:
            "Alligator.":
                "[P] is typing..."
                "You realize that there are more of Anne's messages to read."
            "Orange.":
                "[P] is typing..."
                "You realize that there are more of Anne's messages to read."
hide Aarmsf1u
show Aarmsf1d
A "Oh wait, why am I messaging you lol. You're phone is still in airplane mode."
hide Aarmsf1d
show Aangry1
A "At least, I'm assuming it is, you really have to be a terrible person to not turn on airplane mode."
hide Aangry1
show Ahappy1o
A "Guess I’ll have to choose myself. At least I’ll be able to surprise you!"
"After you stop typing, you immediately see Anne begin to type."
hide Ahappy1o
show Aarmsf1u
A "Hey! I hope you aren't typing on the plane."
A "Your plane should have arrived by now, right? How was your flight?"
menu:
    "Pretty smooth, no delays or anything.":
        P "Pretty smooth, no delays or anything."
        show Aarmsf1d
        P "The pilot even said it was the smoothest flight ever."
    "Pretty rough, we had quite a few delays.":
        P "Pretty rough, we had quite a few delays."
        hide Aarmsf1u
        show Aarmsf1d
        A "Aw, I'm sorry to hear that."
hide Aarmsf1d
show Aarmsf1u
A "I couldn’t sleep a wink, I kept worrying about Conrad."
hide Aarmsf1u
show Aspeak1o
A "But, hey! That’s why we’re here, right? To make sure he’s safe so we stop worrying about him!"
A "I’m over here by the gift shop. Haven’t left ever since I landed. It’s really easy to pass the time just browsing."
hide Aspeak1o
A "Can you see me? I'm wearing a black shirt."
"You look around and see Anne facing away from you, staring intently at her phone."
menu:
    "Scare her":
        "You walk up to Anne and scare her."
        P "boo!"
        A "ahhHHHH"
        $ AHP = AHP + 1
        #Add Ahole point increase here
        show Aangry2
        A "What the hell?!?"
        A "Just who the hell do you think you are you piece of..."
        hide Aangry2
        "Anne suddenly recognizes you."
    "Approach her":
        "You walk around so you don't scare her."
        P "Hey"
        "Anne looks up and instantly recognizes you."
show Ahappy2o
A "OH MY GOSH HI!!"
"Anne extends her arm for a hug."
menu:
    "Hug her.":
        "You accept the hug."
        hide Ahappy2o
    "Reach for a handshake":
        "You reach your hand out for a shake."
        hide Ahappy2o
        show Aarmsf2d
        "Anne realizes what you're doing, puts her hands down and reaches out."
        A "S-Sorry, I just got really excited."
        hide Aarmsf2d
        "Anne shakes your hand, firmly grasping it."
show Ahappy2o
A "I can’t believe this is our first time meeting in real life, I wish it was for a better reason though."
A "I know I’ve seen pictures of you in the past, but it’s still pretty freaky finally seeing your face in person."
hide Ahappy2o
show Aarmsf2d
A "Wait, that came out wrong!"
hide Aarmsf2d
show Aarmsf2u
A "You look nice in person [P]. And in photos!"
hide Aarmsf2u
show Ahips2
A "Anyways, we can talk more later. We should be looking for our ride."
A "My aunt sent someone to pick us up and they should be here by now."
hide Ahips2
"You notice a very tall man wearing professional attire holding up a sign:"
"Pick-up for Miss Anne. G."
"As soon as Anne makes eye contact with the man, she runs up and hugs him."
show Ahappy2o
A "FREIGHT TRAIN!!"
hide Ahappy2o
show Ahappy2c
"The man embraces her back."
hide Ahappy2c
show Aspeak2o
A "[P], this is one of my aunt's employees. Freight Train."
hide Aspeak2o
show Aarmsf2u
A "I uh, don't know his actual name, but he just goes by Freight Train."
hide Aarmsf2u
define F = ("Freight Train")
F "What's up tiny person"
"You try to make out Freight Train's face, but are too intimidated to get a closer look."
if AHP < 0:
    F "I like them."
if AHP < 99:
    "Freight Train is observing you, he looks like a tough guy."
    jump limo
if AHP > 99:
    F "I don't like them."
    F "Seems like a fella who wouldn't turn on Airplane mode."
    show Ahappy1o
    A "Oh don't worry Freight Train, I'm sure [P] uses airplane mode whenever he's on an airline."
    hide Ahappy1o
    show Asas2
    A "After all, you have to be a special kind of evil to not use Airplane mode."
    hide Asas2
    jump limo
label limo:
    A "So uh, lets head out!"
    show Ahappy2o
    "You follow Freight Train outside the airport, a big black limo is there waiting for you."
    hide Ahappy2o
menu:
    "That's a beautiful car.":
        P "That's a beautiful car."
        show Aarmsf2d
        A "O-oh, my Aunt went a little overboard, I could have just gotten a rental car."
        hide Aarmsf2d
    "Wow I didn't know that you were so rich.":
        P "Wow I didn't know that you were so rich."
        show Aarmsf2d
        A "O-oh no its not like that!"
        A "My aunt is the one with the money."
        A "She even bought me first class tickets for my trip over here! I told her it was unnecessary, but she insisted."
        hide Aarmsf2d
        show Aarmsf2u
        A "Too bad I couldn’t figure out how to use the bed recliner."
        A "It was pretty awkward eating sushi with the headrest reclined all the way to the back."
        hide Aarmsf2u
        "You start to regret not letting Anne pay for your tickets"
scene black with dissolve
"You follow Anne inside the limo, Freight Train gets in the drivers seat."
"It's a very nice limo, with fancy seats, and even some televisions."
"A few minutes pass, and Anne falls asleep."
"You arrive at a large house, and the limo stops."
"Anne is still asleep."
define whomst = ("???")

define T = ("Aunt Tiff")
menu:
    "Wake her up.":
        "It would be pretty awkward for you to show up at her Aunt's front door without Anne."
        "You touch Anne ever so slightly on the shoulder, with the tip of your finger."
        A "ahhHHHH"
        show Aangry2
        "Anne looks pretty pissed."
        A "[P] you scared the crap out of me!"
        "You can feel Freight Train staring at you through the rear view mirror."
        hide Aangry2
        "You and Anne exit the limo."
        show Asas2
        show droom with dissolve
        "Anne leads you to the door, and rings the doorbell."
        "A nice looking women answers the door."
        hide Asas2
        show Tidleo at right
        whomst "Hello...?"
        hide Asas2
        show Ahappy2o at midtoleft
        A "Aunt Tiff!"
        "Anne and her aunt immediately embrace."

    "Let her sleep":
        "You allow Anne to continue sleeping."
        "You exit the limo, and walk up to the front door."
        "You ring the doorbell"
        show Tidleo at right
        show droom with dissolve
        whomst "Hello...?"
        whomst "And you are...?"
        "You hear the sound of Anne exiting the limo."
        show Ahappy2o at left
        A "Aunt Tiff!"
        "Anne runs up to her Aunt and embraces her."


hide Ahappy2o
hide Tidleo
show Thappy at right
T "Oh my goodness my little BrilliAnne. I hardly recognized you."
show Asas2 at left
A "Aunt Tiff this is my friend, [P]."
P "It's a pleasure to meet you m'am."
P "BrilliAnne?"
hide Asas2
show Aarmsf2d at left
A "Oh, uh, back when I was little, I used to say 'Brilliant' all the time."
show Aarmsf2u at left
A "I guess it was kinda my catchphrase."
hide Thappy
show Tidleo at right
T "Anne, you didn’t tell me she was bringing over a friend to visit. The more the merrier!"
hide Tidleo
show Thappy at right
hide Aarmsf2u
T "And please, You can call me aunt Tiff! There’s no need to call me ma’am."
hide Aarmsf2d
T "Just how old do you think I am?"
hide Thappy
menu:
    "30":
        P "30? You seem pretty young to be an aunt."
        show Thappy
        T "Oh, I like this one."
        hide Thappy
    "40":
        P "40? since you're Anne's aunt I assume you must be older than Anne by a little bit."
        show Tangry at right
        T "..."
        show Aarmsf2d at left
        A "..."
        hide Tangry
        hide Aarmsf2d
    "60":
        hide Aarmsf2d
        P "60? You look pretty old."
        show Tangry at right
        T "Oh, really? I don't have to let you in my home ya know."
        show Aangry2
        A "Aunt Tiff!"
        hide Tangry
        hide Aangry2
"Aunt Tiff leads you into the dining room."
show Asas2
A "Wow, it’s been such a long time since I’ve visited here. Your house has changed so much; I can barely recognize it!"
A "I don’t remember the dining room being this big."
hide Asas2
show Ahappy2c at midtoleft
show Thappy at right
T "As time went on, my company grew larger and larger. I suppose that the same applied to my home."
hide Thappy
show Tidleo at right
T "If you need anything, I’ll be in the kitchen preparing some snacks for the two of you."
T "Make yourselves at home!"
hide Tidleo
"Aunt Tiff exits the room, leaving you and Anne by yourselves."

P "You and your aunt seem to be really close."
hide Ahappy2c
show Asas2
A "Yeah, since I’m her only niece so I’ve always been given special treatment."
A "It’s a shame that she’s so busy with her business here in Orlando. We rarely get to see each other."
P "I’m glad that you’re able to get together again with your aunt after all these years apart, but I’m sad it’s under these circumstances."
T "What circumstances?"
show Tangry at right
"You turn around and see Aunt Tiff holding a decorative bowl of crackers."

"You immediately regret your choice of words when you see the look on Anne’s face."
hide Asas2
show Aarmsf2d
A "Oh, um, I was meaning to tell you about this eventually…"
A "[P] and I are in Florida to find a missing friend. He hasn’t been answering any of our messages or calls and we’ve been really worried about him."
show Aarmsf2u
A "Ah, I see. You should have told me you were here for more than just a friendly visit, Anne."
A "I’m sorry, I just didn’t want to make you feel bad and think that was the only reason I came to Florida…"
hide Aarmsf2d
hide Tangry
show Thappy at right
T "That’s fine, I’m just glad you’re here. So this friend of yours, tell me about him. "
hide Aarmsf2d
hide Thappy
show Moving with dissolve
"You and Anne spent the rest of the evening telling stories about Conrad to Aunt Tiff."

"During that time, you can’t help but notice a smile on Anne’s face as she reminisced about your time together."

"You started to smile as well."

"And then you started to tell her about Conrad’s sudden disappearance…"
hide Tangry
show Thappy at right
T "I can tell that Conrad is a nice friend from the stories you’ve told. But It’s awfully strange that he would just disappear on you both like that."
hide Aarmsf2u
show Ahappy2o at left
A "Yeah, that’s why we’re really worried about where he is right now. We have to find him! That’s what he would want us to do."
hide Thappy
show Tangry at right
T "Are you sure about that?"
hide Ahappy2o
show Asas2
A "What do you mean?"
hide Tangry
hide Asas2
show Tidleo
T "I had many friendships, relationships, and connections with different people."
T "Many of them left an impact on my life. Some deeper than others. "
T "Although some of them may be gone, they left an impression on me that stayed."
hide Tidleo
show Thappy
T "It seems that wherever Conrad may be, he has left an impression on both of you that will also stay."
T "And I’m sure that both of you have also left an impression on him."
hide Thappy
show Thappy at midtoright
show Aarmsf2u at midtoleft
A "I understand what you’re trying to say, but he isn’t gone yet."
A "I don’t understand why he stopped talking to us… Or where he went..."
hide Aarmsf2u
show Aarmsf2d
A "But, he’s still going to be a big part of our lives and everything will go back to the way it used to be. We just have to go and find him!"
hide Aarmsf2d
show Aarmsf2u at left
A "So that’s why we’re still going to keep looking for him! Right, [P]?"
"You nod in agreement."
hide Thappy
show Tidleo at right
T "Well I wish the two of you the best of luck."
hide Tidleo
hide Aarmsf2u
show Ahappy2o
A "Thanks Aunt Tiff."
hide Ahappy2o
show Asas2
A "[P] we should hit the hay, we're meeting Conrad's friend easrly tomorrow morning."
A "Be sure to wake up bright and early."
"Anne leaves for her room upstairs."
hide Asas2 #fade
"The next morning..."
"You wake up, before Anne does..."
"You recall that she said to wake up bright and early."
menu:
    "Wake her":
        "You decide to wake Anne up."
        "You enter Anne's room, she's passed out on the bed."
        "You throw your entire body on the mattress."
        A "ahhHHHH"
        show Aangry1
        A "Oh, [P] it's just you."
        hide Aangry1
        show Asas1
        A "Looks like I slept in, we should head out."
        hide Asas1


    "Let her sleep":
        "You let her sleep."
        "You go downstairs to the kitchen and hear Aunt Tiffany from the kitchen."
        T "Hello [P]!"
        T "Oh...? Is Anne not awake yet?"
        T "Let me go get her..."
        "Aunt Tiffany walks upstairs to Anne's room. In the distance you hear her scare Anne awake."
        A "ahhHHHH"
"Aunt Tiffany serves the both of you breakfast."
"She made a lot of food for the both of you. Eggs, bacon, grits, and even a hashbrown casserole!"
"There are some biscuits, with gravy for dipping."
show Ahappy2o
A "Thank you for breakfast Aunt Tiff, we'll be headed out now."
show Thappy at right
T "Good luck BrilliAnne, I hope ya find your friend!"
hide Thappy
hide Ahappy2o
"You and Anne step outside."
show Asas2
A "Okay [P], we're meeting Conrad's friend at a football field. Her name is Jade."
A "She said he'd probably be there."
A "Freight Train will be here soon with the limo, Aunt Tiff told me that we could use it all day."
hide Asas2
scene black with dissolve
"You see the limo pull up and get in."
"Freight Train drives you to a football field."
"You look out and see a number of football players practicing, with a few spectators."
show Lax with dissolve
show Ahappy2o
A "Let's see if we can find Jade."
hide Ahappy2o
show Ahappy2c at midtoleft
"You sit in the stands, looking around for her."
define J = ("Jade")
show Jhappyo at midtoright
whomst "You look lost, can I help you?"
hide Ahappy2c
show Ahappy2o at left
A "O-Oh! We're just looking for a friend."
hide Jhappyo
show Jarmsuo at right
whomst "Really? Which friend?"
A "Well, a friend who's gonna take us to our other friend, so we can find out if he's okay."
"Anne pulls out a picture of Conrad."
A "You wouldn't happen to know who this is do you? I was told he might be around here."
hide Jarmsuo
show Jarmsdo at right
whomst "Conrad?"
A "Yeah! Do you know him?"
J "I’d like to think so. It would be pretty strange if I didn’t during all those years of dating."
A "Wait a minute. Jade?"
hide Jarmsdo
show Jhappyo at right
J "Took ya long enough to recognize me, and Conrad said you were supposed to be the smart one."
hide Ahappy2o
J "How are you doing Anne?"
show Asas2 at left
A "Oh my gosh I didn't even recognize you! Which makes sense because I've literally never seen your face before."
A "[P] this is Jade, Conrad's girlfriend."
hide Ahappy
hide Jhappyo
show Jangry at right
J "Ex-girlfriend, currently."
hide Asas2
show Aarmsf2d at left
A "Oh, I’m sorry! I didn’t realize…"
hide Jangry
show Jarmsuo at right
J "It’s fine, it was fairly recent so I don’t expect you to have known. Guess I didn't mention it when we were talking."
J "Now that I think about it, Conrad did mention having friends from California. I apologize for not being able to recognize you both."
hide Aarmsf2d
show Aarmsf2u at left
A "Can you help us find him? It’s really important."
J "We haven’t talked to each other since we’ve broken up, but I don't mind."
P "When was that, if you don’t mind me asking?"
J "A little over a month ago."
A "That’s around the same time he stopped talking to us..."
hide Aarmsf2u
show Aarmsf2d
J "He's out there walking onto the field."
J "He just got out of church, so he's talking to some of his buddies before they practice."
A "Brilliant! I can see him."
J "Be careful if you approach him, he gets really serious when he's practicing."
hide Aarmsf2d
show Ahappy2o
A "That's funny, he gets really passionate about video games when we play together."
hide Ahappy2o
show Aarmsf2d
A "Er. used to play."
J "Well I'm glad I could help ya find him."
hide Jarmsuo
J "Best of luck to ya."
hide Aarmsf2d
show Aarmsf2u
A "Jade is really nice. I wonder why she and Conrad broke up?"
hide Aarmsf2u
show Aarmsf2d
A "And around the same time he stopped talking to us…"
A "There’s so many people on the field. I can’t see any of their faces behind those football helmets."
P "How will we be able to tell which one is Conrad?"
hide Aarmsf2d
show Ahappy2c
A "We’ll have to take a closer look at the players if we want to find him."

"Anne starts to approach the inner field, but you immediately stop her"

P "Hey, Anne. There’s a sign posted right here."
"Please stay five feet away from the inner field at all times."

A "What about it?"
hide Ahappy2c
menu:
    "Follow the sign, we should stay back.":
        P "Follow the sign. We should stay here."
        show Aangry2
        A "No way!"
        A "We’ve already gotten this far. We can’t let a stupid sign stop us"
        A "I’ll go by myself. You can stay on the lookout."
        hide Aangry2
        show Aangry2 at midtoleft
        "Anne tries to sneak further onto the field to get a better look. You stay behind."
        hide Aangry2
        "Luckily, Anne is pretty good at sleuthing around. And all the players are too busy playing football."
        "Your phone vibrates with a new notification."
        A "I can't see him."
        "You look towards the field and see Anne on her phone."
        "But she doesn’t notice a football player is headed straight towards her!"
        P "LOOK OUT!!!"
        A "ahhHHHH"
        "The football player tackles Anne, and she falls to the ground."

    "Signs are stupid, lets go onto the field.":
        P "Signs are stupid, lets go onto the field."
        A "Brilliant!"
        show Ahappy2o
        "Luckily, you and Anne are good at sleuthing, and all the players are too busy playing football."
        A "I can't see him."
        "Anne checks something on her phone, but doesn't notice a football player headed straight for her."
        P "LOOK OUT!!!"
        hide Ahappy2o
        A "ahhHHHH"
        "The football player tackles Anne, and she falls to the ground."
whomst "bruh, watch where you're going."
show Aangry2
A "Ouch..."
"Anne got knocked down pretty hard, but she seems alright."
whomst "That scream..."
C "Anne???!"
show Cspeako at midtoright
"Conrad runs over from the sidelines."
hide Aangry2
show Ahappy2o
A"Conrad?"
C"Anne? What are you doing here?"
C"And [P], too?!"
hide Cspeako
show Csmileo at right
C"Let’s go move to the side, unless you want to get tackled by another player."
scene black with fade
"You, Conrad, and Anne walk off the field to talk."
show Lax_side with dissolve
show Ahappy2o at left
show Cidlec at midtoright
A "We’ve been looking everywhere for you! I’m glad we were able to find you."
hide Cidlec
show Cidleo at right
C "Yeah, that makes one of us…"
hide Ahappy2o
show Aarmsf2u at left
A "What are you talking about?"
C "You two shouldn’t have come here."

"You notice Anne’s smile slowly begin to fade. You can’t hide the disappointment in your face, either."
hide Aarmsf2u at left
show Aangry2 at left
P "What happened to you? Why haven’t you been contacting us?"
A "And why shouldn’t we be here?"
C "I didn't think I'd telling either of you. "
hide Cidleo
show Cidlec at right
C "Just because you show up here unannounced doesn’t mean I’m obligated to explain myself!."
A "I’m pretty sure your friends have the right to know why you suddenly stop talking to them."
A "You’ve always been open to us about what’s going on in your life and so have we!"
C "Maybe that should change."
A "We aren’t going anywhere until we get an explanation."
A "We came all this way for-"
C "For nothing! Coming here was pointless. I never wanted to be found and assuming that otherwise is a pretty selfish thing for your ends."
A "Selfish? You were the one who didn’t even take an effort to send a single message!"
P "We thought something might have happened to you and were worried."
C "That’s your problem to worry about, not mine."
C "All I should be worrying about right now is getting back to training. The thing I was doing before I was interrupted by you two."
A "Oh, so training is more important than talking to your friends?!"
C "Former. Friends."

"You and Anne stand there speechless."

C "*sigh* This is why I never wanted to talk about this."
C "If you’re so desperate to get some closure before you go back to California, here you go."
C "I chose to end this friendship when I stopped talking to you guys."
C "Makes the decision a lot easier."
P "Decision?"
C "I got a sports scholarship at one of my top college picks. A pretty good one, too."
C "I’ll have to train non-stop if I want to keep it, though. Which means no more video games and a lot less time on my phone."
P "And a lot less time being spent with us..."
C "Exactly. I decided that I’d rather end this friendship on my own terms rather than let it die out over time."
C "I’ll admit that cutting off all communication so abruptly was pretty harsh, but that was the easiest way I knew how to do it."
A "You never struck me as the type of guy who’d take the easy way out of things."
C "You never struck me as the type of girl who’d fly across the country just because I wouldn’t respond to a few texts."
C "But I guess we both underestimated each other."
A "A few texts…?"

"You stare at Anne’s expression. She looks like she’s about to burst."
hide Aangry2
show Asad2c at midtoleft
A "It’s been over a MONTH!"
A "We texted you!"
A "We called you!"
A "We never stopped trying to contact you!"
A "We were worried sick about you!"
A "*I* was worried sick about you!"
A "Y- you… You!"
"It looks like Anne is going to explode."
show Asad2c at left
A "You inconsiderate jerk!"
A "You could have said something! Anything!"

"Anne starts to cry. You notice Conrad has a pained expression on his face."

A "We should have never come looking for you!"
A "It would have been better if you stayed gone!"
C "…"
A "…"
P "… Anne…"
A "You really hurt me..."
C "Anne, I-"
C "I never meant for any of this to happen."
C "I should have handled everything differently..."
C "I thought that the longer I stayed friends with both of you, the harder it would be to let the both of you go."
C "So I took the easy way out by cutting off all communication."
C "Hurting you or making you worry about me was the last thing I wanted to do."
C "I guess I was running away. First time for everything, right?"
C "I’m sorry I didn’t say anything… I thought it would be better like this."
A "I just need to clear my head."
hide Asad2c
"(Anne runs away. You and Conrad stand there trying to take in everything she said.)"

C "She’s really hurt..."

C "I wouldn’t blame her if she doesn’t forgive me. I wouldn’t blame you if you don’t forgive me, too."

menu:
    "I forgive you.":
        P "I forgive you."
        C "Thank you, [P]"
        show Csmileo
        hide Cidlec
    "...":
        C "I understand."

C "I understand [P]."

C "I have a lot of regrets of the way I handled all of this."
C "What Anne said really stung, but I bet not as much as my words stung her."
C "I don’t know what hurt more, not hearing from me or hearing what I just said. All I know is that she’s hurting."
P "Come on, we have to go find her."
"You and Conrad walk back to the limo and find that it’s still there, but Anne is not inside. Anne must have left by foot."
C "Wait, I should stay here."
P "What are you talking about?"
C "You should go by yourself. She wouldn’t want to see me."
P "She flew across the country just to see you."
P "She’s upset right now, but it’s only because she cares deeply about you."
C "Are you sure?"
P "I’m positive. She’s done nothing but think about you for the past month."
C "I’m still a bit unsure about this, but okay. I’ll come with you."

"You and Conrad arrive at Aunt Tiff’s house."
jump act3
