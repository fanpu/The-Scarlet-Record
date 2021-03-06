transform depressed_downsize:
    zoom 0.63
    yoffset 400

label chapter_5:
    image C5 = im.Scale("images/C5.png", 1920, 1080)
    scene C5
    with Dissolve(1)
    image wasteland = im.Scale("wasteland3.jpg", 1920, 1080)
    scene wasteland
    with Dissolve(1)
    play music "music/ch5.flac"
    show depressed default at depressed_downsize, right

    p "(Does she know the building where Shin lives?)"

    p "Hello."

#    image depressed_girl_shock1 = "depressed girl/depressed shock1.png"
    hide depressed default
    show waifu at left
    show depressed shock1 at depressed_downsize, right

    g "Oh, a [bot_model]. Were you abandoned? Thrown away for the latest model?"
    p "No..."

    g "Good for you. Now what do you want from me?"

    hide waifu
    show waifu confused

    "..."
    g "No one just approaches for a friendly chat these days. Go on."

    hide waifu confused
    show waifu at left

    p "...Do you know how to get to the Midtown Tower to from here?"
    g "What for? It's the same everywhere. Same crumbling buildings, same desolate land."
    p "I need to get back to someone."
    g "An android, going back to someone. Who do you have?"

menu:
    "My owner.":
        jump owner5
    "My lover.":
        jump lover5

label owner5:
    hide depressed shock1
    show depressed huh1 at depressed_downsize, right

    g "You androids, always programmed to go back."
    g "Well, at least you have a purpose..."
    g "..."
    g "You know what, I'll help you, if you help me. Something simple. What'd you say to that?"
    p "...I'll help."
    jump Chapter5mid

label lover5:
    hide depressed huh1
    show depressed smile2 at depressed_downsize, right

    g "You androids are so cute! The unconditional love you feel for your owners is just adorable!"
    g "Hah, I haven't laughed in a long time."

    g "I suppose I should help you in return."
    g "Come with me, I have a task for you first."
    p "...Fine."
    jump Chapter5mid

label Chapter5mid:
    image messyroom = im.Scale("messyroom.jpg", 1920, 1080)
    scene messyroom
    with Dissolve(.5)
    #stop music "wasteland.mp3"
    #start music "messyroom.mp3"
    hide depressed smile2
    show depressed default at depressed_downsize, right
    show waifu at left

    g "I have not met another person, or anything moving for a long long time."
    g "It gets lonely sometimes, but I'm used to it"
    p "..."
    g "You androids are smart. Smarter than me, at least."
    g "So you should know how to transfer these files to my computer right?"
    p "Yes."

    image screen start = im.Scale("computerstartscreen.png", 1920, 1080)
    scene screen start
    with Dissolve(.5)
    hide waifu
    hide depressed default

    g "Get to it, then."
    g "..."
    g "..."
    g "I wonder how I lived through the bombs."
    g "Is it my curse to watch the world die around me as I waste away?"
    g "without the courage to just end it all?"

label filetransfer:
    menu:
        "Perform scp transfer":
            jump failcomputer3
        "Find Hard drive name":
            jump successcomputer3

label failcomputer3:
    image computerfail3 = im.Scale("filesfailed.png", 1920, 1080)
    scene computerfail3
    g "...I assume it didn't work."
    p "Yes"
    g "It's okay, I'm used to things not working."
    p "(I really should be more careful, lest I am unable to make it back.)"
    jump filetransfer

    label successcomputer3:
    image computersuccess3 = im.Scale("nameofsystem.png", 1920, 1080)
    scene computersuccess3
    g "It's succeeding?"
    p "Yes."
    jump mount

label mount:
    menu:
        "Mount drive":
            jump successcomputer4
        "Copy files":
            jump failcomputer4

label failcomputer4:
    image computerfail4 = im.Scale("filesfailed.png", 1920, 1080)
    scene computerfail4
    g "No! Is it not working?"
    p "I just did something in the wrong order."
    p "(I better be more careful...)"
    jump mount

label successcomputer4:
     image computersuccess4 = im.Scale("mounted.png", 1920, 1080)
     scene computersuccess4
     g "The hard drive, we can see it now? Am I finally saved?"
     p "Yes."
     image insidefolder = im.Scale("insidefolder.png", 1920, 1080)
     scene insidefolder
     g "What? It's empty? How is it possible?"
     p "Not exactly."

label recovery:
    menu:
        "Initiate file recovery":
            jump successcomputer2
        "Search for hidden files":
            jump failcomputer2

