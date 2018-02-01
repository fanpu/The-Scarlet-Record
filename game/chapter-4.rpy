image bg_chap4 = im.Scale("wasteland2.jpg", 1920, 1080)
define p = Character("Player")
define po = Character("Poet")

image p angry = "waifu angry.png"
image p confused = "waifu confused.png"
image p sadbuthappy = "waifu crying but happy.png"
image p exhausted = "waifu exhausted.png"
image p happy = "waifu happy.png"
image p neutral = "waifu neutral.png"
image p relieved = "waifu relieved.png"
image p sad = "waifu sad.png"
image p thinking = "waifu thinking.png"
image p verysad = "waifu very sad.png"

image po happy = "poet happy.png"
image po slightlyangry = "poet slightly angry.png"
image po slightlyworried = "poet slightly worried.png"
image po smile = "poet smile.png"
image po veryangry = "poet very angry.png"
image po worried = "poet worried.png"

label chapter_4:
    image C4 = im.Scale("images/C4.png", 1920, 1080)
    scene C4
    with Dissolve(1)
    scene bg_chap4
    with Dissolve(1)
    jump ch4start

label ch4start:

    show p neutral
    p "Poor [other_bot_name]... "
    show p sad

    p "Never mind, I should worry more about myself. Just where am I?"
    show p confused at left

    #Wandering

    p "Is that someone in the distance? Hopefully she will know the way back to Shin’s place..."

    show po slightlyworried at right
    po "Once upon a midnight dreary, while I pondered, weak and weary,"
    po "Over many a quaint and curious volume of forgotten lore—"

    show p neutral at left

    p "Excuse me?"
    po "Impossible! You are just but a figment of my imagination! See!"

    show po slightlyangry:
        xpos 1100
        linear 2.0 xpos 500

    #poet walks into the player only to realize she is real

    show p confused at left
    p "Well, if that helps you to recognize that I'm real..."

    show po slightlyangry:
        xpos 500
        linear 1.5 xpos 1000

    show po veryangry at right
    po "No! You exist but do not exist! I am the Chosen One! I am the only one left on this world! There cannot be anyone else! The sensation that is you is just a false sensation!"
    p "Umm.. Okay... But could you help me for a bit?"
    po "Such a situation is impossible! After all, I am the chosen talent residing in this gift of a planet! I am the representation of God and His will!"
    p "Then what would it take for me to convince you that I am here, and I am me?"
    show po slightlyangry at right
    po "Hm... Then answer the question from the Gods!"
    
    jump feelingQuiz

label feelingQuiz:
    "In this quiz, you have to identify words that represent feelings to show that you comprehend and can exhibit emotions."
    $ quiz_score = 0
    
    # Question 1
    menu:
        "Which of the following feelings best represents anger?"
        "Sad":
            p "Sad."
        "Sleepy":
            p "Sleepy."
        "Bitter":
            p "Bitter."
        "Furious":
            p "Furious."
            $ quiz_score += 1

    # Question 2
    menu:
        "Which of the following feelings best represents sadness?"    
        "Solemn":
            p "Solemn."
        "Melancholy":
            p "Melancholy."
            $ quiz_score += 1
        "Sleepy":
            p "Sleepy."
        "Salty":
            p "Salty."

    # Question 3
    menu:
        "Which of the following feelings best represents happiness?"
        "Ecstatic":
            p "Ecstatic."
            $ quiz_score += 1
        "Depression":
            p "Depression."
        "Sleepy":
            p "Sleepy."
        "Angry":
            p "Angry."

    if quiz_score == 3:
        "Congratulations!"
        jump ch4mid
    else:
        "You got [quiz_score] out of 3 questions correct."
        "Try again!"
        jump feelingQuiz

