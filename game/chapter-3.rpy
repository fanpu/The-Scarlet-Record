label chapter_3:
    image C3 = im.Scale("images/C3.png", 1920, 1080)
    scene C3
    with Dissolve(1)
    scene black
    with Dissolve(1)
    
    "\"You and I will live together from now on.\""
    "A smile, the same smile that I would come to love."
    "A gentle voice that I would never grow tired of."
    "----- That was 6 years ago. Since then, I have never once wished for something else. As long as I was around Shin, there would be nothing else that I would ever need."
    "His smile, his voice... it was all perrfect to me. I needed nothing else."
    "I sometimes wondered what was outside. What the world was like. But it was fleeting. That wasn't important to me, and I made no effort to find out."
    "But now..."
    
    image wasteland_chap3 = im.Scale("images/wasteland.png", 1920, 1080)
    scene wasteland_chap3
    with Dissolve(.5)
    
    show waifu neutral
    
    "After getting out, all I see a wasteland with nothing nearby apart from the facility."
    "That was not particularly surprising, due to the apparent war making Earth inhabitable. Shin has talked about it at length."
    "The destruction caused was already apparent back home through the grimy windows. But I never realized how bad it was, inside the house."
    p "It is truly a miracle that there are still people surviving here, or any sign of life, machine or human."
    "What should I do? What can I do?"
    p "Shin would miss me, I should go back quickly so that he will stop worrying."
    "That was definitely the choice I would have made just a few days ago."
    "What should I do now?"
    
menu:
    "Find my way to Shin.":
        jump choice_3_1a
    "Find clues about myself.":
        jump choice_3_1b

label choice_3_1a:
    $ choice_3_1 = True
    "Shin is still the most important to me. I should find clues of how to get back quickly. Hopefully I can find someone who knows where town is."
    jump choice_3_1done

label choice_3_1b:
    $ choice_3_1 = False
    "Maybe it is time for me to know more about myself. Shin can wait for awhile. Hopefully I can find someone or something who knows or says something about who I am."
    jump choice_3_1done
    
label choice_3_1done:
    scene black
    with Dissolve(.5)
    scene wasteland_chap3
    with Dissolve(.5)
    
    if choice_3_1:
    
        hide waifu neutral
        show waifu sad
    
        "It has been 3 hours, but there is not a single person to be found."
    
    else:
    
        hide waifu neutral
        show waifu sad
    
        "It has been 3 hours, but there are still no clues to be found, not even a lead."
    jump chapter_3_scene_1

label chapter_3_scene_1:
    p "Maybe I should turn back, this might be the wrong direction."
    "The world is a wasteland, but I should have found something by now."
    
    hide waifu sad
    show waifu neutral
    
    p "Hold on, what is that?"
    "It was very far away, but I can definitely see a person walking in my direction."
    if choice_3_1:
        p "Could he know where I am?"
    else:
        p "Could he know what I am?"
    
    show waifu neutral:
        xalign 0.25
        yalign 1.0
    show waifu2 neutral:
        xalign 0.75
        yalign 1.0
    
    p "..Something is wrong."
    w "<ERROR COMMUNICATION SYSTEMS DOWN ERROR...>"
    p "Communication system error. Won't be too hard to fix..."
    jump chapter_3_fixing

label chapter_3_fixing:
    image circuitboard = im.Scale("images/circuitboard.jpg", 1920, 1080)
    scene circuitboard
    with Dissolve(.5)

    p "(The soundbytes are corrupted, but it should be easy to download new ones.)"
    w "<ERROR, SPEECH.MP3 NOT FOUND>"
    p "(Before I start working on fixing the error, I should recall some my knowledge.)"
    jump exclusion

label exclusion:
    menu:
        p "(If a process is executing in its critical section, then no other processes can be executing in their critical section. This condition is called...)"

        "mutual exclusion":
            jump exclusionright
        "critical exclusion":
            jump exclusionwrong
        "synchronous exclusion":
            jump exclusionwrong
        "asynchronous exclusion":
            jump exclusionwrong

label exclusionright:
    p "(Yes, I recall now, mutual exclusion is the right answer. Turns out I have not forgotten everything yet)"
    p "(Just to be sure, I should recall another property.)"
    jump aging

label exclusionwrong:
    p "(No, that's definitely not the right answer. I should quickly recall the right property before I lose more time.)"
    jump exclusion

