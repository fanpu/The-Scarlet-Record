transform owner_transform:
    zoom 1.5

label chapter_1:
    image C1 = im.Scale("images/C1.png", 1920, 1080)
    scene C1
    with Dissolve(1)
    image bg_black = im.Scale("images/black.jpg", 1920, 1080)
    scene bg_black
    with Dissolve(1)
    play music "music/ch1.flac"

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
    "Straight ahead, a shattered glass window showed the view of a bombed-out city, and beyond that, a bright shining sun rising above grimy dessert horizon"
    p "(And Owner is nowhere to be found.)"
    p "(He should be back home, soon, I hope.)"
    p "(It's not the safest area, but I have faith in his abilities.)"

    "*DOOR OPENS*"
    show owner at owner_transform, right

    show owner neutral at owner_transform, right
    image waifu happy = "waifu happy.png"
    show waifu happy
    p "You're back!"
    o "Gathering supplies outside was hell, as usual."
    show waifu sad
    o "Oh come on, it isn't that bad. I'm fine here, you see?"
    hide waifu
    show waifu at left
    p "You always worry me so much..."
    hide owner
    show owner serious at owner_transform, right

    o "Don't. I'll be fine. I'm more than able to take care of myself."
    o "So don't worry, ok?"
    p "..."
    p "...I can't not worry about you, [owner_name]"
    o "...Let's watch the sunset together, [bot_name]."

    image wastelandsunset = im.Scale("wastelandsunset.jpg", 1920, 1080)
    scene wastelandsunset
    o "..."
    p "..."
    o "Do you know the sunset used to be more orange than red?"
    o "After the war, the air changed."
    p "...It's still beautiful."
    o "Yes."
    "..."
    stop music
    o "Can you promise me to stay safe?"
    hide waifu
    image waifu confused = "waifu confused.png"
    show waifu confused
    p "W-why? Do you not trust me?"
    hide owner
    show owner happy at owner_transform, right
    o "No no, nothing like that. Just that...this Earth isn't friendly to anything, not even something as sweet as you."
    hide waifu
    show waifu at left
    p "With you at my side, I'm not afraid of anything. You don't have to worry, [owner_name]."
    o "Haha, you always know the right thing to say."
    hide owner
    show owner neutral at owner_transform, right
    o "Alright, just promise me."
    hide owner
    show owner sad at owner_transform, right
    o "Please."
    menu:
     "I promise":
          jump promise
     "I can't":
          jump nopromise

label promise:
    show waifu happy
    p "Alright, I promise!"
    show owner happy at owner_transform, right
    o "Thank you! You don't know how much it means to me."
    p "With you, what do I have to worry about?"
    jump chapter_2

label nopromise:
    show waifu sad at left
    p "I'm sorry, I can't. Androids, we don't take promises lightly."
    show owner sad at owner_transform, right
    o "...I understand."
    jump chapter_2
