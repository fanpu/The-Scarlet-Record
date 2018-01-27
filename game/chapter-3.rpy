label chapter_3:
    scene black
    
    "\"You and I will live together from now on.\""
    "A smile, the same smile that I would come to love."
    "A gentle voice that I would never grow tired of."
    "----- That was 6 years ago. Since then, I have never once wished for something else. As long as I was around Shin, there would be nothing else that I would ever need."
    "His smile, his voice... it was all eprfect to me. I needed nothing else."
    "I sometimes thought of my origin. Who made me? What was my purpose?"
    "But that wasn't important to me, and I made no effort to find out."
    "But now..."
    
    image wasteland = im.Scale("images/wasteland.png", 1920, 1080)
    scene wasteland
    
    "After getting out, I found myself in a wasteland with nothing nearby apart from the facility."
    "That was not particularly surprising, due to the nuclear war in 2020 making the Earth uninhabitable."
    "The destruction caused was already apparent back at our town. However, it was only now, without Shin, that I truly felt the despair that humans still on Earth felt."
    p "It is truly a miracle that there are still people surviving here."
    "I had hoped that the surroundings would help me decide where to go next, but the empty wasteland did not provide anything meaningful. I did not have a plan of what to do next."
    p "Shin would miss me, I should go back quickly so that he will stop worrying."
    "That was definitely the choice I would have made just a few days ago. However, after the kidnapping, I felt a need to truly find out who I am."
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
    "Maybe it is time for me to know more about myself. Shin can wait for awhile. Hopefully I can find someone who knows something about who I am."
    jump choice_3_1done
    
label choice_3_1done:
    if choice_3_1:
        "It has been 3 hours, but there is not a single person to be found."
    else:
        "It has been 3 hours, but there are still no clues to be found."
    jump chapter_3_scene_1

label chapter_3_scene_1:
    p "Maybe I should turn back, this might be the wrong direction."
    "The world is a wasteland, but I should have found something by now."
    p "Hold on, what is that?"
    "It was very far away, but I can definitely see a person walking in my direction."
    if choice_3_1:
        p "He might know where our home is, I should talk to him."
    else:
        p "He might know something about me, I should talk to him."
    "As the person got closer, it became clear that it was not human, just like me. However, I noticed something else..."
    "The robot looked exactly like me. but as it got closer..."
    w "<ERROR COMMUNICATION SYSTEMS DOWN ERROR...>"
    "Her communication module is spoilt, I will have to fix it if I want information from her."
    jump chapter_3_fixing

label chapter_3_fixing:
    "WIP"
    jump chapter_3_scene_2
    
label chapter_3_scene_2:
    p "Alright, it's done!"
    "That was really hard, but I'm glad that I managed to fix it."
    w "Thanks, now I can go back to finding my owner Rin. I have spent my whoel life with her, I must find her..."
    "That's weird, it's exactly how I feel about Shin. Could that mean..."
    "me and that robot are both programmed to love our owners?"
    p "No, that cannot be..."
    w "What are you talking ab - <ERROR PROGRAM CORRUPTED>"
    "I must have missed something while fixing her, let me check..."
    "I opened up her circuit box again, but this time I caught something that I missed"
    "The mineral used to power robots, waifunium, was gone. Nothing can be done to fix her."
    "The only thing I can do is shut off the robot, but that would mean her death."
    "I could leave her like this, but she would never be able to function properly."
    "What should I do?"
    
menu:
    "Shut her off.":
        jump choice_3_2a
    "Let her be.":
        jump choice_3_2b

label choice_3_2a:
    "I can't leave her like this, I have to shut off her power."
    "I quickly opened the circuit and shut her off permanently."
    jump chapter_3_scene_3
           
label choice_3_2b:
    "I can't kill her, I will just leave her here and carry on."
    jump chapter_3_scene_3

label chapter_3_scene_3:
    if choice_3_1:
        "After leaving the robot behind, I continued seraching for Shin, with many questions in my mind."
    else:
        "After leaving the robot behind, I decided to search for Shin instead. There are many questions which I have to ask him."

    "What am I? Where did I come from? What is my purpose? And perhaps most importantly..."
    "Do I really love Shin?"
