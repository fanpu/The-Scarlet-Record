label chapter_1:
    image bg_black = im.Scale("images/black.jpg", 1920, 1080)
    scene bg_black


label scene_start:
    "*TIME CHECK: 7.39A.M.*"
    "*BOOT UP SEQUENCE INITIATED. COMMENCING IN 3….2….1…*"

    #change to room interior
    image bg_house_exterior = im.Scale("images/bg house exterior.png", 1920, 1080)
    scene bg_house_exterior
    with zoomout

    "Light floods my vision. As standard protocol dictates, I look around myself to ascertain my positon."
    "To my right, stood a dust-covered bookshelf; yellowed volumes, cobwebs and spiders covered its surfaces."
    "Next to that was an equally dilapidated worktable, with various damaged writing instruments scattered across the table face."
    "Straight ahead, a shattered glass window showed the view of a bombed-out city, and beyond that, a bright shining sun rising above grimy dessert horizon."
    "A dilapidated room in a dilapidated city, in a dilapidated world."
    "*SNOOOOOOOOOOOORE*"
    "Finally, on my left, Master lay fast asleep on a bamboo mat. Time to rouse him, as he instructed."

    p "Master, master, it’s time to wake up."
    "As I continued my attempts to awaken Master, his peaceful expressions slowly morphed into an annoyed one."
    o "Mgnnnn……mgnya!"
    "Suddenly, Master broke free from is seemingly everlasting slumber, and groggily sat up. As he  looked around groggily, his gaze fell upon me. A wide smile spread across his face."

    o "Ah, good morning, Darling."
    p "Good morning to you too, Master. Also, I have a name, it’s [bot_name]. not \"Darling\". Such relationships are impossible, you are a Human, I am an Ex Machina. I am a mass produced machine created to serve you, my Master. You falling for me is equivalent to the weaboos of centuries past, going on and on with their imaginary \"waifus\". It is unsightly, please be careful not to do this again."
    "I was nonplussed."
    o "Ehhhh~ [bot_name], why are you always this serious. Sheesh, I must’ve messed up somewhere when I tried to fix you back when I first found you. I heard that back before the Great War, Ex Machinas were your dream robot that is tailored to the owners wants and needs. They’d be your maid, your wife, your lover, whatever you want them to be!"
    o "Ah well, not that it matters. Your deadpanned responses are cute too~"

    p "*Sighs* It is getting late, Master. We still have a long day ahead of us, shall we pack up and go?"


    "It was a day just like any other."
    "It is the year 2037, and we live in a world where sentient machines called Ex Machina live alongside humans."
    "Well, not exactly alongside - we are still machines, after all."
    "We are designed and programmed to serve the needs of our masters."
    "Every Ex Machina is assigned to a human master from birth, and we stay faithful servants until their death."
    "I was out running errands for my master, Takagi Shinichirou."
    "Doing the usual things - buying groceries, settling bills, and buying household items."
    "Now that all those are done, I'm finally back home!"
    jump home

label home:
    image bg_livingroom = im.Scale("images/bg livingroom day.jpg", 1920, 1080)
    scene bg_livingroom
    with dissolve
    show waifu smiling at left
    p "[owner_name], I'm back!"
    show owner at right
    o "[bot_name], I've missed you!"
    p "Heheh... sorry for taking so long this time!"
    o "You always make me worry! But I'm more grateful than anything else..."
    p "You make me blush..."
    "[owner_name] and I have been close ever since he was born and I was created."
    "It was comforting to always have him by my side - he gave my existence purpose and filled my life with joy."
    o "Have you seen the news... precious metal prices are skyrocketing yet again!"
    o "The past few decades of unchecked mining has stripped the Earth to its core..."
    o "Gold, silver, platinum, palladium, rhodium, ruthenium, iridium and osmium - all these precious metals used in complex circuit chips are in severe short supply."
    o "I could only imagine how this would impact the future of our society that is so reliant on Ex Machinas."
    p "It will be ok - as long as we have each other, things will be fine."
    p "We have already been through so many hardships together."
    o "You don't understand..."
    o "Things are not as simple as it seems."
    o "It seems like I say this all the time, but I am really worried for you."
    p "W-why?"
    o "You are built with the treasures of this Earth - the exact ones that people would do anything to obtain."
    o "I worry for your safety, [bot_name]."
    o "Promise me..."
    o "Promise me you will be safe."

    p "[owner_name]..."
    "I notice a teardrop roll down [owner_name]'s cheeks"
    p "[owner_name]..."
    "[owner_name] steps forward and embraces me."
menu:
    "I promise.":
        jump promise

    "I...I don't know.":
        jump dont_know

label promise:
    p "I...I promise, [owner_name]."
    o "Thank you, [bot_name]."
    o "You don't know how much this means to me."
    jump chapter_1_end

label dont_know:
    p "I...I don't know, [owner_name]."
    o "I understand."
    p "Ex Machinas never make a promise they can't keep...it's just how we are engineered."
    jump chapter_1_end

label chapter_1_end:
    "We break our embrace."
    "I hope that our happy days together will continue on forever, just like this..."
    jump chapter_2
