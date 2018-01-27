label Chapter 6:
 scene wastelandsqaure.jpg
 stop music "chapter5end.mp3"
 start music "nofountain.mp3"
 
 p "(Where is the fountain?)"
 p "(...did she lie to me?)"
 p "(No, it doesn't make sense. I must be lost.)"
 p "(...what now?)"
 
 show manonbicycle.jpg
 
 p "!"
 
 hide manonbicycle.jpg
 show manonbicycleclose.jpg
 
 m "What's an android doing out here?"
 p "Do you know how to get to Midtown Tower from here?"
 
 hide manonbicycleclose.jpg
 show thinkingman.jpg
 
 m "I do...but you androids are good at computer stuff right?"
 p "...Yes."
 
 hide thinkingman.jpg
 show happyman.jpg
 
 m "Just what I was looking for! Can you do me a favour? In exchange for information?"
 
 menu:
  "No":
   jump no6
  "Fine":
   jump yes6

label no6:
 hide happyman.jpg
 show raisedeyebrowman.jpg
 
 m "You sure? I am the only sane man in this entire area, you won't get another chance."
 p "(He isn't lying, no sensors are going off.)"
 p "...Fine."
 
 hide raisedeyebrowman.jpg
 show happyman.jpg
 
 m "Great. So the company i work for, they didn't pay me nothing. I need you to go there, hack into the servers, and transfer my pay to me."
 jump Chapter6mid
 
label yes6:
 p "Fine, I'll do it. What do you want?"
 m "Great. So the company I work for, they didn't pay me nothin. I need you to go there, hack into the servers, and transfer my pay to me."
 jump Chapter6mid
 
label Chapter6mid:
 p "I can do that."
 
 hide happyamn.jpg
 show seriousman.jpg
 
 m "You better do that or you ain't gonna get nothin."
 m "Hop on my bike and we'll head there."
 p "...Ok"
 
 hide seriousman.jpg
 scene blurredroad.jpg
 stop music "wastelandsqaure.mp3"
 play music "motorcyclesounds.mp3"
 
 m "You never answered my first question, android. What are you doing in here of all places?"
 p "I'm lost."
 m "You are lucky you haven't been stripped for parts, android. People here, they are desperate."
 p "Desperate...to leave Earth?"
 m "HOHOHOHO, those are the ones who are truly hopeless and abandoned. Given up all hope, desperate for nothing"
 m "No android, we are desperate to stay. To live a life similar to that before the likes of you existed."
 m "Desperate to be truly human again."
 
 stop music "motorcyclesounds.mp3"
 play music "factorysounds.mp3"

 scene factory.jpg
 show man.jpg
 
 m "This factory is the last of its kind. Producing androids like you, but with human labour instead of robots."
 p "But..."
 
 hide man.jpg
 show manangry.jpg
 
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
 
 hide manangry.jpg
 show man.jpg
 
 m "Help me, huh."
 
 hide man.jpg
 show mansmile.jpg
 
 m "I suppose I'm a dirty hypocrite, eh? Asking an adroid for help, just like all those backstabbers?"
 m "Heh."
 
 hide mansmile.jpg
 show sadman.jpg
 
 m "I guess we just can't help it."
 jump Chapter6mid2
 
label notcalm:
 p "(I better not say anything, or else he will get angrier.)"
 m "And we just watched, and even cheered, as we got slowly replaced."
 
 hide angryman.jpg
 show sadman.jpg
 
 m "And even now, after we got bombed to hell by those damn AI, we didn't learn a damn thing."
 p "..."
 jump Chapter6mid2
 
label Chapter6mid2:
 m "...So, you go do your thing."

 scene computerroom.jpg
 stop music "factorysounds.mp3"
 start music "computerroom.mp3"
 
 m "Here are the computers, connected to the server or whatever they call it."
 m "Don't let me down, now. I need the cash."
 p "..."
 
 scene hackscreen.jpg
 
 p "(Wow, this technology is really old.)"
 p "(They would likely be more vulnearable to oldschool hacking methods)"
 
label findingip:
 menu:
  "whois":
   jump successip
  "nmap":
   jump failip
  "dig":
   jump failip
 
label successip:
 scene successip.jpg
 
 p "(Axiom? Didn't they...make me?)"
 p "(...Maybe...I can find out more about myself)"
 jump findingports
 
label failip:
 scene failip.jpg
 p "(I must have forgotten. It was so long ago.)"
 p "(I can't afford to forget all of it.)"
 jump findingip
 
label findingports:
 p "(I got the ip address, now I need to find the open ports...)"
 menu:
  "dig":
   jump failport
  "nmap"
   jump successport
  "netcat"
   jump failport

label failport:
 scene failport.jpg
 
 p "(It's in my memory, how can I forget?)"
 jump findingports

label successport:
 scene successport.jpg
 
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
 scene failvuln.jpg
 p "(No, I can't mess up now. I'm too close to fail)"
 jump vulnscan

label successvuln:
 scene successvuln.jpg
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
 scene exploitfail.jpg
 p "(No, this won't get me the information I want.)"
 jump exploit
 
label exploitsuccess:
 scene exploitsuccess.jpg
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
 scene exploit2fail.jpg
 p "No, they have barriers set up"
 jump kill
 
label rmrf:
 scene exploitsuccess.jpg
 p "(Are my circuits haywire?)"
 jump kill
 
label exploit2success:
 scene exploit2success.jpg
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
 scene rootsuccess.jpg
 p "(Good, I can now access all files without obstruction.)"
 p "(Should I...)"
 menu:
  "Check own source code":
   jump sourcecode
  "Don't do it":
   jump nosourcecode
  
label rootfail:
 scene rootfail.jpg
 p "(I know I have this stored somewhere...)"
 jump root

label sourcecode:
 scene sourcecode.jpg
 p "(It's there. I am programmed to feel unconditional love towards my owner.)"
 p "(...)"
 p "(My feelings, they are fake...)"
 p "(...Does Shin know?)"
 p "(...Does Shin care?)"
 p "(....Do I care?)"
 "Hey! Someone is messing with the servers!"
 jump moneytransfer

label nosourcecode:
 scene rootsuccess.jpg
 p "(No. My feelings are my feelings. They exist, programmed or not. I do not need to know.)"
 "Hey! Someone is messing with the servers!"
 jump moneytransfer

label moneytransfer: 
 p "(I better fulfil my promise quick.)"
  
 scene moneytransfer.jpg
  
 p "And done."
  
 scene factory.jpg
 stop music "computerroom.mp3"
 start music "factorysounds.mp3"
 show man.jpg
  
 m "...So you succeeded, eh?"
 m "Knew it, you droids do everything better than us."
 m "Midtown Tower is straight South. You should reach within a day, at most two."
 m "...now scram, before I beat you to a pulp."
 p "..."
 
 
 
 
  
 
