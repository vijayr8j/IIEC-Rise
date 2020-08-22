import os
import pyttsx3
import random
import datetime
from datetime import datetime as dt
import pytz
import math
#intro
timezone=datetime.datetime.now(datetime.timezone(datetime.timedelta(0))).astimezone().tzinfo
dtime=dt.now(timezone)
time= int(dtime.strftime("%H"))
starting_time=int(dtime.strftime("%M"))
starting_time0=int(dtime.strftime("%S"))
if(time>0)and(time<8):
	wishes="Very Good Morning! Let us start fresh"
elif(time>=8)and(time<12):
	wishes="Good Morning"
elif(time>=12)and(time<16):
	wishes="Good Afternoon"
else:
	wishes="Good Evening"

#function for end conversation
def end_conv():
	greetings=["see you next time!", "waiting... to see you again!", "all is well!", "let your dreams come true!","See you soon!"]
	choice=random.randrange(0,5)
	timezone=datetime.datetime.now(datetime.timezone(datetime.timedelta(0))).astimezone().tzinfo
	dtime=dt.now(timezone)
	time= int(dtime.strftime("%H"))
	

	timezone=datetime.datetime.now(datetime.timezone(datetime.timedelta(0))).astimezone().tzinfo
	dtime=dt.now(timezone)
	time= int(dtime.strftime("%H"))
	starting_time1=int(dtime.strftime("%M"))
	starting_time01=int(dtime.strftime("%S"))
	if((starting_time1-starting_time)==0):
		diff=starting_time01-starting_time0
		diff=abs(diff)
		print("we are getting close, my friend! you have spend "+str(diff)+" seconds with me.")
		pyttsx3.speak("we are getting close, my friend! you have spend "+str(diff)+"  seconds with me.")
	else:
		diff=starting_time1-starting_time
		diff=abs(diff)
		print("we are getting close, my friend! you have spend "+str(diff)+" minutes with me.")
		pyttsx3.speak("we are getting close, my friend! you spend "+str(diff)+" minutes with me.")
	print("bye "+name+ "!")
	pyttsx3.speak("bye "+name+ "!")

	print(greetings[choice])
	pyttsx3.speak(greetings[choice])


	if(time>=8) and (time<=11):
		print("Have you had your breafast "+name+"? if not, take it "+name+".")
		pyttsx3.speak("Have you had your breafast "+name+"? if not, take it "+name+".")
	elif(time>=12) and (time<=15):
		print("Have you had your lunch "+name+"? if not, take it "+name+".")
		pyttsx3.speak("Have you had your lunch "+name+"? if not, take it "+name+".")
	elif(time>=17) and (time<19):
		print("Hurray! crack your snacks "+name+"!")
		pyttsx3.speak("Hurray! crack your snacks "+name+"!")
	elif(time>=20) and (time<=22):
		print("Have you had your dinner "+name+"? if not take it "+name+".")
		pyttsx3.speak("Have you had your dinner "+name+"? if not take it "+name+".")
	elif time>=22:
		print("Good night! "+name+", It is getting late.. have a sleep "+name+".")
		pyttsx3.speak("Good night! "+name+", It is getting late.. have a sleep "+name+".")
	else:
		pass	
