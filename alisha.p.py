import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import pywhatkit
import geocoder
import time
import tkinter as tk

engine = pyttsx3.init('sapi5')#to use inbuilt voices

voices = engine.getProperty('voices')#getting details of current voice

engine.setProperty('voice', voices[1].id)#helps us to select different voices

newVoicesRate = 140
engine.setProperty('rate',newVoicesRate)


#We use speak() function to convert our text to speech.
def speak(audio):
    engine.say(audio)
    engine.runAndWait()#Without this command, speech will not be audible to us.

# Now, we will make a wishme() function that will make our Alisha. 
# Wish or greet the user according to the time of computer or pc. 
# To provide current or live time to A.I., we need to import a module called datetime

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Alisha Sir or Madam. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()#help us to recognize the voice
    with sr.Microphone() as source: # We will use this as source moicrophone
        print("Listening...") #seconds of non-speaking audio before a phrase is considered as complete  
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.


    except Exception as e:
        # print(e)    
        print("Say that again please...")  #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

#We have created a main() function, and inside this main() Function, we will call our speak function.

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() #Whatever we will write inside this speak() function will be converted into speech

        # Logic for executing tasks based on query
        if 'wikipedia' in query:    #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # Here, we are using an elif loop to check whether Youtube is in the user's query.
        elif 'sleep'in  query:
                print(' let me know, if i can help you again have a great day.')
                speak(' let me know if i can help you again have a great day')
                break

        elif "hello" in query :
                speak(" hello and welcome ")
 
        elif "how are you" in query :
                speak(" i am good  i hope you are doing good as well  ") 

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open amazon' in query:
             webbrowser.open("www.amazon.in")   

        elif 'open flipkart' in query:
             webbrowser.open("www.flipkart.com")   

        #elif 'open chatbot' in query:
           # webbrowser.open("http://127.0.0.1:7860/")
                  

        #We first opened our music directory and then listed all the songs present in the directory with the os module's help. 
        
        #elif 'play music' in query:
         #   music_dir = 'C:\\Users\\Admin\\Desktop\\song'
          #  songs = os.listdir(music_dir)
           # print(songs)    
            #os.startfile(os.path.join(music_dir, songs[0])) #Here with the help of os.startfile, you can play any song of your choice.

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") #we are using the datetime()function and storing the current or live system time into a variable called strTime.  
            speak(f"Sir, the time is {strTime}")#After storing the time in strTime, we are passing this variable as an argument in speak function 

        elif 'open' in query:
            codePath = "http://127.0.0.1:7860"
            os.startfile(codePath)

        elif 'open notepad' in query:
            codePath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(codePath)    

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song) 


        elif 'alarm' in query:
            speak("Sir Please tell me the time to set the alarm")
            tt = takeCommand()
            tt = tt.replace("set alarm to", " ")
            tt = tt.replace("." , "")
            tt = tt.upper()
            import MyAlarm   
            MyAlarm.alarm(tt)
       

        

# code for setting a reminder
"""elif 'reminder' in query:
        speak('What would you like me to remind you of?')
        with sr.Microphone() as source:
            sr.adjust_for_ambient_noise(source)
            audio = sr.listen(source)
        try:
            reminder_text = sr.Recognizer(audio)
            speak(f"Okay, I will remind you to {reminder_text} in 5 minutes.")
            # code for scheduling the reminder
            reminder_time = datetime.datetime.now() + datetime.timedelta(minutes=5)
            os.system(f'start cmd /c "echo Reminder: {reminder_text} && timeout /t 300"')

        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            pass"""

# Create the main window
"""window = tk.Tk()
window.title("Virtual Desktop Assistant")

# Create the button for starting the speech recognition
start_button = tk.Button(window, text="Start Speaking", command=takeCommand)
start_button.pack()

# Start the GUI main loop
window.mainloop()"""

     

   

            

 