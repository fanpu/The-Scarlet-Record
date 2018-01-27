label start:
    jump ch4start
    
label ch4start:
    p "That poor <insert waifubot name>... "

    p "Never mind, I should worry more about myself. Just where am I?"

    #Wandering

    p "Is that someone in the distance? Hopefully he will know the way back to Shin’s place..."

    po "Once upon a midnight dreary, while I pondered, weak and weary,"
    po "Over many a quaint and curious volume of forgotten lore—"

    p "Excuse me?"

    po "Impossible! You are just but a figment of my imagination! See!"

    #poet walks into the player only to realize she is real

    p "Well, if that helps you to recognize that I'm real..."

    po "No! You exist but do not exist! I am the Chosen One! I am the only one left on this world! There cannot be anyone else! The sensation that is you is just a false sensation!"

    p "Umm.. Okay... But could you help me for a bit?"

    po "Such a situation is impossible! After all, I am the chosen talent residing in this gift of a planet! I am the representation of God and His will!"

    p "Then what would it take for me to convince you that I am here, and I am me?"

    po "Hm… Then answer the question from the Gods!"
    
    jump feelingQuiz

label feelingQuiz:
    "In this quiz, you have to identify words that represent feelings to show that you comprehend and can exhibit emotions."
    $ quiz_score = 0
    
    # Question 1
    "Which of the following feelings best represents anger?"
    menu:
        "Which of the following feelings best represents anger?"
        "Sad":
            p "Sad"
        "Sleepy":
            p "Sleepy"
        "Bitter":
            p "Bitter"
        "Furious":
            p "Furious"
            $ quiz_score += 1

    # Question 2
    "Which of the following feelings best represents sadness?"
    menu:
        "Which of the following feelings best represents sadness?"    
        "Solemn":
            p "Solemn"
        "Melancholy":
            p "Melancholy"
            $ quiz_score += 1
        "Sleepy":
            p "Sleepy"
        "Salty":
            p "Salty"

    # Question 3
    "Which of the following feelings best represents happiness?"
    menu:
        "Which of the following feelings best represents happiness?"
        "Ecstatic":
            p "Ecstatic"
            $ quiz_score += 1
        "Depression":
            p "Depression"
        "Sleepy":
            p "Sleepy"
        "Angry":
            p "Angry"

    if quiz_score == 3:
        "Congratulations!"
        jump ch4mid
    else:
        "You got [quiz_score] out of 3 questions correct."
        "Try again!"
        jump feelingQuiz

label ch4mid:
    po "Wait so you are actually real.. I can’t believe it..."
    po "And I thought I was the one graced by the heavens, the one blessed with the gift of this very cursed world..."
    po "HOWEVER! You are but a robot! A being to mirror Humans! Show me that you deserve the help of the Chosen Human!"

    p "So he still believes that he is a \"chosen one\". Sigh.."
    po "Complete this quiz and show me that you are worthy of help from me."
    
    jump networkQuiz

label networkQuiz:
    $ quiz_score = 0
    
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
            $ quiz_score += 1
        "None of the above":
            p "None of the above"

    # Question 2
    po "What protocol is used to find the hardware address of a local device?"
    menu:
        "What protocol is used to find the hardware address of a local device?"
        "RARP":
            p "RARP"
        "ARP":
            p "ARP"
            $ quiz_score += 1
        "IP":
            p "IP"
        "ICMP":
            p "ICMP"
        "None of the above":
            p "None of the above"

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
            $ quiz_score += 1
        "hub":
            p "hub"    
        "None of the above":
            p "None of the above"

    # Question 4
    po "Layer one of the OSI model is the"
    menu:
        "Layer one of the OSI model is the"
        "physical layer":
            p "physical layer"
            $ quiz_score += 1
        "link layer":
            p "link layer"
        "transport layer":
            p "transport layer"
        "network layer":
            p "network layer"    
        "None of the above":
            p "None of the above"

    if quiz_score == 4:
        "Congratulations!"
        jump ch4end
    else:
        "You got [quiz_score] out of 4 questions correct."
        "Try again!"
        jump networkQuiz

label ch4end:
    po "You... you are more capable than I thought. As I am truly a man of my word, what can I help you with? Ask and you shall receive."
    p "Yes.. Then, do you know how to get to <insert address here>?"
    po "By my vast knowledge of the pre-crisis era, the location that you ask for is <insert something>"

    p "Thank you so much!"

    po "No worries! For it is my duty as the Chosen Human! For that is my Noblesse Oblige!"

    #po disappear, out of scene

    p "That wasn’t very useful.. But at the very least that’s the first lead I’ve gotten."
    p "I hope I can return back to Shin soon..."

    "<Insert player name> continues her journey to look for her master walking towards <insert random landmark/direc>"