def choose_pgm(pgm):
	if (((("open" in pgm)or("run" in pgm)or("start" in pgm)or("execute" in pgm)or("" in pgm)))and("browser" in pgm))and(("chrome" not in pgm)and("mozilla" not in pgm)and("firefox" not in pgm)and("internet" not in pgm)and("explorer" not in pgm)and("edge" not in pgm)and("ie" not in pgm)):
		print("wait a minute, I can find many browser installed in your system...")
		pyttsx3.speak("wait a minute... I can find many browser installed in your system...")
		print("which browser, do you want to open?",end="  ")
		pyttsx3.speak("which browser, do you want to open?")
		multi_browser=input()
		if("nope" in multi_browser)or("no" in multi_browser)or("end" in multi_browser)or("exit" in multi_browser)or("close" in multi_browser)or("cancel" in multi_browser):
			print("hey! "+name+", please answer me!")
			pyttsx3.speak("hey! "+name+", please answer me!")
		else:
			choose_pgm(multi_browser)
	elif (("open" in pgm)or("run" in pgm)or("start" in pgm)or("" in pgm)or("execute" in pgm)or("launch" in pgm))and(("chrome" in pgm)or("google" in pgm)):
		os.system("chrome")
		print("Don't feel alone, you have 1 billion mates using chrome! chrome is really a browsing rocket!!")
		pyttsx3.speak("Don't feel alone, you have 1 billion mates using chrome! chrome is really a browsing rocket!!")
	elif (("open" in pgm)or("run" in pgm)or("start" in pgm)or("" in pgm)or("execute" in pgm)or("launch" in pgm))and(("firefox" in pgm)or("mozilla" in pgm)):
		os.system("firefox")
		print("hey! developer, you are using one of the best open source browser...")
		pyttsx3.speak("hey! developer, you are using one of the best open source browser...")
	elif (("open" in pgm)or("run" in pgm)or("start" in pgm)or("" in pgm)or("execute" in pgm)or("launch" in pgm))and(("internet" in pgm)or("explorer" in pgm)or("explore" in pgm)or("ie" in pgm)):
		os.system("iexplore")
		print("I think you are fan of tortoise! but it wins the race...")
		pyttsx3.speak("I think you are fan of tortoise! but it wins the race...")
	elif (("open" in pgm)or("run" in pgm)or("start" in pgm)or("" in pgm)or("execute" in pgm)or("launch" in pgm))and("edge" in pgm):
		os.system("msedge")
		print("you are cool! you are updated!")
		pyttsx3.speak("you are cool! you are updated!")
	elif (("open" in pgm)or("run" in pgm)or("start" in pgm)or("execute" in pgm)or("" in pgm)or("launch" in pgm))and(("Text editor" in pgm)or("notepad" in pgm)):
		os.system("notepad")
		print("hey! creator, script here, whatever you want to create...")
		pyttsx3.speak("hey! creator, script here, whatever you want to create...")
	elif (("open" in pgm)or("run" in pgm)or("start" in pgm)or("execute" in pgm)or("" in pgm)or("launch" in pgm))and(("python" in pgm)or("py" in pgm)or("interpreter" in pgm)):
		os.system("python")
		print("I was also developed with python...")
		pyttsx3.speak("I was also developed with python...")
	elif (("open" in pgm)or("run" in pgm)or("start" in pgm)or("execute" in pgm)or("" in pgm)or("launch" in pgm))and(("eclipse" in pgm)or("IDE" in pgm)or("interpreter" in pgm)):
		os.system("eclipse")
		print("OOPs, good to be a java developer...")
		pyttsx3.speak("oops, good to be a java developer...")
	elif (("open" in pgm)or("run" in pgm)or("start" in pgm)or("execute" in pgm)or("" in pgm)or("launch" in pgm))and(("tableau" in pgm)or("data" in pgm)or("visualization" in pgm)or("visualize" in pgm)):
		os.system("tableau")
		print("visualize your data...")
		pyttsx3.speak("visualize your data...")
	elif (("open" in pgm)or("run" in pgm)or("start" in pgm)or("execute" in pgm)or("" in pgm)or("launch" in pgm))and(("calculation" in pgm)or("calculator" in pgm)):
		os.system("calc")
		print("All technology evloved from invention of calculator...")
		pyttsx3.speak("All technology evloved from invention of calculator...")
	elif (("open" in pgm)or("run" in pgm)or("start" in pgm)or("execute" in pgm)or("" in pgm)or("launch" in pgm))and(("bandicam" in pgm)or("screen recorder" in pgm)):
		os.system("bdcam")
		print("record important speech/video with bandicam...")
		pyttsx3.speak("record important speech/video with bandicam...")
	elif ((("open" in pgm)or("run" in pgm)or("start" in pgm)or("execute" in pgm)or("" in pgm))and(("player" in pgm)or("audio" in pgm)or("video" in pgm)))and(("vlc" not in pgm)and("windows" not in pgm)and("media" not in pgm)): 
		print("hurray! I can find more than one player installed in your system...")
		pyttsx3.speak("hurray! I can find more than one player installed in your system...")
		print("which player, do you want to open?",end="  ")
		pyttsx3.speak("which player, do you want to open?")
		multi_player=input()
		if("nope" in multi_player)or("no" in multi_player)or("end" in multi_player)or("exit" in multi_player)or("close" in multi_player)or("cancel" in multi_player):
			print("hey! "+name+", please answer me!")
			pyttsx3.speak("hey! "+name+", please answer me!")
		else:
			choose_pgm(multi_player)
	elif (("open" in pgm)or("run" in pgm)or("start" in pgm)or("execute" in pgm)or("" in pgm)or("launch" in pgm))and(("vlc" in pgm)or("player" in pgm)):
		os.system("vlc")
		print("vlc is opened...")
		pyttsx3.speak("vlc is opened...")
	elif (("open" in pgm)or("run" in pgm)or("start" in pgm)or("execute" in pgm)or("" in pgm)or("launch" in pgm))and(("wm" in pgm)or("windows" in pgm)or("media" in pgm)or("player"in pgm)):
		os.system("wmplayer")
		print("media player is opened...")
		pyttsx3.speak("media player is opened...")
	elif (("open" in pgm)or("run" in pgm)or("start" in pgm)or("execute" in pgm)or("" in pgm)or("launch" in pgm))and(("photo" in pgm)or("viewer" in pgm)):
		os.system("picasa3")
		print("view and edit your photo with picasa...")
		pyttsx3.speak("view and edit your photo with picasa...")
	elif (("open" in pgm)or("run" in pgm)or("start" in pgm)or("execute" in pgm)or("" in pgm)or("launch" in pgm))and(("teamviewer" in pgm)or("share screen" in pgm)):
		os.system("teamviewer")
		print("work with your team...")
		pyttsx3.speak("work with your team...")
	elif ((("open" in pgm)or("run" in pgm)or("start" in pgm)or("execute" in pgm)or("" in pgm))and(("microsoft office" in pgm)or("ms office" in pgm))) and(("word" not in pgm) and ("excel" not in pgm ) and ("outlook" not in pgm)and ("powerpoint" not in pgm)and("access" not in pgm)):
		print("Alas! This package contains more softwares...")
		pyttsx3.speak("Alas! This package contains more softwares...")
		print("which software, do you want to open?",end="  ")
		pyttsx3.speak("which software, do you want to open?")
		ms=input()
		if("nope" in ms)or("no" in ms)or("end" in ms)or("exit" in ms)or("close" in ms)or("cancel" in ms):
			print("hey! "+name+", please answer me!")
			pyttsx3.speak("hey! "+name+"please answer me!")
		else:
			choose_pgm(ms)
	elif (("open" in pgm)or("run" in pgm)or("start" in pgm)or("execute" in pgm)or("" in pgm)or("launch" in pgm))and(("word" in pgm)or("document" in pgm)):
		os.system("winword")
		print("cool to see your document...")
		pyttsx3.speak("cool to see your document...")
	elif (("open" in pgm)or("run" in pgm)or("start" in pgm)or("execute" in pgm)or("" in pgm)or("launch" in pgm))and(("excel" in pgm)or("spreadsheet" in pgm)):
		os.system("excel")
		print("cool to see your spreadsheet...")
		pyttsx3.speak("cool to see your spreadsheet...")
	elif (("open" in pgm)or("run" in pgm)or("start" in pgm)or("execute" in pgm)or("" in pgm)or("launch" in pgm))and(("powerpoint" in pgm)or("ppt" in pgm)or("presentation" in pgm)):
		os.system("powerpnt")
		print("cool to see your presentation...")
		pyttsx3.speak("cool to see your presentation...")
	elif (("open" in pgm)or("run" in pgm)or("start" in pgm)or("execute" in pgm)or("" in pgm)or("launch" in pgm))and("access" in pgm):
		os.system("msaccess")
		print("cool to see your database...")
		pyttsx3.speak("cool to see your database...")
	elif (("open" in pgm)or("run" in pgm)or("start" in pgm)or("execute" in pgm)or("" in pgm)or("launch" in pgm))and("outlook" in pgm):
		os.system("outlook")
		print("check your mail...")
		pyttsx3.speak("check your mail...")
	elif("nope" in pgm)or("no" in pgm)or("end" in pgm)or("exit" in pgm)or("close" in pgm):
		end_conv()
	else:
		print("I am sorry! I didn't prepared for this command, can you please make it more clear...")
		pyttsx3.speak("i am sorry! i didn't prepared for this command, can you please make it more clear...")
		print("")
		print("I am prepared for launching:")
		pyttsx3.speak("I am prepared for launching:")
		print("1. Your browser(includes chrome,firefox,internet explorer, ms edge)") 
		pyttsx3.speak("Your browser(includes chrome,firefox,internet explorer, ms edge)")
		print("2. Microsoft office(includes word, excel, powepoint, access, outlook)")
		pyttsx3.speak("Microsoft office(includes word, excel, powepoint, access, outlook)")
		print("3. player(includes vlc, windows media player)")
		pyttsx3.speak("player(includes vlc, windows media player)")
		print("4. Python interpreter, Eclipse IDE")
		pyttsx3.speak("Python interpreter, Eclipse IDE")
		print("5. Text Editor(Notepad)") 
		pyttsx3.speak("Text Editor(Notepad)")
		print("6. Tools like tableau, bandicam, calculator, teamviewer, picasa3")
		pyttsx3.speak("Tools like tableau, bandicam, calculator, teamviewer, picasa3")
		print("")
			
