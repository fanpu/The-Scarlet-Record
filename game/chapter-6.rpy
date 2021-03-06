transform man_downsize:
    yoffset 400

label chapter_6:
    image C6 = im.Scale("images/C6.png", 1920, 1080)
    scene C6
    with Dissolve(1)
    image wastelandsquare = im.Scale("wastelandsquare.jpg", 1920, 1080)
    scene wastelandsquare
    with Dissolve(1)

    p "(Where is the fountain?)"
    p "(...did she lie to me?)"
    p "(No, it doesn't make sense. I must be lost.)"
    p "(...what now?)"
    
    image man default = "Spriteset - Male Student 4/MS4-default.png"
    show man default at man_downsize, right
    show waifu at left

    p "!"
    m "What's an android doing out here?"
    p "Do you know how to get to Midtown Tower from here?"
    m "I do...but you androids are good at computer stuff right?"
    p "...Yes."
    m "Just what I was looking for! Can you do me a favour? In exchange for information?"

    menu:
        "No":
            jump no6
        "Fine":
            jump yes6

label no6:
    m "You sure? I am the only sane man in this entire area, you won't get another chance."
    p "(He isn't lying, no sensors are going off.)"
    p "...Fine."
    image man happy = "Spriteset - Male Student 4/MS4-smile7.png"
    show man happy at man_downsize, right
    m "Great. So the company i work for, they didn't pay me nothing. I need you to go there, hack into the servers, and transfer my pay to me."
    jump Chapter6mid
 
label yes6:
    p "Fine, I'll do it. What do you want?"
    image man happy = "Spriteset - Male Student 4/MS4-smile7.png"
    show man happy at man_downsize, right
    m "Great. So the company I work for, they didn't pay me nothin. I need you to go there, hack into the servers, and transfer my pay to me."
    jump Chapter6mid
 
label Chapter6mid:
    p "I can do that."
    m "You better do that or you ain't gonna get nothin."
    m "Hop on my bike and we'll head there."
    p "...Ok"
 
    hide man happy
    image blurredroad = "movingroad.jpg"
    scene blurredroad
    with Dissolve(.5)
    #stop music "wastelandsquare.mp3"
    #play music "motorcyclesounds.mp3"
 
    m "You never answered my first question, android. What are you doing in here of all places?"
    p "I'm lost."
    m "You are lucky you haven't been stripped for parts, android. People here, they are desperate."
    p "Desperate...to leave Earth?"
    m "HOHOHOHO, those are the ones who are truly hopeless and abandoned. Given up all hope, desperate for nothing"
    m "No android, we are desperate to stay. To live a life similar to that before the likes of you existed."
    m "Desperate to be truly human again."

    #stop music "motorcycle.mp3"
    #play music "factory_original.mp3"

    image factory2 = im.Scale("factory.jpg", 1920, 1080)
    scene factory2
    with Dissolve(.5)
    show man default at man_downsize, right
    show waifu at left
 
    m "This factory is the last of its kind. Producing androids like you, but with human labour instead of robots."
    p "But..."
 
    hide man default
    image man angry= "Spriteset - Male Student 4/MS4-angry2.png"
    show man angry at man_downsize, right
 
    m "But what? But it will be less efficient? Make less money? So what? At least humans have a purpose and role again!"
    m "Humans used to do something. Be something. Contribute to our world. Lawmaking, Doctors, Factory workers."
    m "And then YOU came and took it away."
    m "And those slimeballs have the audacity to tell us to kick back and relax, to enjoy your aimless and purposeless lives?"
    p "(He's getting really riled up, should I calm him down?)"
    menu:
        "No":
            jump notcalm
        "Yes":
            jump calm
 
label calm:
    p "Please calm down, or I can't help you."
 
    hide man angry
    show man default at man_downsize, right
 
    m "Help me, huh."
 
    hide man defualt
    show man happy at man_downsize, right
 
    m "I suppose I'm a dirty hypocrite, eh? Asking an adroid for help, just like all those backstabbers?"
    m "Heh."
 
    hide man happy
    show man default at man_downsize, right
 
    m "I guess we just can't help it."
    jump Chapter6mid2
 
label notcalm:
    p "(I better not say anything, or else he will get angrier.)"
    m "And we just watched, and even cheered, as we got slowly replaced."
 
    hide man angry
    show man default at man_downsize, right
 
    m "And even now, after we got bombed to hell by those damn AI, we didn't learn a damn thing."
    p "..."
    jump Chapter6mid2
 
label Chapter6mid2:
    m "...So, you go do your thing. My account number is 144, don't mess it up eh?"

    image computerroom = im.Scale("computerroom.png", 1920, 1080)
    scene computerroom
    with Dissolve(.5)
    #stop music "factory_original.mp3"
    #play music "computerroom.mp3"
 
    m "Here are the computers, connected to the server or whatever they call it."
    m "Don't let me down, now. I need the cash."
    p "..."
 
    image hack = im.Scale("hackscreen.png", 1920, 1080)
    scene hack
    with Dissolve(.5)
 
    p "(Wow, this technology is really old.)"
    p "(They would likely be more vulnearable to oldschool hacking methods)"
 
