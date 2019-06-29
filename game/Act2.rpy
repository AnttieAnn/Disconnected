label act2:
        #hi
        define Pilot = ("Pilot")
        "As you check in your baggage, you receive a notification from Discord."
        "It's a message from Anne"
        A "Hey [P]! I'm leaving my flight now."
        A "Uh the first class plane is really nice, I wish you had let me pay for your ticket lol."
        A "We can keep talking if ya want so you don't get bored."
        A "Oh wait, actually, you better put your phone in airplane mode."
        A "I'll hear from ya in a few hours."
        "You board the plane, and the intercom speaks."
        Pilot "Thank you for flying with Omnia Airlines, please remember to put your phone into airplane mode."
        "Your moral compass tells you to put your phone into airplane mode, but."
        "There's an in game event for this game you play on your phone, and it requires the internet.."
        menu:
            "Put phone into airplane mode":
                $ Airplanemode = "ye"
                "You put your phone in airplane mode."
                "+1 brownie points for being a good person."
                "This is your pilot speaking, we will be taking off momentarily."
                "You decide to doze off and take a nap..."
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
                "A few hours later"
                Pilot "This is your pilot speaking, due to phones not being shut off or put in airplane mode, we are being forced to make a stop on the ground."
                "Please remain seated."
                "Some time passes, and eventually after many delays, the plane is back up in the air, and you arrive in Orlando shortly."

        if Airplanemode == "ye":
            $ AHP -= 1
            jump planedone
        if Airplanemode == "non":
            $ AHP += 100
            jump planedone


label planedone:
        "You exit the plane, spend 50 minutes searching for your luggage, and are now in the lobby."
        "You open up your discord, to see several messages from Anne."
        A "Just arrived in Orlando! ✈️"
        A "Your flight should be arriving a little later than mine."
        A "I’ll take a quick nap at the airport lobby so I don’t miss you."
        A "Or actually, maybe I should go check out the gift shop to see if I can find anything to surprise you!"
        A "Oops! Guess I ruined the surprise…"
        A "Oh well, since you already know that I’m going to get you something I’ll let you choose what gift I get for you."
        A "It’s the least I could do since you came all the way here to help me out!"
        A "There’s a cool-looking alligator keychain. The alligator’s jaws also double as a bottle opener! It’s really handy."
        A "But there’s also a cute necklace of an orange with a smiley face on it!"
        A "I actually can't stand oranges, they remind me of this one really annoying character from an anime I watched."
        A "But this necklace is pretty cool. It even lights up when you click on it! It’s really bright."
        A "I can’t decide. Which would you like me to buy?"
menu:
    "Alligator.":
        "[P] is typing..."
        "You realize that there are more of Anne's messages to read."
    "Orange.":
        "[P] is typing..."
        "You realize that there are more of Anne's messages to read."
A "Oh wait, why am I messaging you lol. You're phone is still in airplane mode."
A "I'm assuming it is, you really have to be a terrible person to not turn on airplane mode."
A "Guess I’ll have to choose myself. At least I’ll be able to surprise you!"
"After you stop typing, you immediately see Anne begin to type."
A "Hey! I hope you aren't typing on the plane."
A "Your plane should have arrived by now, right? How was your flight?"
menu:
    "Pretty smooth, no delays or anything.":
        P "Pretty smooth, no delays or anything."
        P "The pilot even said it was the smoothest flight ever."
    "Pretty rough, we had quite a few delays.":
        P "Pretty rough, we had quite a few delays."
        A "Aw, I'm sorry to hear that."

A "I couldn’t sleep a wink, I kept worrying about Conrad."
A "But, hey! That’s why we’re here, right? To make sure he’s safe so we stop worrying about him!"
A "I’m over here by the gift shop. Haven’t left ever since I landed. It’s really easy to pass the time just browsing."
A "Can you see me? I'm wearing a black shirt."
"You look around and see Anne facing away from you, staring intently at her phone."
menu:
    "Scare her":
        "You walk up to Anne and scare her."
        P "boo!"
        A "ahhHHHH"
        $ AHP = AHP + 1
        #Add Ahole point increase here
        A "What the hell?!?"
        A "Just who the hell do you think you are you piece of..."
        "Anne suddenly recognizes you."
    "Approach her":
        "You walk around so you don't scare her."
        P "Hey"
        "Anne looks up and instantly recognizes you."
