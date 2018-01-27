label Chapter5:
 image wasteland = "wasteland3.jpg"
 scene wasteland
 play music "x.mp3"
 image far_girl= "farawaygirl.gif"
 show far_girl
 
 "After walking for a few more days, I came across a girl."
 p "(Does she know the building where Shin lives?)"
 
 image close_girl = "closegirl.gif"
 hide far_girl
 show close_girl

 p "Hello"    
 g "Oh, a model 3.4. Were you abandoned? Thrown away for the latest model?"
 p "No"
 
 hide close_girl
 image bored_girl = "boredgirl.gif"
 show bored_girl

 g "Good for you. Now what do you want from me?"
 "..."
 g "No one just approaches for a friendly chat these days. Go on."
 p "...Do you know how to get to the Midtown Tower to from here?"
 g "What for? It's the same everywhere. Same crumbling buildings, same desolate land." 
 p "I need to get back to someone."
 g "An android, going back to someone. Who do you have?"
menu: 
 "My owner":
   jump owner5 
 "My lover":
   jump lover5

label owner5:
 hide bored_girl
 image amused_girl = "amusedgirl.gif"
 show amused_girl

 g "You androids, always programmed to go back."
 g "Well, at least you have a purpose"
 g "..."
 g "You know what, I'll help you, if you help me. Something simple. What'd you say to that?"
 p "...I'll help."
 jump Chapter5mid
  
label lover5:
 image laugh_girl = "laughinggirl.gif"
 hide bored_girl
 show laugh_girl
 
 g "You androids are so cute! The unconditional love you feel for your owners is just adorable!"
 g "Hah, I haven't laughed in a long time."
 
 hide laugh_girl
 show amused_girl
 
 g "I suppose I should help you in return."
 g "Come with me, I have a task for you first."
 p "...Fine."
 jump Chapter5mid
 
label Chapter5mid:
 image messyroom = "messyroom.jpg"
 scene messyroom
 stop music "wasteland.mp3"
 start music "messyroom.mp3"
 hide amused_girl
 image girl = "girl.gif"
 show girl
 
 g "I have not met another person, or anything moving for a long long time"
 g "It gets lonely sometimes"
 g "But I'm used to it"
 p "..."
 g "You androids are smart. Smarter than me, at least."
 
 hide girl
 
 g "So you should know how to transfer these files to my computer right?"
 p "Yes"
 
 image screenstart = "computerscreenstart.jpg"
 scene screenstart
 
 g "Get to it, then."
 g "..."
 g "I wonder how I lived through the bombs."
 g "Is it my curse to watch the world die around me as I waste away?"
 g "without the courage to just end it all?"
   
label decryption:
 scene screenstart
 
 menu: 
  "Decrypt base64":
   jump failcomputer
  "Decrypt MD5":
   jump successcomputer
  "Decrypt SHA-384":
   jump failcomputer
   
label failcomputer: 
 image failedcom = "failedcomputer.jpg"
 scene failedcom
 
 g "Is it all lost?"
 p "I must have guessed wrong."
 g "I want to feel truly happy again instead of wallowing in a pit of apathy. I was only ever happy in old Earth."
 p "..."
 g "Please succeed."
 jump retrycomputer
 
label retrycomputer:
 p "(That took some energy, I better not fail again)"
 jump decryption

label successcomputer:
 image successcom = "successcomputer.jpg"
 scene successcom
 
 g "Ah, my old photos."
 g "They are all I have now. My only way to escape the chasm of apathy I had fallen in."
 g "Have you ever tried so hard to feel something? Feel something real?"
 p "...No"
 g "...Of course, an android will not know."
 g "Do you even know what Earth was like?"
 p "No"
 g "It wasn't perfect, but it was real. It was warm. It was alive."
 g "Nothing like what the world is now."
 
 image insidefolder = "insidefolder.jpg"
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
 
 image computerfail2 = "computerfail2.jpg"
 scene computerfail2
 
 p "No, this must be a mistake."
 g "It better be."
 p "(My battery is limited, I cannot risk wasting it on dead ends)"
 jump recovery
 
label successcomputer2:
 image computersuccess2 = "computersuccess2.jpg"
 scene computersuccess2
 
 g "..Thank you. I still have a chance."
 p "...Why don't you leave Earth, if you think this place offers nothing?"
 g "You think I don't want to? Interplanetary travel isn't cheap, and I can never afford it even if I live to 80. You actually think anyone would voluntarily stay in this godforsaken land?"
 p "..."
 g "This land is dead. It's inhabitants are withering, abandoned. The population dwindles every year. Soon, there will be nothing left."
 g "We will all return to dust as Earth dies."
 
label filetransfer:
 menu:
  "Perform scp transfer":
   jump failcomputer3
  "Find Hard drive name":
   jump successcomputer3
    
label failcomputer3:
 image computerfail3 = "computerfail3.jpg"
 scene computerfail3
 g "...I assume it didn't work."
 p "Yes"
 g "It's okay, I'm used to things not working."
 p "(I really should be more careful, lest I am unable to make it back)"
 jump filetransfer
 
label successcomputer3:
 image computersuccess3 = "computersuccess3.jpg"
 scene successcomputer3
 g "What now?"
 p "I need to finish the file transfer."
 g "So it will work?"
 p "Almost garuanteed."
 g "...You know how torturous it is, knowing the key to your happiness is locked behind something you cannot access?"
 g "Everyday the hard drive is just there, taunting me with memories of a happier time."
 g "...I would have gone crazy if I never learnt not to care, to surpress my desires and emotions."

label mount:
 menu:
  "Mount drive":
   jump successcomputer4
  "Copy files":
   jump failcomputer4
   
label failcomputer4:
 image computerfail4 = "computerfail4.jpg"
 scene computerfail4
 g "No! Is it not working?"
 p "I'm trying. It should succeed the next time."
 p "(I better be more careful...)"
 jump mount
 
label successcomputer4:
 image computersuccess4 = "computersuccess4.jpg"
 scene computersuccess4
 
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
 stop music "filetransfer.mp3"
 start music "done.mp3"
 image computersuccess5 = "computersuccess5.jpg"
 scene computersuccess5
 image girl_relieved = "relievedgirl.gif"
 show girl_relieved

 p "It's done."
 g "...Thank you.Thank you kindly."
 g "So...the directions to Midtown Tower, am I right?"
 p "Yes."
 g "Go straight north until you see the giant fountain, you can't miss it. There, turn right. You should reach the building within two days."
 p "Thank you"
 p "...Those photos...will they make your life worth living?"
 g "No. No for long."
 p "What will?"
 g "Something real to care about. Like you, you care about your owner right?"
 p "But..."
 menu:
  "It might not be real":
   jump real5
  "Nothing.":
   jump nothing5
   
label real5:
 hide girl_relieved 
 show girl_amused
 
 g "Hah, never knew an android could think of that."
 g "Does it matter if the feelings are real or not?"
 p "..."
 g "At least you do feel care, feel for something real and tangible."
 g "I wish I could do that"
 jump chapter5ending
 
label nothing5:
 hide girl_relieved
 show girl
 
 g "...Hold on to that care."
 g "Don't let it slip away like I did."
 g "It makes all the difference."
 jump chapter5ending
 
label chapter5ending:
 hide girl_relieved
 stop music "end.mp3"
 start music "chap5end.mp3"
 scene wasteland
 
 p "(I would wish her all the best, but I feel that wish will be wasted)"
                 
    
return
 


	      
        
       
       
