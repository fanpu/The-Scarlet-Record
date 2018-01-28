label chapter_3:
    scene black
    
    "\"You and I will live together from now on.\""
    "A smile, the same smile that I would come to love."
    "A gentle voice that I would never grow tired of."
    "----- That was 6 years ago. Since then, I have never once wished for something else. As long as I was around Shin, there would be nothing else that I would ever need."
    "His smile, his voice... it was all perrfect to me. I needed nothing else."
    "I sometimes wondered what was outside. What the world was like. But it was fleeting. That wasn't important to me, and I made no effort to find out."
    "But now..."
    
    image wasteland = im.Scale("images/wasteland.png", 1920, 1080)
    scene wasteland
    with Dissolve(.5)
    
    show waifu
    
    "After getting out, all I see a wasteland with nothing nearby apart from the facility."
    "That was not particularly surprising, due to the apparent war making Earth inhabitable. Shin has talked about it at length"
    "The destruction caused was already apparent back home through the grimy windows. But I never realized how bad it was, inside the house"
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
    if choice_3_1:
    
        hide waifu
        show sad_waifu
    
        "It has been 3 hours, but there is not a single person to be found."
    
    else:
    
        hide waifu
        show sad_waifu
    
    "It has been 3 hours, but there are still no clues to be found, not even a lead."
    jump chapter_3_scene_1

label chapter_3_scene_1:
    p "Maybe I should turn back, this might be the wrong direction."
    "The world is a wasteland, but I should have found something by now."
    
    hide sad_waifu
    show waifu
    
    p "Hold on, what is that?"
    "It was very far away, but I can definitely see a person walking in my direction."
    if choice_3_1:
        p "Could he know where I am?"
    else:
        p "Could he know what I am?"
  
    p "..Something is wrong."
    w "<ERROR COMMUNICATION SYSTEMS DOWN ERROR...>"
    p "Communication system error. Won't be too hard to fix"
    jump chapter_3_fixing

label chapter_3_fixing:
    image circuitboard = im.Scale("images/circuitboard.jpg", 1920, 1080)
    scene circuitboard
    with Dissolve(.5)
    
    p "(The soundbytes are corrupted, but it should be easy to download new ones.)"
    w "<ERROR, SPEECH.MP3 NOT FOUND>"
    p "(There are radiowaves here...)"
    menu:
        jump chapter_3_scene_2
    
label chapter_3_scene_2:
    hide waifu
    show happy_waifu
    
    p "It's fixed. Or at least that's what I hope."
    
    hide happy_waifu
    show waifu
    
    "...She still doesn't seem...right."
    w "Kosuke, you're back!"
    
    hide waifu
    show confused_waifu
    
    p "I'm not-"
    w "I've missed you so much!"
    p "Me? But"
    w "Come with me, let's go home and watch the moon rise."
    p "..."
    w "Come on, why are you waiting? We do it all the time!"
    p "..."
    w "What's wrong. Do you have anyting on your mind? I'm here, don't worry, you can share."
    P "(Her actions...are eerily similar to mine.)"
    w "Come on, Kosuke. Let's spend some time together. Don't you miss me?"
    p "..."
    p "...I'm not Kosuke."
    w "...<ERROR PROGRAM CORRUPTED>"
    w "Kosuke! You're back!"
    p "..."
    w "Don't you miss me?"
    p "(She's broken...beyond repair. Likely a motherboard malfunction.)"
    w "Come on, Kosuke. Didn't you miss of the times we had?"
    
    hide confused_waifu
    show waifu
    
    p "(Should I...)"
    
menu:
    "Shut her off.":
        jump choice_3_2a
    "Let her be.":
        jump choice_3_2b

label choice_3_2a:
    
    hide waifu
    show sad_waifu
    
    "..."
    jump chapter_3_scene_3
           
label choice_3_2b:
    
    hide waifu
    show sad_waifu
    
    "(...I can't do anything for her)"
    jump chapter_3_scene_3

label chapter3_scene_3:
    p "(Is Kosuke her Shin?)"
    p "(Am I simply a clone of her?)"
    p "(...)"
    p "(My feelings for Shin, they are manufactured, aren't they?)"
    p "(...)"
    P "(I...I want to go back.)"