A "OH MY GOSH HI!!"
"Anne extends her arm for a hug."
menu:
    "Hug her.":
        "You accept the hug."
    "Reach for a handshake":
        "You reach your hand out for a shake."
        "Anne realizes what you're doing, puts her hands down and reaches out."
        A "S-Sorry, I just got really excited."
        "Anne shakes your hand, firmly grasping it."
A "I can’t believe this is our first time meeting in real life, I wish it was for a better reason though."
A "I know I’ve seen pictures of you in the past, but it’s still pretty freaky finally seeing your face in person."
A "Wait, that came out wrong!"
A "You look nice in person, [P]. And in photos!"
A "Anyways, we can talk more later. We should be looking for our ride."
A "My aunt sent someone to pick us up and they should be here by now."
"You notice a very tall man wearing professional attire holding up a sign:"
"Pick-up for Miss Anne. G."
"As soon as Anne makes eye contact with the man, she runs up and hugs him."
A "FREIGHT TRAIN!!"
"The man embraces her back."
A "[P] This is one of my aunt's employees. Freight Train."
A "I uh, don't know his actual name, but he just goes by Freight Train."
define F = ("Freight Train")
F "What's up tiny person"
"You try to make out Freight Train's face, but are too intimidated to get a closer look."
if AHP < 0:
    F "I like him."
if AHP < 99:
    "Freight Train is observing you, he looks like a tough guy."
    jump limo
if AHP > 99:
    F "I don't like this guy."
    F "Seems like the fella would wouldn't turn on Airplane mode."
    A "Oh don't worry Freight Train, I'm sure [P] uses airplane mode whenever he's on an airline."
    A "After all, you have to be a special kind of evil to not use Airplane mode."
    jump limo
label limo:
    A "So uh, lets head out!"
    "You follow Freight Train outside the airport, a big black limo is there waiting for you."
menu:
    "That's a beautiful car.":
        P "That's a beautiful car."
        A "O-oh, my Aunt went a little overboard, I could have just gotten a rental car."
    "Wow I didn't know that you were so rich.":
        P "Wow I didn't know that you were so rich."
        A "O-oh no its not like that!"
        A "My aunt is the one with the money."
        A "She even bought me first class tickets for my trip over here! I told her it was unnecessary, but she insisted."
        A "Too bad I couldn’t figure out how to use the bed recliner."
        A "It was pretty awkward eating sushi with the headrest reclined all the way to the back."
        "You start to regret not letting Anne pay for your tickets"
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
        "Anne looks pretty pissed."
        A "[P] you scared the crap out of me!"
        "You can feel Freight Train staring at you through the rear view mirror."
        "You and Anne exit the limo."
        "Anne leads you to the door, and rings the doorbell."
        "A nice looking women answers the door."
        whomst "Hello...?"
        A "Aunt Tiff!"
        "Anne and her aunt immediately embrace."

    "Let her sleep":
        "You allow Anne to continue sleeping."
        "You exit the limo, and walk up to the front door."
        "You ring the doorbell"
        whomst "Hello...?"
        whomst "And you are...?"
        "You hear the sound of Anne exiting the limo."
        A "Aunt Tiff!"
        "Anne runs up to her Aunt and embraces her."
T "Oh my goodness my little BrilliAnne. I hardly recognized you."
A "Aunt Tiff this is my friend, [P]."
P "It's a pleasure to meet you m'am."
P "BrilliAnne?"
A "Oh, uh, back when I was little, I used to say 'Brilliant' all the time."
A "I guess it was kinda my catchphrase."
T "Oh? Anne didn’t tell me she was bringing over a friend to visit. The more the merrier!"
T "And please, You can call me aunt Tiff! There’s no need to call me ma’am."
T "Just how old do you think I am?"
menu:
    "30":
        P "30? You seem pretty young to be an aunt."
        T "Oh, I like them."
    "40":
        P "40? since you're Anne's aunt I assume you must be older than Anne by a little bit."
        T "..."
        A "..."
    "60":
        P "60? You look pretty old."
        T "Oh, really? I don't have to let you in my home ya know."
        A "Aunt Tiff!"