label failcomputer2:
    image computerfail2 = im.Scale("filesfailed.png", 1920, 1080)
    scene computerfail2

    p "No, this must be a mistake."
    g "It better be."
    jump recovery

label successcomputer2:
    image computersuccess2 = im.Scale("filesappeared.png", 1920, 1080)
    scene computersuccess2

    g "..Thank you. I still have a chance."
    p "...Why don't you leave Earth, if you think this place offers nothing?"
    g "You think I don't want to? Interplanetary travel isn't cheap, and I can never afford it even if I live to 80. You actually think anyone would voluntarily stay in this godforsaken land?"
    p "..."
    g "This land is dead. It's inhabitants are withering, abandoned. The population dwindles every year. Soon, there will be nothing left."
    g "We will all return to dust as Earth dies."
    g "..."
    g "What now?"
    p "I need to decrypt the files."
    g "So it will work?"
    p "Almost guaranteed."
    g "...You know how torturous it is, knowing the key to your happiness is locked behind something you cannot access?"
    g "Everyday the hard drive is just there, taunting me with memories of a happier time."
    g "...I would have gone crazy if I never learnt not to care, to surpress my desires and emotions."

label decryption:
    scene screen start

    menu:
        "Decrypt base64":
            jump failcomputer
        "Decrypt MD5":
            jump successcomputer
        "Decrypt SHA-384":
            jump failcomputer

label failcomputer:
    image failedcom = im.Scale("computerfailed.png", 1920, 1080)
    scene failedcom

    g "Is it all lost?"
    p "I must have guessed wrong."
    g "I want to feel truly happy again instead of wallowing in a pit of apathy. I was only ever happy in old Earth."
    p "..."
    g "Please succeed."
    jump retrycomputer

label retrycomputer:
     p "(That took some energy, I better not fail again.)"
     jump decryption

label successcomputer:
     image successcom = im.Scale("computersuccess.png", 1920, 1080)
     scene successcom

     p "It's almost done."
     g "...I don't know what to feel."
     p "Happy? You get to experience your best memories again."
     g "It rings so hollow. Masquerading and pretending the world we live in doesn't exist, escaping into past happier times."
     g "...I always wanted to ask an android, do you ever feel like shutting down...forever?"
     p "No, androids do not have such a function."
     g "...Must be great being an android."
     p "Only humans 'shut down' in such great quantities because of their feelings. Other creatures, they usually want to survive. Why?"
     g "Humans are the only creatures who question life. Ask whether it's worth living."
     menu:
        "Copy files":
            jump successcomputer5

label successcomputer5:
     #stop music "filetransfer.mp3"
     #start music "done.mp3"
     image computersuccess5 = im.Scale("copied.png", 1920, 1080)
     scene computersuccess5
     show depressed relieved1 at depressed_downsize, right
     show waifu at left

     p "It's done."
     g "...Thank you.Thank you kindly."
     g "Ah, my old photos."
     g "They are all I have now. My only way to escape the chasm of apathy I had fallen in."
     g "Have you ever tried so hard to feel something? Feel something real?"
     p "...No."
     g "...Of course, an android will not know."
     g "Do you even know what Earth was like?"
     p "No"
     g "It wasn't perfect, but it was real. It was warm. It was alive."
     g "Nothing like what the world is now."
     p "..."
     g "..."
     g "So...the directions to Midtown Tower, am I right?"
     p "Yes."
     g "Go straight north until you see the giant fountain, you can't miss it. There, turn right. You should reach the building within two days."
     p "Thank you."
     p "...Those photos...will they make your life worth living?"
     g "No. No for long."
     p "What will?"
     g "Something real to care about. Like you, you care about your owner right?"
     p "But..."
     menu:
         "It might not be real.":
             jump real5
         "Nothing.":
             jump nothing5

label real5:
    hide depressed relieved1
    show depressed smile2 at depressed_downsize, right
    show waifu at left

    g "Hah, never knew an android could think of that."
    g "Does it matter if the feelings are real or not?"
    p "..."
    g "At least you do feel care, feel for something real and tangible."
    g "I wish I could do that..."
    jump chapter5ending

label nothing5:
     hide depressed relieved1
     show depressed default at depressed_downsize, right
     show waifu at left

     g "...Hold on to that care."
     g "Don't let it slip away like I did."
     g "It makes all the difference."
     jump chapter5ending

label chapter5ending:
     hide depressed relieved1
     hide waifu
     #stop music "end.mp3"
     #start music "chap5end.mp3"
     scene wasteland
     with Dissolve(.5)

     p "(I would wish her all the best, but I feel that wish will be wasted.)"
     jump chapter_6
