label chapter_1:
    image bg_black = im.Scale("images/black.jpg", 1920, 1080)
    scene bg_black


label scene_start:
    "*TIME CHECK: 7.39A.M.*"
    "*BOOT UP SEQUENCE INITIATED. COMMENCING IN 3….2….1…*"

    #change to room interior
    image bg_livingroom = im.Scale("images/bg livingroom day.jpg", 1920, 1080)
    scene bg_livingroom
    with fade

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
    o "Ehhhh~ [bot_name], why are you always this serious. Sheesh, I must’ve messed up somewhere when I tried to fix you back when I first found you. I heard that back before the Great War, Ex Machinas were your dream robot that is tailored to the owners wants and needs. They’d be your maid, your wife, your lover, whatever you want them to be!"
    o "Ah well, not that it matters. Your deadpanned responses are cute too~"

    p "*Sighs* It is getting late, Master. We still have a long day ahead of us, shall we pack up and go?"
    jump chapter_2
