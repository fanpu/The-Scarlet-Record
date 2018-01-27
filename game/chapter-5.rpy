label Chapter5start:

    scene wasteland.jpg
    play music "x.mp3"
    show farawaygirl.gif

    p "(Does she know the building where Shin lives?)

    hide farawaygirl.gif
    show closegirl.gif
    
    p "Hello"    
    g "Oh, a model 3.4. Were you abandoned? Thrown away for the latest model?"
    p "No"
    
    hide closegirl.gif
    show boredgirl.gif

    g "Good for you. Now what do you want from me?"

    "..."
  
    g "No one just approaches for a friendly chat these days. Go on."
    p "...Do you know how to get to the Midtown Tower to from here?"
    g "What for? It's the same everywhere. Same crumbling buildings, same desolate land." 
    p "I need to get back to someone."
    g "An android, going back to someone. Who do you have?"

    menu: 
      "My owner":
        jump 5owner
      "My lover":
	jump 5lover

   label 5owner:
	
        hide boredgirl.gif
	show amusedgirl.gif
        
  g "You androids, always programmed to go back."
	g "Well, at least you have a purpose"
	g "..."
	g "You know what, I'll help you, if you help me. Something simple. What'd you say to that?"
	p "...I'll help."
	jump Chapter5mid

  label 5lover:
	
	hideboredgirl.gif
	show laughinggirl.gif

	g "You androids are so cute! The unconditional love you feel for your owners is just adorable!"

	hide laughinggirl.gif
	show amusedgirl.gif

	g "Hah, I haven't laughed in a long time."   
	g "I suppose I should help you in return."
	g "Come with me, I have a task for you first."
	p "...Fine."
	jump Chapter5mid
 
label Chapter5mid:

       scene messyroom.jpg
       stop music "wasteland.mp3"
       start music "messyroom.mp3"
       hide amusedgirl.gif
       show girl.gif
	
       g "I have not met another person, or anything moving for a long long time"
       g "It gets lonely sometimes"
       g "But I'm used to it"
       p "..."
       g "You androids are smart. Smarter than me, at least."
       
       hide girl.gif
       show girlwithdrive.gif
       
       g "So you should know how to transfer these files to my computer right?"
       p "Yes"
       g "Get to it, then."
       
       stop music "messyroom.mp3"
       start music "filetransfer.mp3"
       hide girlwithdrive.gof
       scene computerscreenstart.jpg
       
       g "I wonder how I lived through the bombs."
       g "Is it my curse to watch the world die around me as I waste away?"
       g "without the courage to just end it all?"
   
   label decryption:
       menu: 
          "Decrypt base64":
	     jump failcomputer
	  "Decrypt MD5":
	     jump successcomputer
	   "Decrypt SHA-384":
	     jump failcomputer
	    
    label failcomputer:
    	
	scene failedcomputer.jpg
	g "Is it all lost?"
	p "I must have guessed wrong."
	g "I want to feel truly happy again instead of wallowing in a pit of apathy. I was only ever happy in old Earth."
	p "..."
	g "Please succeed."
	
	jump retrycomputer
	
    label retrycomputer:
   	scene computerscreenstart.jpg
	p "(That took some energy, I better not fail again)"
	jump decryption
	
   label successcomputer:
        
   	scene successcomputer.jpg
	g "Ah, my old photos."
	g "They are all I have now. My only way to escape the chasm of apathy I had fallen in."
	g "Have you ever tried so hard to feel something? Feel something real?"
	p "...No"
	g "...Of course, an android will not know."
        g "Do you even know what Earth was like?"
	p "No"
	g "It wasn't perfect, but it was real. It was warm. It was alive."
	g "Nothing like what the world is now."
        scene insidefolder.jpg
	g "What? It's empty? How is it possible?"
	p "Not exactly." 
	
label recovery:
	menu: 
	  "Initiate file recovery":
	  	jump successcomputer2
	  "Search for hidden files"
	  	jump failcomputer2
		
   label failcomputer2:
   	
	scene failcomputer2.jpg
	
	p "No, this must be a mistake."
	g "It better be."
	p "(My battery is limited, I cannot risk wasting it on dead ends)"
	jump recovery
	
   label successcomputer2:
   	
	scene successcomputer2.jpg
	
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
	   	jump successcompuer3
    
    label failcomputer3:
    
    	scene failcomputer3.jpg
	
        g "...I assume it didn't work."
	p "Yes"
	g "It's okay, I'm used to things not working."
	p "(I really should be more careful, lest I am unable to make it back)"
	jump filetransfer
	
    label successcomputer3:
    
    	scene computersucces3.jpg
	
	g "What now?"
	p "I need to finish the file transfer."
	g "So it will work?"
	p "Almost garuanteed."
	g "You know how torturous it is, knowing the key to your happiness is locked behind something you cannot access?"
	g "Everyday the hard drive is just there, taunting me with memories of a happier time."
	g "...I would have gone crazy if I never learnt not to care, to surpress my desires and emotions."
	
    label mount:
    	menu:
	   "Mount drive":
	   	jump successcomputer4
	   "Copy files":
	   	jump failcomputer4
  
    label successcomputer4:
    	
	scene successcomputer4.jpg
	
	p "It's almost done."
	g "...I don't know what to feel."
	p "Happy? You get to experience your best memories again."
	g "It rings so hollow. Masquerading and pretending the world we live in doesn't exist, escaping into past happier times."
	g "...I always wanted to ask an android, do you ever feel like shutting down...forever?"
	p "No, androids do not have such a function."
	g "...Must be great being an android."
	p "Only humans 'shut down' in such great quantities because of their feelings. Other creatures, they usually want to survive. Why?"
	g "Humans are the only creatures who question life. Ask whether it's worth living."


	label copy:
	    menu: 
	    	"Copy files":
			




	      
        
       
       
