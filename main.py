
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init('dummy')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            listener.dynamic_energy_threshold = 3000
            print("listening...")
            voice = listener.listen(source,timeout=4.0)
            command = listener.recognize_google(voice)
            command = command .lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playing(song)
    elif'time' in command:
            time = datetime.datetime.now().strftime('%l:&M%p')
            talk('current time is '+ time )
    elif'who the heck is ' in command:
        person = command.replace('who the heck is','')
        info =wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif'date' in command:
        talk('sorry,i have headache')
    elif'are you single' in command:
        talk('yeah  i am single.for what are you asking')
    elif'tell me a joke ' in command:
        talk(pyjokes.get_joke())
    else:
        talk('please say something.')
        command = ""

while True:
    try:
        run_alexa()
    except UnboundLocalError:
            print("no command detected! alexa has stopped working")
            command = ""
            print(command)