"Aunt Tiff leads you into the dining room."
A "Wow, it’s been such a long time since I’ve visited here. Your house has changed so much; I can barely recognize it!"
A "I don’t remember the dining room being this big."
T "As time went on, my company grew larger and larger. I suppose that the same applied to my home."

T "If you need anything, I’ll be in the kitchen preparing some snacks for the two of you."
T "Make yourselves at home!"

"Aunt Tiff exits the room, leaving you and Anne by yourselves."

P "You and your aunt seem to be really close."
A "Yeah, since I’m her only niece so I’ve always been given special treatment."
A "It’s a shame that she’s so busy with her business here in Orlando. We rarely get to see each other."
P "I’m glad that you’re able to get together again with your aunt after all these years apart, but I’m sad it’s under these circumstances."
T "What circumstances?"

"You turn around and see Aunt Tiff holding a decorative bowl that resembles a barrel filled with crackers for you and Anne."

"You immediately regret your choice of words when you see the look on Anne’s face."

A "Oh, um, I was meaning to tell you about this eventually…"
A "[P] and I are in Florida to find a missing friend. He hasn’t been answering any of our messages or calls and we’ve been really worried about him."
A "Ah, I see. You should have told me you were here for more than just a friendly visit, Anne."
A "I’m sorry, I just didn’t want to make you feel bad and think that was the only reason I came to Florida…"
A "That’s fine, I’m just glad you’re here. So this friend of yours, tell me about him. "
A "It seems that he’s very special for both of you to come all the way here searching for him."

"You and Anne spent the rest of the evening telling stories about Conrad to Aunt Tiff."

"During that time, you can’t help but notice a smile on Anne’s face as she reminisced about your time together."

"You started to smile as well."

"And then you started to tell her about Conrad’s sudden disappearance…"

T "I can tell that Conrad is a nice friend from the stories you’ve told. But It’s awfully strange that he would just disappear on you both like that."
A "Yeah, that’s why we’re really worried about where he is right now. We have to find him! That’s what he would want us to do."
T "Are you sure about that?"
A "What do you mean?"
T "I had many friendships, relationships, and connections with different people."
T "Many of them left an impact on my life. Some deeper than others. "
T "Although some of them may be gone, they left an impression on me that stayed."
T "It seems that wherever Conrad may be, he has left an impression on both of you that will also stay."
T "And I’m sure that both of you have also left an impression on him."
A "I understand what you’re trying to say, but he isn’t gone yet."
A "I don’t understand why he stopped talking to us… Or where he went..."
A "But, he’s still going to be a big part of our lives and everything will go back to the way it used to be. We just have to go and find him!"
A "So that’s why we’re still going to keep looking for him! Right, [P]?"
"You nod in agreement."
T "Well I wish the two of you the best of luck."
A "Thanks Aunt Tiff."
A "[P] we should hit the hay, we're meeting Conrad's friend easrly tomorrow morning."
A "Be sure to wake up bright and early."
"Anne leaves for her room upstairs."
T "So uh, [P], was it?"
T "How did you and Anne meet?"
menu:
    "Over the internet.":
        P "Over the internet."
        T "Really? I've always wanted to try one of those online dating apps."
        P "Actually, we didn't use a dating app. We have a software called discord."

    "We met a few years ago.":
        P "We met a few years ago."
        T "Really? well that's cool."
        T "Did you all use an online dating app? I've been meaning to give one of those a try."
        P "Actually, we aren't dating, but there is this app called discord that we use."

