transform kidnapper_transform:
    zoom 0.7

label chapter_2:
    image C2 = im.Scale("images/C2.png", 1920, 1080)
    scene C2
    with Dissolve(1)
    image bg_livingroom_night = im.Scale("images/bg livingroom night.jpg", 1920, 1080)
    scene bg_livingroom_night
    with Dissolve(1)
    jump chapter_2_scene_1

label chapter_2_scene_1:
    "It is night time."
    "[owner_name] has already went to bed after a long day of collecting important supplies."
    "There are a few more things for me to tidy up, before heading to recharge my battery for the night."
    "..."
    "..."
    "..."
    "*{i}knock knock{/i}*"
    "What?!"
    show waifu smiling at left
    p "H-hello?"
    "Why would anyone come at this ungodly hour?"
    p "Is anyone there?"
    "*{i}knock knock{/i}*"
    "I wonder who it could be..."
    "I go to the door, and unlock it slowly."
    show kidnapper smiling at kidnapper_transform, right
    k "I hope you're ready."
    k "*{i}raises EMP gun{/i}*"
    p "Wh-what!"

menu:
    "Fight back":
        jump fight

    "Reason with intruder":
        jump reason

label fight:
    "I decide to fight back."
    p "*[[WEAPONS INITIATED]*"
    p "You better think again about what you're trying to do!"
    k "*{i}fires EMP gun{/i}*"
    p "PKG-42 repeating gun, fire!"
    "It was too late."
    jump shot

label reason:
    "I decide to reason with the intruder."
    p "What are you doing??"
    p "What do you want?!"
    k "*{i}fires EMP gun{/i}*"
    jump shot

label shot:
    show waifu pain at left
    p "AHHHHH!!"
    p "*[[POWER SURGE DETECTED]*"
    p "W-why would you...*{i}crackle{/i}*...do this..."
    p "*[[CRITICAL SYSTEMS DOWN]*"
    p "Stop..."
    p "*[[INITIATING PREVENTIVE SHUTDOWN]*"
    p "No..."
    p "This can't be happening..."
    k "There's nothing you can do now."
    p "Whatever you do...please don't hurt [owner_name]!"
    p "[owner_name], I'm sorry..."
    k "Keep quiet, or there will be more for you to worry about."
    p "You will...*[[TERMINAL SEQUENCE REACHED]*...regret...*[[SYSTEM DOWN]*..."
    "[bot_name] collapses on the living room floor"
    hide waifu
    hide kidnapper
    image bg_black = im.Scale("images/black.jpg", 1920, 1080)
    scene bg_black
    with fade
    jump chapter_2_scene_2

label chapter_2_scene_2:
    "What on earth..."
    "How long has it been?"
    "I open my eyes"
    image bg_factory = im.Scale("images/bg factory.jpg", 1920, 1080)
    scene bg_factory
    "I see the ruins of a large old factory around me"
    "Where am I...?"
    "And most importantly, what happened that night?"

#    "What should I do..."
# TODO: let player select choices
# menu:
#     "Initiate full system check":
#         jump system_check
#     "Explore the area":
#         jump explore
#     "Try to recall what happened":
#         jump recall

    "(I decide to explore this place and see if I can get out of here)."
    "(Is that a figure in the distance?)"

    show angry at right
    gu "Ahh, welcome to the Industrial Extractor Works!"
    gu "I haven't seen you around here before, are you new?"
    show waifu at left
    p "Uhh..."
    gu "Wait a moment..."
    gu "*[[SELECT COUNT(*) FROM employees WHERE name=[bot_name]]*"
    gu "No, you don't belong here."
    gu "Are you an android meant to be condemned?"
    gu "We are in a great shortage of circuit components, after all..."

menu:
    "I'm just wandering around":
        p "I'm just wandering around, don't mind me."
        jump challenge
    "I'm lost":
        p "I'm lost...could you help me?"
        jump challenge

