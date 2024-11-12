import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()                # voice recognize
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)    # for female voice


def talk(text):
    alexa.say(text)
    alexa.runAndWait()


def take_command():
    command = ""  # Initialize the command variable
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()             # lower case
            if 'alexa' in command:                    # mention command to alexa,not other person like siri
                command = command.replace('alexa', '')
            print(f"Command received: {command}")
    except sr.UnknownValueError:
        print("Sorry, I did not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"An error occurred: {e}")  # Print the error message for debugging
    return command


def run_alexa():
    command = take_command()            # take command from user
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)             # pywhatkit for search youtube
    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')        # ' ' - empty string. replace or user's command
        info = wikipedia.summary(look_for, 1)                        # 1 line  reply
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'date' in command:
        talk('Sorry vaiya, I am in another relation')
    else:
        talk('I did not get it but I am going to search it for you')
        pywhatkit.search(command)

while True:
     run_alexa()                                            # EXECUTION will start here

                            # block ensures that the voice assistant runs properly when executed directly, listens indefinitely,
                            # handles keyboard interruptions gracefully, and catches unexpected errors to provide feedback.


# if __name__ == "__main__":            # used to make sure the script behaves correctly when run as the main program

#     try:
#         while True:
#             run_alexa()                # EXECUTION will start here
#     except KeyboardInterrupt:
#         print("Program interrupted by user")
#     except Exception as e:
#         print(f"An error occurred: {e}")

