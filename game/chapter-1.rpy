label chapter_1:
    image bg_house_exterior = im.Scale("images/bg house exterior.png", 1920, 1080)
    scene bg_house_exterior

label scene_start:
    "It was a day just like any other."
    "It is the year 2075, and sentient machines called Ex Machina live alongside humans."
    "Well, not exactly alongside - we are still machines, after all."
    "We are designed and programmed to serve the needs of our masters."
    "Every Ex Machina is assigned to a human master from birth, and we stay faithful servants until their death."
    
    # Collect player name
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