label challenge:
    gu "Heh, I don't think so."
    gu "I am Homura, the security warden for this complex. Everything passes through me and nothing slips by me."
    p "P-please, I don't mean any harm!"
    gu "Well, well... under standard protocol I should terminate you right here and then."
    gu "But it's been a while since we've had visitors, and I am more than a little bit bored... say, shall we play a game?"
    gu "Win, and it'll be as if you never entered this place."
    gu "Lose, and you're scrap metal."
    "I'm good at games... I suppose I could do this."
    "Furthermore, it's probably the best chance I have at entertaining her and getting out of this place unscathed."

menu:
    "I accept your challenge.":
        jump accept
    "Stop wasting my time.":
        p "Stop wasting my time, and let me out of here already!"
        gu "Wow, who do you think you are?"
        gu "You really do not know how to value your own life."
        gu "Have fun, scrap."
        "END"
        return

label accept:
    gu "Very well! You have made a good decision. I would have blasted you to shreds otherwise, heheh."
    gu "As an Ex Machina I expect you to know a thing or two about Linux, the operating system that powers our very core."
    gu "So as you know, you can send Linux processes the standard POSIX signals."
    gu "These signals help to transmit events and allows processes and threads to communicate with one another in a standard way."
    gu "They interrupt a program's normal execution flow and causes its signal handler to take over."

    menu:
        gu "Well now! First question: Which of the following signal cannot be handled or ignored?"

        "SIGINT":
            p "The answer is SIGINT."
            jump q1_wrong
        "SIGCHLD":
            p "The answer is SIGCHLD."
            jump q1_wrong
        "SIGKILL":
            p "The answer is SIGKILL."
            gu "Good! Very good!"
            jump q1_exp
        "SIGALRM":
            p "The answer is SIGALRM."
            jump q1_wrong

label q1_wrong:
    gu "Wrong! The correct answer is SIGKILL"
    jump q1_exp

label q1_exp:
    gu "The two signals that cannot be intercepted and handled are SIGKILL and SIGSTOP."
    gu "SIGKILL, for one, is sent to a process to force it to terminate immediately."

menu:
    gu "Next question: What niceness value for a process among the following indicate most favorable scheduling by the kernel? I will give you a hint: the name \"niceness\" stems from the idea that a process with a higher niceness value is \"nicer\" to other processes in the system."

    "0":
        p "The answer is 0."
        jump q2_wrong
    "19":
        p "The answer is 19."
        jump q2_wrong
    "5":
        p "The answer is 5."
        jump q2_wrong
    "-20":
        p "The answer is -20."
        gu "That's correct!"
        jump q2_exp

label q2_wrong:
    gu "That's wrong!"
    gu "I see you are starting to sweat now, heh!"
    jump q2_exp

label q2_exp:
    gu "When processes are spawned, they are assigned a priority based on their \"nice value\"."
    gu "There are 40 niceness values, with -20 being the one with the highests priority and 19 being the one with the lowest."
    gu "The default niceness value is zero, and a child processes inherits the niceness value of their parents."


menu:
    gu "Last question for you - how do you get out of the Vim editor? If you don't answer this correctly, you're not getting out of here either!"

    ":w":
        p "I would enter :w."
        jump q3_wrong
    ":q":
        p "I would enter :q."
        gu "Heh, glad to know that you are not completely clueless."
        jump q3_exp
    ":e":
        p "I would enter :e."
        jump q3_wrong
    ":$":
        p "I would enter :$"
        jump q3_wrong

label q3_wrong:
    gu "Wrong, wrong, wrong!!!"

label q3_exp:
    gu ":w writes the buffer opened into memory."
    gu ":e allows you to revert a particular buffer which may have been modified by an external program, allowing you to start from the latest copy."
    gu ":$ moves the cursor to the last line in the file."
    gu "So yes, the correct to exit Vim is :q!"

    gu "Well, I guess you did ok."
    gu "You certainly know quite a bt for a Ex Machina [bot_model]."
    gu "You've certainly made my monotonous job here much more interesting as well."
    gu "Well, you may go!"
    p "T-thank you, Homura."
    "With that, Homura led me out of the complex."
    jump chapter_3
