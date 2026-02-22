import speech_recognition as sr
import pyttsx3
import webbrowser
import requests
import google.generativeai as genai


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "3aca60d1c96344428b6e279b7c4884c4"


def speak(text):
    engine.say(text)
    engine.runAndWait()


genai.configure(api_key="YOUR_API_KEY_HERE") 
generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
)


history = []


print("Jarvis: Hello, HOW CAN I HELP YOU")
speak("Hello, how can I help you?")


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open gmail" in c.lower():
        webbrowser.open("https://gmail.com")
    elif "open x" in c.lower():
        webbrowser.open("https://x.com")
    elif "open classroom" in c.lower():
        webbrowser.open("https://google.classroom.com")
    elif "open google maps" in c.lower():
        webbrowser.open("https://google.maps.com")
    elif "open reddit" in c.lower():
        webbrowser.open("https://reddit.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open netflix" in c.lower():
        webbrowser.open("https://netflix.com")
    elif "open spotify" in c.lower():
        webbrowser.open("https://spotify.com")
    elif "open wikipedia" in c.lower():
        webbrowser.open("https://wikipedia.org")
    elif "open amazon" in c.lower():
        webbrowser.open("https://amazon.com")
    elif "open ebay" in c.lower():
        webbrowser.open("https://ebay.com")
    elif "open stackoverflow" in c.lower():
        webbrowser.open("https://stackoverflow.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif "open quora" in c.lower():
        webbrowser.open("https://quora.com")
    elif "open pinterest" in c.lower():
        webbrowser.open("https://pinterest.com")
    elif "open tiktok" in c.lower():
        webbrowser.open("https://tiktok.com")
    elif "open discord" in c.lower():
        webbrowser.open("https://discord.com")
    elif "open zoom" in c.lower():
        webbrowser.open("https://zoom.us")
    elif "open udemy" in c.lower():
        webbrowser.open("https://udemy.com")
    elif "open coursera" in c.lower():
        webbrowser.open("https://coursera.org")
    elif "open medium" in c.lower():
        webbrowser.open("https://medium.com")
    elif "open khan academy" in c.lower():
        webbrowser.open("https://khanacademy.org")
    elif "open udacity" in c.lower():
        webbrowser.open("https://udacity.com")
    elif "open news" in c.lower():
        webbrowser.open("https://news.google.com")
    elif "open bbc" in c.lower():
        webbrowser.open("https://bbc.com")
    elif "open cnn" in c.lower():
        webbrowser.open("https://cnn.com")
    elif "open flipkart" in c.lower():
        webbrowser.open("https://flipkart.com")
    elif "open snapdeal" in c.lower():
        webbrowser.open("https://snapdeal.com")
    elif "open swiggy" in c.lower():
        webbrowser.open("https://swiggy.com")
    elif "open zomato" in c.lower():
        webbrowser.open("https://zomato.com")
    elif "open paytm" in c.lower():
        webbrowser.open("https://paytm.com")
    elif "open google drive" in c.lower():
        webbrowser.open("https://drive.google.com")
    elif "open google docs" in c.lower():
        webbrowser.open("https://docs.google.com")
    elif "open google sheets" in c.lower():
        webbrowser.open("https://sheets.google.com")
    elif "open google maps" in c.lower():
        webbrowser.open("https://maps.google.com")
    elif "open imdb" in c.lower():
        webbrowser.open("https://imdb.com")
        webbrowser.open("https://google.classroom.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
       
        link = None
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, I could not find that song.")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            for article in data['articles']:
                print(article['title'])
                speak(article['title'])
        else:
            speak("Sorry, I could not fetch the news.")
    else:
        # Using Google Generative AI for unknown queries
        chat_session = model.start_chat(history=history)
        response = chat_session.send_message(c)
        model_response = response.text
        print(f'Bot: {model_response}')
        speak(model_response)

        # Update history for contextual understanding
        history.append({"role": "user", "parts": [c]})
        history.append({"role": "assistant", "parts": [model_response]})

# Function to get voice input
def getVoiceInput():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for voice input...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing speech...")
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected.")
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
        except sr.RequestError as e:
            print(f"Speech recognition error: {e}")
        return None

# Main loop to handle both text and voice input
if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        # Ask user if they want to use text or voice input
        input_mode = input("Would you like to use (T)ext or (V)oice input? ").lower()

        if input_mode == 't':
            # Text input mode
            command = input("Type your command: ")
            processCommand(command)
        elif input_mode == 'v':
            # Voice input mode
            command = getVoiceInput()
            if command:
                processCommand(command)
        else:
            print("Invalid input. Please choose either 'T' for text or 'V' for voice.")
