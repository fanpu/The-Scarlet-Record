label chapter_1:
    image bg_house_exterior = im.Scale("images/bg house exterior.png", 1920, 1080)
    scene bg_house_exterior

label scene_start:
    "It was a day just like any other."
    "It is the year 2037, and we live in a world where sentient machines live alongside humans."
    "Well, not exactly alongside - we are still machines, after all."
    "We are designed and programmed to serve the needs of our owners. Whatever it may be"
    "For me, I am a wifebot. I provide companionship and love to the lonely and abandoned."
    jump home

label home:
    image bg_livingroom = im.Scale("images/bg livingroom day.jpg", 1920, 1080)
    scene bg_livingroom
    with dissolve
    show owner smiling at left
    o "[bot_name], I'm back!"
    show owner at right
    p "[owner_name], I've missed you! How was your day?"
    o "As usual. Nothing changes every day, except a little more of the world disappears"
    p "...I won't ever disspear, would I?"
    o "No, you won't. I will not allow that to happen."
    "[owner_name] and I have been close ever since I was created and he booted me up."
    "It was comforting to always have him by my side - he gave my existence purpose and filled my life with joy."
    o "Have you seen the news... precious metal prices are skyrocketing yet again!"
    o "The past few decades of unchecked mining has stripped the Earth to its core..."
    o "Gold, silver, platinum, palladium, rhodium, ruthenium, iridium and osmium - all these precious metals used in complex circuit chips are in severe short supply."
    o "I could only imagine how this would impact the future of our society that is so reliant androids like you."
    p "You don't have to worry about that, you already have me. We'll be together for as long as you live."
    o "You don't understand..."
    o "Things are not as simple as it seems."
    o "It seems like I say this all the time, but I am really worried for you."
    p "W-why? We have been through many hardships. With you at my side, what do I have to be afraid of?"
    o "You are built with the treasures of this Earth - the exact ones that people would do anything to obtain."
    o "I worry for your safety, [bot_name]."
    o "Promise me..."
    o "Promise me you will be safe."

    p "..."
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
    p "Androids never make a promise they can't keep...it goes against our programming."
    jump chapter_1_end

label chapter_1_end:
    "We break our embrace."
    "I hope that our happy days together will continue on forever, just like this...with me and his side. I could not ask for more."
    jump chapter_2