T "This cord? What about it?"
"Aunt Tiff holds up a cable of some sort."
P "No no no, DIScord. It's an online messaging app."
T "What's discord?"
"You explain to Aunt Tiff what discord is." #Sort of fade in and out between phrases to show a pasasage of time and that we are leaving stuff out.
T "The hypesquad you say? So that's what was on Anne's shirt." #fade
P "There's this thing called a Wumpus, he's sort of like the mascot."
T "A wumpus? What kind of word is that?" #fade
T "It took them THAT long to add screenshare??! Was it worth the wait?" #fade
T "You use it to play what game? Super Smas-"#fade
P "But yeah, that's pretty much it."
T "Huh, that's a really neat program."
T "Right now the chat platform I use feels so outdated."
T "Anyway [P], you should go to bed, you have an early day tomorrow."
T "Your room is straight down that hall on the second floor, last door to the right."
"You head to your room, get into the bed, and doze off..."
"The next morning..."
"You wake up early, about 90 minutes before you're supposed to leave."
"You walk outside, and realize that no one is awake."
"Anne must still be sleeping, her room isn't that far away."
menu:
    "Wake her":
        "You decide to wake Anne up."
        "You enter Anne's room, she's passed out on the bed."
        "You throw your entire body on the mattress."
        A "ahhHHHH"
        A "Oh, [P] it's just you."
        A "Looks like I slept in, we should head out."


    "Let her sleep":
        "You let her sleep."
        "You go downstairs to the kitchen and see Aunt Tiffany making some breakfast."
        T "Hello [P]!"
        T "Oh...? Is Anne not awake yet?"
        T "Let me go get her..."
        "Aunt Tiffany walks upstairs to Anne's room. In the distance you hear her scare Anne awake."
        A "ahhHHHH"
"Aunt Tiffany serves the both of you breakfast."
"She made a lot of food for the both of you. Eggs, bacon, grits, and even a hashbrown casserole!"
"There are some biscuits, with gravy for dipping."
A "Thank you for breakfast Aunt Tiff, we'll be headed out now."
T "Good luck BrilliAnee, I hope ya find your friend!"
"You and Anne step outside."
A "Okay [P], we're meeting Conrad's friend at a football field."
A "She said he'd probably be there."
A "Freight Train will be here soon with the limo, Aunt Tiff told me that we could use it all day."
"You see the limo pull up and get in."
"Freight Train drives you to a football field."
"You look out and see a number of football players practicing, with a few spectators."
A "Let's see if we can find Jade."
"You sit in the stands, looking around for her."
define J = ("Jade")
whomst "You look lost, can I help you?"
A "O-Oh! We're just looking for a friend."
whomst "Really? Which friend?"
A "Well, a friend who's gonna take us to our other friend, so we can find out if he's okay."
"Anne pulls out a picture of Conrad."
A "You wouldn't happen to know who this is do you? I was told he might be around here."
whomst "Conrad?"
A "Yeah! Do you know him?"
J "I’d like to think so. It would be pretty strange if I didn’t during all those years of dating."
A "Wait a minute, Jade?"
J "Took ya long enough to recognize me, and Conrad said you were supposed to be the smart one."
J "How are you doing Anne?"
A "Oh my gosh I didn't even recognize you! Which makes sense because I've literally never seen your face before."
A "[P] this is Jade, Conrad's girlfriend."
J "Ex-girlfriend, currently."
A "Oh, I’m sorry! I didn’t realize…"
J "It’s fine, it was fairly recent so I don’t expect you to have known. Guess I didn't mention it when we were talking."
J "Now that I think about it, Conrad did mention having friends from California. I apologize for not being able to recognize you both."
A "Can you help us find him? It’s really important."
J "We haven’t talked to each other since we’ve broken up, so I’m not quite sure where he is right now."
P "When was that, if you don’t mind me asking?"
J "A little over a month ago."
A "That’s around the same time he stopped talking to us..."
J "He's out there walking onto the field."
J "He just got out of church, so he's talking to some of his buddies before they practice."
A "Brilliant! I can see him."
J "Be careful if you approach him, he gets really serious when he's practicing."
A "That's funny, he gets really passionate about video games when we play together."
A "Er. used to play."
J "Well I'm glad I could help ya find him."
J "Best of luck to ya."
A "Jade is really nice. I wonder why she and Conrad broke up?"
A "And around the same time he stopped talking to us…"
A "There’s so many people on the field. I can’t see any of their faces behind those football helmets."
P "How will we be able to tell which one is Conrad?"
A "We’ll have to take a closer look at the players if we want to find him."

