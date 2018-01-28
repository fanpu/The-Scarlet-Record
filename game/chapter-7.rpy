image bg = im.Scale("ch7.jpg", 1280, 720)

image p angry = "waifu angry.png"
image p confused = "waifu confused.png"
image p sadbuthappy = "waifu crying but happy.png"
image p exhausted = "waifu exhausted.png"
image p happy = "waifu happy.png"
image p neutral = "waifu neutral.png"
image p relieved = "waifu relieved.png"
image p sad = "waifu sad.png"
image p thinking = "waifu thinking.png"
image p verysad = "waifu very sad.png"

label start:
    scene bg
    play music "music/ch7.flac"

    show p neutral
    p "It's been really long since I went missing..."
    p "The last time I went out on my own without informing <insert owner name>, he was worried sick..."
    p "And that was less than a day..."
    p "Now it's been a week..."
    p "..."
    p "..."
    
    show p thinking
    p "I don't even want to imagine how distressed he is right now..."
    p "..."
    p "..."

    show p exhausted
    p "I’m so tired... I’ve been having a lot of trouble to sleep for the past few days."
    p "I’m worried that if I sleep, I’ll be wasting precious time which I can spend with you, and maybe I can find you more quickly."
    p "..."
    p "..."
    
    stop music
    p "I’m worried that if I don’t sleep, I’ll collapse from exhaustion and lose all my memory, and I wouldn’t be able to find you ever again."
   
    show p sad
    play sound "music/sobbing.mp3"
    p "No, I have to be strong, right? I definitely can find you, right?"
    stop sound
    
    play music "music/ch7repeat.mp3"
    p "Ok, <insert bot name>, calm down... You have to be brave, be strong, and find your way back..."
    p "I’ve read up what other humans have to say about feelings."
    p "They say pain diminishes with time – eventually people will learn to forget their past and focus on the present."
    stop music
    
    play music "music/sobbing.mp3"
    p "I don’t understand how humans can possibly do that... I don’t want to forget you..."
    p "How can humans be so cruel to cope with sadness by forgetting it?"
    stop music

    p "Oh no! Please don’t forget me, <insert owner name>!! Don’t listen to what the \"specialists\" have to say about human feelings. Please..."
    p "I want to find you as fast as possible. Hopefully this is the right way back – if it isn’t –"
    
    play sound "music/crying.mp3"
    show p verysad
    p "<insert owner name>, I miss you..."
    p "I need a shoulder to lean on, a shirt to cry on, a way to help me carry on..."
    p "I’m already on the verge of giving up..."
    
    p "Wherever you are, I hope you can hear me. I really miss you..."
    p "I miss the having trouble sleeping every night because I look forward to spending another day with you..."
    p "I miss the occasional adventures that we have at midnight..."
    p "I miss the frequency of you – I always see you around all the time, but I haven’t seen you for the past few days..."
    p "I miss the way you embrace me when we sleep at night – those warm hands, your comfy chest..."
    p "I miss the way you snore – it has a nice, comfortable rhythm to it that helps me to sleep..."
    p "I miss your handsome smile - I'll do anything to see it again..."
    stop sound

    play sound "music/running.mp3"
    p "Every second without you feels like an eternity."

    show p sadbuthappy
    p "You aren't just the other half that completes me. You're simply everything to me..."
