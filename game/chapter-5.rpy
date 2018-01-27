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

   label 5owner
	
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
 
Label Chapter5mid

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
       
       hide girlwithdrive.gof
       scene computerscreenstart.jpg
       
       g "I wonder how I lived through the bombs."
       g "Is it my curse to watch the world die around me as I waste away?"
       g "without the courage to just end it all?"
       
       menu: 
          "
        
       
       