label findingip:
    menu:
        "host":
            jump successip
        "netcat":
            jump netcatip
        "whois":
            jump whoisip
 
label successip:
    image ip_ok = im.Scale("successip.png", 1920, 1080)
    scene ip_ok
    p "(Wait it's Axiom? Didn't they...make me?)"
    p "(...Maybe...I can find out more about myself)"
    jump findingports
 
label whoisip:
    image ip_fail = im.Scale("whoisip.png", 1920, 1080)
    scene ip_fail
    p "(This is not what I need. I must have forgotten. It was so long ago.)"
    p "(I can't afford to forget all of it.)"
    jump findingip

label netcatip:
    image ip_fail2 = im.Scale("netcatip.png", 1920, 1080)
    scene ip_fail2
    p "(This is not what I need. I must have forgotten. It was so long ago.)"
    p "(I can't afford to forget all of it.)"
    jump findingip
 
label findingports:
    p "(I got the ip address, now I need to find the open ports...)"
    menu:
        "dig":
            jump failport
        "nmap":
            jump successport
        "netcat":
            jump failport

label failport:
    image port_fail = im.Scale("failport.png", 1920, 1080)
    scene port_fail
 
    p "(It's in my memory, how can I forget?)"
    jump findingports

label successport:
    image port_success = im.Scale("portsuccess.png", 1920, 1080)
    scene port_success
 
    p "(Good, now time to prod the server)"

label vulnscan:
    menu:
        "nse --script vuln":
            jump successvuln
        "netcat":
            jump failvuln
        "Hydra":
            jump failvuln

label failvuln:
    scene port_fail
    p "(No, I can't mess up now. I'm too close to fail)"
    jump vulnscan

label successvuln:
    image vuln_success = im.Scale("vulnsuccess.png", 1920, 1080)
    scene vuln_success
    p "(Oh, a common vulnerabiltity. Should be easy)"

label exploit:
    menu: 
        "Upload malicious code":
            jump exploitfail
        "Set up reverse tcp shell":
            jump exploitsuccess
        "Do a DDOS attack":
            jump exploitfail

label exploitfail:
    p "(Wait, this won't get me the information I want.)"
    jump exploit
 
label exploitsuccess:
    image exploit_success = im.Scale("exploitsuccess.png", 1920, 1080)
    scene exploit_success
    p "(Meterpreter shell is set up. Time to obtain root.)"

label kill:
    menu:
        "Kill":
            jump exploit2success
        "Upload rootkit":
            jump exploit2fail
        "rm -rf":
            jump rmrf
 
label exploit2fail:
    image exploit2_fail = im.Scale("killfail.png", 1920, 1080)
    scene exploit2_fail
    p "No, they have barriers set up"
    jump kill
 
label rmrf:
    scene exploit_success
    p "(Are my circuits haywire?)"
    jump kill
 
label exploit2success:
    image exploit2_success = im.Scale("kill.png", 1920, 1080)
    scene exploit2_success
    p "(Protection is disabled.)"

label root:
    menu:
        "Upload rootkit":
            jump rootsuccess
        "hashdump":
            jump rootfail
        "sysinfo":
            jump rootfail

label rootsuccess:
    image root_success = im.Scale("rootsuccess.png", 1920, 1080)
    scene root_success
    p "(Good, I can now access all files without obstruction.)"
    p "(Should I...)"
    menu:
        "Check own source code":
            jump sourcecode
        "Don't do it":
            jump nosourcecode
  
label rootfail:
    p "(This is obviously the wrong command. I know I have the correct one stored somewhere...)"
    jump root

label sourcecode:
    image sourcefolder = im.Scale("sourcefolder.png", 1920, 1080)
    scene sourcefolder
    p "(It's there. I am programmed to feel unconditional love towards my owner.)"
    p "(...)"
    p "(My feelings, they are fake...)"
    p "(...Does Shin know?)"
    p "(...Does Shin care?)"
    p "(....Do I care?)"
    "Hey! Someone is messing with the servers!"
    jump moneytransfer

label nosourcecode:
    scene root_success
    p "(No. My feelings are my feelings. They exist, programmed or not. I do not need to know.)"
    "Hey! Someone is messing with the servers!"
    jump moneytransfer

label moneytransfer: 
    p "(I better fulfil my promise quick.)"
 
    image transfermoney = im.Scale("moneytransfer.png", 1920, 1080)
    scene transfermoney
  
    p "And done."
  
    scene factory2
    with Dissolve(.5)
    #stop music "computerroom.mp3"
    #play music "factorysounds.mp3"
    show man default at man_downsize, right
    show waifu at left
 
    m "...So you succeeded, eh?"
    m "Knew it, you droids do everything better than us."
    m "Midtown Tower is straight South. You should reach within a day, at most two."
    m "...now scram, before I beat you to a pulp."
    p "..."
 
    hide waifu
    hide man default
    scene wastelandsquare
    with Dissolve(.5)
 
    p "(Are humans usually that irrational and contradictory?)"
    p "(No wonder the war even happened.)"
 
    jump chapter_7
