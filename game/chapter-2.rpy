label chapter_2:
    image bg_livingroom_night = im.Scale("images/bg livingroom night.jpg", 1920, 1080)
    scene bg_livingroom_night
    jump chapter_2_scene_1

label chapter_2_scene_1:
    "It is night time."
    "[owner_name] has already went to bed."
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
    show kidnapper smiling at right
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
    p "Whatever you do...please don't hurt [owner_name]!!"
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
    "What should I do..."
menu:
    "Initiate full system check":
        jump system_check
    ""
