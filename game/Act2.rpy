label act2:
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
        $ Airplanemode = "true"
        "You put your phone in airplane mode."
        "+1 brownie points for being a good person."
        "This is your pilot speaking, we will be taking off momentarily."
        "You decide to doze off and take a nap..."
        "A few hours later.."
        Pilot "This is your pilot speaking, just letting you know that this was the smoothest flight of my career, and that we will  be touching down in Orlando momentaily"
    "Keep internet on.":
        "You decide that your weeaboo rhythm game is much more important than the safety of you and the passengers."
        $Airplanemode = "false" #Add 100 Aholepoints, so that they can't get any nice dialogue
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
