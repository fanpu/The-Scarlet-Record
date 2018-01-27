define s = Character('Sylvie', color="#c8ffc8")
define m = Character('Me', color="#c8c8ff")

# True if the player has decided to compare a VN to a book.
default book = False
label start:

    scene bg meadow
    with fade
    "After a short while, we reach the meadows just outside the neighborhood where we both live."

    "It's a scenic view I've grown used to. Autumn is especially beautiful here."

    "When we were children, we played in these meadows a lot, so they're full of memories."

    m "Hey... Umm..."

    show sylvie green smile at right
    with dissolve
    
    "She turns to me and smiles. She looks so welcoming that I feel my nervousness melt away."

    "I'll ask her...!"

    m "Ummm... Will you..."

    m "Will you be my artist for a visual novel?"

    show sylvie green surprised

    "Silence."


    s "Sure, but what's a \"visual novel?\""

menu:

    "It's a videogame.":
        jump game

    "It's an interactive book.":
        jump book

label game:

    m "It's a kind of videogame you can play on your computer or a console."

    jump marry

label book:

    $ book = True
    m "It's like an interactive book that you can read on a computer or a console."

    jump marry