label ch4mid:
    show p neutral at left
    po "Wait so you are actually real.. I can’t believe it..."
    po "And I thought I was the one graced by the heavens, the one blessed with the gift of this very cursed world..."

    show po veryangry at right
    po "WAIT! Yes! It makes total sense! I AM the chosen human, and YOU are the chosen android! The ying to my yang! The logic to my emotions! Together, we shall birth a grand new world!"

    p "(He's crazy. Totally crazy. Trying to rope me into his msaterplan too?)"

    po "BUT, I cannot just let any robot to be my partner, my right-hand man-er android."
    po "Complete this quiz and show me that you are worthy of standing shoulder to shoulder with the Chosen One!"
    
    jump networkQuiz

label networkQuiz:
    $ quiz_score = 0
    $ correct = False
    
    # Question 1
    po "Which of the following protocols uses both TCP and UDP?"
    menu:
        "Which of the following protocols uses both TCP and UDP?"
        "FTP":
            p "FTP"
        "SMTP":
            p "SMTP"
        "Telnet":
            p "Telnet"
        "DNS":
            p "DNS"
            $ correct = True
        "None of the above":
            p "None of the above"

    if correct == False:
        "DNS uses TCP for zone exchanges between servers and UDP when a client is trying to resolve a hostname to an IP address."
    else:    
        $ quiz_score += 1
        $ correct = False

    # Question 2
    po "What protocol is used to find the hardware address of a local device?"
    menu:
        "What protocol is used to find the hardware address of a local device?"
        "RARP":
            p "RARP"
        "ARP":
            p "ARP"
            $ correct = True
        "IP":
            p "IP"
        "ICMP":
            p "ICMP"
        "None of the above":
            p "None of the above"

    if correct == False:
        "Address Resolution Protocol (ARP) is used to find the hardware address from a known IP address."
    else:    
        $ quiz_score += 1
        $ correct = False

    # Question 3
    po "A device that links two homogeneous packet-broadcast local networks, is a"
    menu:
        "A device that links two homogeneous packet-broadcast local networks, is a"
        "gateway":
            p "gateway"
        "repeater":
            p "repeater"
        "bridge":
            p "bridge"
            $ correct = True
        "hub":
            p "hub"    
        "None of the above":
            p "None of the above"

    if correct == False:
        "A gateway is a node (router) in a computer network, a key stopping point for data on its way to or from other networks."
        "A repeater is a network device used to regenerate or replicate a signal."
        "A hub is the most basic networking device that connects multiple computers or other network devices together."
        "By elimination, the answer is bridge."
    else:
        $ quiz_score += 1
        $ correct = False

    # Question 4
    po "Layer one of the OSI model is the"
    menu:
        "Layer one of the OSI model is the"
        "physical layer":
            p "physical layer"
            $ correct = True
        "link layer":
            p "link layer"
        "transport layer":
            p "transport layer"
        "network layer":
            p "network layer"    
        "None of the above":
            p "None of the above"

    if correct == False:
        "Layer one of the OSI model describes the most fundamental layer, which is the physical layer."
    else:
        $ quiz_score += 1
        $ correct = False

label ch4end:
    show p happy at left
    show po smile at right
    po "You... you are more capable than I thought. I finally found my equal! Step into the light and join me!"
    p "(He's totally bonkers)"
    p "Yes, right after I run an errand. I need to get to [home_address], and after that I'll be right back."
    p "However, I need directions"
    po "Ah ah ah! So this is the start of our official partnership!"
    po "Let's see..."
    po "By my vast knowledge of the pre-crisis era, the location that you ask for is the North-East direction!"

    p "Well, thanks..."

    show po happy at right
    po "No worries! When you return, we shall start the herald of a brave new world!"
    hide po
    #po disappear, out of scene

    show p relieved
    p "Whew, he has more than a few screws loose... But at the very least that’s the first lead I’ve gotten."

    show p neutral
    p "I hope I can return back to Shin soon..."

    "And so, [bot_name] continues her journey to look for Shin."
    jump chapter_5
