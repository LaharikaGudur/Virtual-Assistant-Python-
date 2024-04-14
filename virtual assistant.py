import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("voices",voices[0].id)

def speak(audio):
  engine.say(audio)
  engine.runAndWait()

def wishme():
  hour = int(datetime.datetime.now().hour)
  if hour>=0 and hour<12:
    speak("Good Morning")
  elif hour>=12 and hour<18:
    speak("Good Afternoon")
  else:
    speak("Good Evening")

  speak("I am Alexa mam,Please tell me how may I help you")

wishme()

def takecommand():
  r = sr.Recognizer()

  with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=2)
    print("Listening...")
    audio = r.listen(source)
  try:
    print("Recognizing...")
    query = r.recognize_google(audio, language="en-in")
    print(f"User said:{query}")
  except:
    print("say that again please")
    return "None"
  return query

#wishme()
while True:
  query = takecommand().lower()

  if "Who are you" in query:
    speak("I am your virtual assistant mam, my name is Alexa")
  elif "What can you do" in query:
    speak("I can search google,facebook,search wikipedia")
  elif "sleep" in query:
    break  
