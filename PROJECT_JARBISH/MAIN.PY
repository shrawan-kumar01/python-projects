import wikipedia
import datetime
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
#  sapi5 is a windows api inbuilt voice 
voices = engine.getProperty('voices')
# print(voices[1].id)   IRA_11.0
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

#  creating a wishing function 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <=12 :
        speak("good morning sir ")
    elif hour >=12 and hour<= 18:
        speak("good afternoon sir ")
    else:
        speak("goods evening sir ")
    speak("hy i'm zira , tell me how could i help you  ")

def takeCommand():
    # it take microphone as input and return a string 
    r= sr.Recognizer()
    with sr.Microphone() as source :
        print("listening ..... . ... ...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing..... ... ... .. . ")
        query = r.recognize_google(audio , language='en-in')
        print("suer said:~ ", query + "\n")
    
    except Exception as e:
        print(e)
        print()
        print("say that again please .... ")
        return "none"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            query = query.relpace("wikipedia","")
            reasult =wikipedia.summary(query,sentences = 3)
            speak("according to wikipedia")
            speak(reasult)
            #  defining the logic for command ecxecution 
            print(reasult)

    # speak("hii  i am zera")
