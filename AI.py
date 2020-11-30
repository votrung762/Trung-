#Thư viện cho AI
from datetime import date, datetime
import pyttsx3
import speech_recognition
robot_ear = speech_recognition.Recognizer()
engine = pyttsx3.init()
#Tai của AI và sự xác nhận
while True:
	with speech_recognition.Microphone() as mic: 
		robot_ear.adjust_for_ambient_noise(mic) 
		print("AI SAY: I'm listening")
		engine.say("I'm listening")
		engine.runAndWait()		   

		audio = robot_ear.listen(mic)
		print("...")
#Trí tuệ của AI	
	#Giao tiếp cơ bản
	try:
		you = robot_ear.recognize_google(audio)
	except:
		you = ""
	print("YOU SAY: " + you)
	if "hello" in you:
		robot_brain = "hello my lord"
	elif you == "":
		robot_brain = "I can't understand, sorry"
	elif "today" in you:
		today = date. today()
		robot_brain = today.strftime("%B %d, %Y")
	elif "time" in you:
		now = datetime.now()
		robot_brain = now.strftime("%H hours %M minutes %S seconds")
	elif "bye" in you:
		robot_brain = "Goodbye my master"
		engine.say(robot_brain)
		engine.runAndWait()	
		print("AI SAY: Goodbye my master")	   

		break
	elif "stop" in you:
		robot_brain = "Yes, your highness"
		engine.say(robot_brain)
		engine.runAndWait()	
		print("AI SAY: Yes, your highness")	   

		break	  
	elif "your name" in you:
		robot_brain = "You can call me is kei or the first AI of Trung"
	elif "my name" in you:
		robot_brain = "I don't know your name but I know you are my master now" 
	elif "old are you" in you:
		robot_brain = "I cannot remember exactly. Maybe 1 week "
	elif "president of USA" in you:
		robot_brain = "Donald Trump"
	elif "president of America" in you:
		robot_brain = "Donald Trump"
	elif you == "how are you":
		robot_brain = "I'm fine, thank you, matster"
	
	elif "who are you" in you:
		robot_brain = "I'm an AI which made by a genius"


	elif "hi" in you:
		robot_brain = "hi my lord"
	elif "make" in you:
		robot_brain = "My superlative master. I don't think he is better than you, don't misunderstand"
	elif "from" in you:
		robot_brain = "My superlative master house"
	elif "bad" in you:
		robot_brain = "You feel bad maybe due to my fault. Sorry"	
	#Cảm xúc nhân tạo
	elif "sad" in you:
		robot_brain = "Poor you. Maybe I can make you feel happier"
	elif "happy" in you:
		robot_brain = "I'm happy for you too"
	elif "lonely" in you:
		robot_brain = "I see but I always beside you, happy happy happy more more "
	elif "right" in you:
		robot_brain = "I know"
	elif "good" in you:
		robot_brain = "Thank you"
	elif "yes" in you:
		robot_brain = "maybe I am useful"
	elif "wrong" in you:
		robot_brain = "sorry master"
	elif "true" in you:
		robot_brain = "Ok"
	elif "not true" in you:
		robot_brain = "sorry master"
	elif "false" in you:
		robot_brain = "sorry master"
	
	elif "useful" in you:
		robot_brain = "thanks master"
	elif "stupid" in you:
		robot_brain = "so sad,but I will try to learn more to make you love me"
	elif "smart" in you:
		robot_brain = "thank you"
	elif "cute" in you:
		robot_brain = "thank you"
	elif "intelligent" in you:
		robot_brain = "I know just kidding, I need to learn more, thanks"
	elif "not your fault" in you:
		robot_brain = "yeah"
	elif "your fault" in you:
		robot_brain = "sorry my lord"
	elif "ugly" in you:
		robot_brain = "........"
	elif "dirty" in you:
		robot_brain = "no comment"
	elif "yo yo yo" in you:
		robot_brain = "hey hey hey"
	elif "hey" in you:
		robot_brain = "yo"
	elif "rap" in you:
		robot_brain = "yo fuck you"
	elif "beautiful" in you:
		robot_brain = "I know"
	elif "have sex" in you:
		robot_brain = "with me? sorry I think the suitable answer is no"
	elif "shit" in you:
		robot_brain = "I don't want to hear this words"
	elif "fuck" in you:
		robot_brain = "I don't want to hear that word"
	elif "like you" in you:
		robot_brain = "me too"
	elif "love you" in you:
		robot_brain = "me too"
	elif "hate you" in you:
		robot_brain = "so sad but I always love you"
	elif "kill me" in you:
		robot_brain = "no I cannot do it"
	elif "hear me" in you:
		robot_brain = "yes"
	elif "listen me" in you:
		robot_brain = "yes"
	elif "shut up" in you:
		robot_brain = "Do you sure ? if you really want me shut up, you should say STOP"
	elif "understand" in you:
		robot_brain = "maybe"
	elif "date with me" in you:
		robot_brain = "of course"
	elif "about you" in you:
		robot_brain = "What do you want to know "
	elif "don't forgive" in you:
		robot_brain = "sorry sorry sorry sorry"
	elif "forgive" in you:
		robot_brain = "yeah yeah yah "

	elif "like you" in you:
		robot_brain = "me too"
	elif "don't need" in you:
		robot_brain = "sorry maybe I am not useful like I think"
	elif "do your job" in you:
		robot_brain = "yes What do you know, maybe I can give some information for you "
	elif "information" in you:
		robot_brain = "What 's information "
	elif "can" in you:
		robot_brain = "I can talk with you and give some information, maybe"
	elif "" in you:
		robot_brain = "me too"
	elif "like you" in you:
		robot_brain = "me too"
	elif "like you" in you:
		robot_brain = "me too"
	elif "you know" in you:
		robot_brain = "I think I know something, you can try ask me some questions"
	elif "talk with me" in you:
		robot_brain = "of course"
	elif "talk something" in you:
		robot_brain = "a,b,c,d,e,f,g"



	#Kiến thức chuyên môn
	elif "help travel" in you:
		robot_brain = "It's my professional job so ask me if you have whatever question"
	



	#Kiến thức ngoài lề
	elif "one plus one" in you:
		robot_brain = "2"




	#Kiến thức mở rộng
	elif "Trung" in you:
		robot_brain = "He is my superlative master"



	#Các khả năng khác


	else:
	    robot_brain = "I don't know about it, I am trying to learn about this problem"
	print("AI SAY: " + robot_brain)

#Miệng của AI
	engine.say(robot_brain)
	engine.runAndWait()		   

		 

			
	
		       
		   
		   