"Anne starts to approach the inner field, but you immediately stop her"

P "Hey, Anne. There’s a sign posted right here."
"Please stay five feet away from the inner field at all times."

A "What about it?"

menu:
    "Follow the sign, we should stay back.":
        P "Follow the sign. We should stay here."
        A "No way!"
        A "We’ve already gotten this far. We can’t let a stupid sign stop us"
        A "I’ll go by myself. You can stay on the lookout."

        "Anne tries to sneak further onto the field to get a better look. You stay behind."

        "Luckily, there Anne is pretty good at sleuthing around. And all the players are too busy playing football."

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
        "Luckily, you and Anne are good at sleuthing, and all the players are too busy playing football."
        A "I can't see him."
        "Anne checks something on her phone, but doesn't notice a football player headed straight for her."
        P "LOOK OUT!!!"
        A "ahhHHHH"
        "The football player tackles Anne, and she falls to the ground."
whomst "bruh, watch where you're going."
A "Ouch..."
"Anne got knocked down pretty hard, but she seems alright."
whomst "That scream..."
C "Anne???!"
"Conrad runs over from the sidelines."
A"Conrad?"
C"Anne? What are you doing here?"
C"And [P], too?!"
C"Let’s go move to the side, unless you want to get tackled by another player."

"You, Conrad, and Anne walk off the field to talk."

A "We’ve been looking everywhere for you! I’m glad we were able to find you."
C "Yeah, that makes one of us…"
A "What are you talking about?"
C "You two shouldn’t have come here."

"You notice Anne’s smile slowly begin to fade. You can’t hide the disappointment in your face, either."

P "What happened to you? Why haven’t you been contacting us?"
A "And why shouldn’t we be here?"
C "I never planned on telling either of you. "
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

A "It’s been over a MONTH!"
A "We texted you!"
A "We called you!"
A "We never stopped trying to contact you!"
A "We were worried sick about you!"
A "*I* was worried sick about you!"
A "Y- you… You!"
"It looks like Anne is going to explode. What should you do?"
menu:
    "Let her explode.":
        P "..."
    P "Anne-"
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
A "I- I didn’t expect to blow up like that."
A "It’s just all too painful to hear. "
A "I’m not sure if I don’t understand or if I don’t want to understand."
A "All I know is that I feel hurt and confused."
A "I have to go and clear my head. I’m sorry about what I said..."

"Anne runs away. You and Conrad stand there trying to take in everything she said.)"

C "She’s really hurt..."
C "I wouldn’t blame her if she doesn’t forgive me. I wouldn’t blame you if you don’t forgive me, too."

menu:
    "I forgive you.":
        P "I forgive you."
        C "Thank you, [P]"
    "...":
        C "I understand."

C "I understand, [P]."

C "I have a lot of regrets of the way I handled all of this."
C "What Anne said really stung, but I bet not as much as my words stung her."
C "I don’t know what hurt more, not hearing from me or hearing what I just said. All I know is that she’s hurting."
P "Come on, we have to go find her."
"You and Conrad walk back to the limo and find that it’s still there, but Anne is not inside. Anne must have left by foot.)"
C "Wait, I should stay here."
P "What are you talking about?"
C "You should go by yourself. She wouldn’t want to see me."
P "She flew across the country just to see you."
P "She’s upset right now, but it’s only because she cares deeply about you."
C "Are you sure?"
P "I’m positive. She’s done nothing but think about you for the past month."
C "I’m still a bit unsure about this, but okay. I’ll come with you."

"You and Conrad arrive at aunt Tiff’s house."
