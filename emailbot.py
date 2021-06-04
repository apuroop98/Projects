# For this progream to work
# Go to your Gmail account -> Manage your Google Account -> Security -> Less secure app access -> Turn on.
# For any other person to test, change parameters in server.login and email['from']


import smtplib
 # Simple Mail Transfer Protocol. It is kind of a package to sernd email
# Get a server. It acts as a middle person.
# Ex: If you want to send an email to your friend, it goes from your system to server and then from server to your friends system.
import speech_recognition as sr
import pyttsx3
# Converts text to voice.Python talks to us using this package
from email.message import EmailMessage
# Imports structure of email
listener = sr.Recognizer()
# Listenes and recogonises what you are saying
engine = pyttsx3.init()
# Initialising python text to speech convertor

def talk(text):
    engine.say(text)        # Say text
    engine.runAndWait()     # Execute and stop

def get_info():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            # Listen to user commands
            info = listener.recognize_google(voice)
            # Uses google API to convert voice into text
            print(info)
            return info.lower() # COnverts all text to lower case

    except:
        pass

def send_email(receiver,subject,message):
    server = smtplib.SMTP('smtp.gmail.com',587)
    # Param 1 is server name, In this case we send mail using gmail
    # 2nd param is port(Similar to a door no in a large hallway)
    server.starttls()
    # TLS- TRansport Layer Security.This basically tells server to trust me :)
    server.login('apuroop98@gmail.com','Hetto@500')
    #1st param is your email address, 2nd param is your password.
    email = EmailMessage() #preexisting fun in python
    email['From'] = 'apuroop98@gmail.com' # Set senders email address
    email['To'] = receiver # Receivers mail address(given by you)
    email['subject'] = subject # Subject of email given by you
    email.set_content(message) # Body of email
    server.send_message(email) # Asking to server to send email(entire email with from, to subjevt and message)
    print('Email sent Succesfully !')
    
email_list = {          # Dictionary to map name to email address
    'myself':'apuroop98@gmail.com',
    'dad':'pvsravikumar@gmail.com'
}
def email_info():
    talk('To Whom You want to send Email') # calls talk function on top
    name = get_info()   #calls get info method on top
    receiver = email_list[name] # Maps name to email from email list dict
    print(receiver)
    talk('What is the subject of your Email?') # calls talk function on top
    subject = get_info() #calls get info method on top
    talk('Tell me the body of your Email ') # calls talk function on top
    message = get_info()  #calls get info method on top

    send_email(receiver,subject,message)


email_info()