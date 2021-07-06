import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener = sr.Recognizer() # Recognize speech 
engine = pyttsx3.init() # Initialise python text to speech converter
engine.say('Hi I am JARVIS Your Personal Assistant')
engine.say('What can I do for you ?')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source: # Input from microphone
            print('Listening...')
            voice = listener.listen(source) # Listenining to source or I/p from microphone and passing it to listener to recognise speech.
            command = listener.recognize_google(voice) # Uses google API to convert voice into text
            command = command.lower() # Convert to lower case
            if 'jarvis' in command:
                command = command.replace('jarvis', ' ') # Remove jarvis from speech
                
    except:
        pass
        
    return command

def run_command():
    command = take_command() # Calls take command function
    print(command)
    if ('play' in command):
        song = command.replace('play', '') # Remove play from function
        talk('playing'+ song)
        pywhatkit.playonyt(song)
    elif('time' in command):
        time = datetime.datetime.now().strftime('%I : %M %p') # Time in hours and minutes
        # % I = 12 hr format, % p = am/pm
        print(time)
        talk('Current time is'+ time)
    elif('are you single' in command):
        talk('I am in a relationship with Siri')

    elif('who are you' in command):
        talk('I am a personal assistant created by Apuroop Paravada')

    elif('joke' in command):
        talk(pyjokes.get_joke())

    elif('who is' in command):
        person = command.replace('who is','')
        info = wikipedia.summary(person,1) # will retreive 1 line of information
        print(info)
        talk(info)
    else:
        talk('Sorry I am not programmed to answer this. Please try asking a different question')
    
    
  
while True:
    run_command()