label aging:
    menu:
        p "('Aging' is...)"

        "keeping track of cache contents":
            jump agingwrong
        "keeping track of what pages are currently residing in memory":
            jump agingwrong
        "keeping track of how many times a given page is referenced":
            jump agingwrong
        "increasing the priority of jobs to ensure termination in a finite time":
            jump agingright

label agingright:
    p "(Yes, I remember what Aging is. Now I can confidently fix the error.)"
    p "(The CPU doesn't seem to be fetching instructions correctly.)"
    jump fetch

label agingwrong:
    p "(No, that's not the answer. I don't have much time to waste, I need to quickly recall my knowledge so that I can solve the problem.)"
    jump aging
    
label fetch:
    menu:
        p "(Instead, it should fetch the instruction from memory according to the value of...)"

        "program counter":
            jump fetchright
        "status register":
            jump fetchwrong
        "instruction register":
            jump fetchwrong
        "program status word":
            jump fetchwrong
    
label fetchright:
    p "(Let me try this...)"
    p "(It works! The CPU is now fetching information correctly.)"
    p "(But even after that, the problem still persists. It could be due to a long time for communication between the CPU and the communication module.)"
    jump scheduling

label fetchwrong:
    p "(Let me try this...)"
    p "(That didn't work, the CPU is still fetching information incorrectly.)"
    p "(I cannot make too many errors, if not I might run out of time.)"
    jump fetch

label scheduling:
    menu:
        p "(Which algorithm should I implement in the robot to have the minimum average waiting time for communication?)"

        "First Come, First Served":
            jump schedulingwrong
        "Shortest Job First":
            jump schedulingright
        "Round-robin":
            jump schedulingwrong
        "Priority":
            jump schedulingwrong
           
label schedulingright:
    p "(Let me try implementing this algorithm...)"
    p "(It worked, communication time has been reduced significantly.)"
    jump chapter_3_scene_2

label schedulingwrong:
    p "(Let me try implementing this algorithm...)"
    p "(It didn't work, the communication time is still the same as before. I can't waste time.)"
    jump scheduling
    
label chapter_3_scene_2:
    scene wasteland_chap3
    with Dissolve(.5)
    
    hide waifu neutral
    show waifu happy:
        xalign 0.25
        yalign 1.0
    show waifu2 happy:
        xalign 0.75
        yalign 1.0
    
    p "It's fixed. Or at least that's what I hope."
    
    hide waifu happy
    show waifu neutral:
        xalign 0.25
        yalign 1.0
    
    "...She still doesn't seem...right."
    w "Kosuke, you're back!"
    
    hide waifu neutral
    show waifu confused:
        xalign 0.25
        yalign 1.0
    
    p "I'm not-"
    w "I've missed you so much!"
    p "Me? But"
    w "Come with me, let's go home and watch the moon rise."
    p "..."
    w "Come on, why are you waiting? We do it all the time!"
    p "..."
    w "What's wrong. Do you have anyting on your mind? I'm here, don't worry, you can share."
    
    hide waifu confused
    show waifu thinking:
        xalign 0.25
        yalign 1.0
    
    p "(Her actions...are eerily similar to mine.)"
    w "Come on, Kosuke. Let's spend some time together. Don't you miss me?"
    p "..."
    p "...I'm not Kosuke."
    w "...<ERROR PROGRAM CORRUPTED>"
    w "Kosuke! You're back!"
    p "..."
    w "Don't you miss me?"
    
    hide waifu confused
    show waifu sad:
        xalign 0.25
        yalign 1.0
    
    p "(She's broken...beyond repair. Likely a motherboard malfunction.)"
    w "Come on, Kosuke. Didn't you miss of the times we had?"
    p "(Should I...)"
    
menu:
    "Shut her off.":
        jump choice_3_2a
    "Let her be.":
        jump choice_3_2b

label choice_3_2a:
    
    hide waifu2 happy
    hide waifu neutral
    show waifu sad
    
    "..."
    jump chapter_3_scene_3
           
label choice_3_2b:
    
    hide waifu2 happy
    hide waifu neutral
    show waifu sad
    
    "(...I can't do anything for her)"
    jump chapter_3_scene_3

label chapter_3_scene_3:
    p "(Is Kosuke her Shin?)"
    p "(Am I simply a clone of her?)"
    p "(...)"
    p "(My feelings for Shin, they are manufactured, aren't they?)"
    p "(...)"
    p "(I...I want to go back.)"
    jump chapter_4
