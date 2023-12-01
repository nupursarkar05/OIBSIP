import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize voice commands
def recognize_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"User: {command}")
            return command.lower()
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            speak("Sorry, I cannot process your request at the moment.")
            return ""

# Function to perform actions based on voice commands
def process_command(command):
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today's date is {current_date}")
    elif "search" in command:
        speak("What do you want to search for?")
        query = recognize_command()
        if query:
            search_url = f"https://www.google.com/search?q={query}"
            webbrowser.open(search_url)
        else:
            speak("I didn't catch that. Please try again.")

# Main loop to listen for voice commands
while True:
    command = recognize_command()
    if command:
        process_command(command)