print(wishes+"!! I am vireo, a perfect assistant to navigate between programs in your system. Can you please share your name?",end="  ")
pyttsx3.speak(wishes+"!! I am vireo, a perfect assistant to navigate between programs in your system. Can you please share your name?")
name=input()


#permission to continue
print("Hey "+name+", Can we start to navigate?", end="  ")
pyttsx3.speak("Hey "+name+", Can we start to navigate")
condition=input()


if ("yes" in condition.lower()) or ("yeah" in condition.lower()) or (("s" in condition.lower())and(len(condition)==1)) or ("yup" in condition.lower()) or ("ok" in condition.lower()) or ("okay" in condition.lower()) or ("kk" in condition.lower()):
	count=1
	while(count>0):
		if(count==1):
			print("Which program do you want to start first?", end="  ")
			pyttsx3.speak("Which program do you want to start first?")
			which_pgm=input()
			if("nope" in which_pgm)or("no" in which_pgm)or("end" in which_pgm)or("exit" in which_pgm)or("close" in which_pgm)or("cancel" in which_pgm):
					print("hey! "+name+", please answer me!")
					pyttsx3.speak("hey! "+name+"please answer me!")
					count=0
			else:
				choose_pgm(which_pgm.lower())
		
		if(count>1):
			print("Do you need any other program to run:",end="  ")
			pyttsx3.speak("Do you need any other program to run")
			condition=input()
			if ("yes" in condition.lower()) or ("yeah" in condition.lower()) or (("s" in condition.lower())and(len(condition)==1)) or ("yup" in condition.lower()) or ("ok" in condition.lower()) or ("okay" in condition.lower()) or ("kk" in condition.lower()):
				print("which you program do you want to run now?",end="  ")
				pyttsx3.speak("which you program do you want to run now?")
				which_pgm=input()
				which_pgm=which_pgm.lower()
				choose_pgm(which_pgm)
				if("nope" in which_pgm)or("no" in which_pgm)or("end" in which_pgm)or("exit" in which_pgm)or("close" in which_pgm)or("cancel" in which_pgm):
					print("hey! "+name+", please answer me!")
					pyttsx3.speak("hey! "+name+"please answer me!")
			elif ("no" in condition.lower()) or ("nope" in condition.lower()) or (("end" in condition.lower())and(len(condition)==1)) or ("exit" in condition.lower()) or ("cancel" in condition.lower()):
				end_conv()
				count=-1
			else:
				print("hey! "+name+", please answer me!")
				pyttsx3.speak("hey! "+name+"please answer me!")
		if(((count%7)==0)and(count!=0)):
			print("Do you like to clear the screen?",end="  ")
			pyttsx3.speak("Do you like to clear the screen?")
			condition=input()
			if ("yes" in condition.lower()) or ("yeah" in condition.lower()) or (("s" in condition.lower())and(len(condition)==1)) or ("yup" in condition.lower()) or ("ok" in condition.lower()) or ("okay" in condition.lower()) or ("kk" in condition.lower()):
				os.system("cls")
		count+=1			 
elif ("no" in condition.lower()) or ("nope" in condition.lower()) or (("end" in condition.lower())and(len(condition)==1)) or ("exit" in condition.lower()) or ("cancel" in condition.lower()):
	end_conv()
else:
	print("hey! "+name+", please answer me!")
	pyttsx3.speak("hey! "+name+"please answer me!")

		
