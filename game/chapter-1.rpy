label chapter_1:
    image bg_house_exterior = im.Scale("images/bg house exterior.png", 1920, 1080)
    scene bg_house_exterior

label scene_start:
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
    image bg_livingroom = im.Scale("images/bg livingroom.jpg", 1920, 1080)
    scene bg_livingroom
    with dissolve
    show waifu smiling at left
    p "Shin, I'm back!"
    show owner at right
    o "[bot_name], I've missed you!"
    p "Heheh... sorry for taking so long this time!"
    o "You always make me worry! But I'm more grateful than anything else..."
    p "You make me blush..."
    "Shin and I have been close ever since he was born and I was created."
    "It was comforting to always have him by my side - he gave my existence purpose and filled my life with joy."
    o "Have you seen the news... precious metal prices are skyrocketing yet again!"
    o "The past few decades of unchecked mining has stripped the Earth to its core..."
    o "Gold, silver, platinum, palladium, rhodium, ruthenium, iridium and osmium - all these precious metals used in complex circuit chips are in severe short supply."
    o "I could only imagine how this would impact the future of our society that is so reliant on Ex Machinas."
    p "


python:
    player = renpy.input("What is your name?")
    player = player.strip()

label test:
    p "hello [player]"
    
    p "Why don't you visit {a=https://renpy.org}Ren'Py's home page{/a}?"

    p "Or {a=jump:more_text}here for more info{/a}."
    p "[botname]"
    return

label more_text:

    p "In Hot Springs, Arkansas, there's a statue of Al Capone you can take a picture with."

    p "That's more info, but not the kind you wanted, is it?"

    return


#renpy.input(prompt, default='', allow=None, exclude='{}', length=None, with_none=None, pixel_width=None) link
"And so, we become a visual novel creating duo."
pov "My name is [player]!"
