label chapter_1:
    "Hello!"
    # Collect player name
label test:

    p "Why don't you visit {a=https://renpy.org}Ren'Py's home page{/a}?"

    p "Or {a=jump:more_text}here for more info{/a}."

    return

label more_text:

    p "In Hot Springs, Arkansas, there's a statue of Al Capone you can take a picture with."

    p "That's more info, but not the kind you wanted, is it?"

    return

python:
    povname = renpy.input("What is your name?")
    povname = povname.strip()
#renpy.input(prompt, default='', allow=None, exclude='{}', length=None, with_none=None, pixel_width=None) link
"And so, we become a visual novel creating duo."
pov "My name is [povname]!"
