import speech_recognition as sr
import pyttsx3
import webbrowser
import musiclibrary
import requests
import os
import google.generativeai as genai


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "AIzaSyAdk9nSKAO3B7Kdts3gHfwaN-HlQDTN79Q"


def speak(text):
    engine.say(text)
    engine.runAndWait()

genai.configure(api_key="AIzaSyC5Jjq7Ei7YLBvQhlO0d8p0NB_vkEn0sTY")

generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}


model = genai.GenerativeModel(
  model_name="gemini-2.5-flash-lite",
  generation_config=generation_config,
)

history = []


print("Jarvis: Hello, HOW MAY I HELP YOU")
speak("Hello, how may I help you?")

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
    
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1:]
        link = "https://music.youtube.com/search?q="+" ".join(song)


        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, I could not find that song.")

    elif c.lower().startswith("youtube"):
        title = c.lower().split(" ")[1:]
        link = "https://youtube.com/search?q="+" ".join(title)


        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, I could not find that song.")
    
    elif c.lower().startswith("search"):
        term = c.lower().split(" ")[1:]
        if len(term)==0:
            speak("I didn't get that.")
        else:
            if term[0] == "for":
                term = term[1:]
            link = "https://www.google.com/search?hl=en&q="+" ".join(term)


            if link:
                webbrowser.open(link)

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
        chat_session = model.start_chat(history=history)
        response = chat_session.send_message(c)
        model_response = response.text
        print(f'Bot: {model_response}')
        speak(model_response)


        history.append({"role": "user", "parts": [c]})
        history.append({"role": "assistant", "parts": [model_response]})


# main loop
if __name__ == "__main__":

    while True:
        mode = input("Enter 's' to speak or 't' to type: ").strip().lower()

        if mode == 's':
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                print("Listening...")

                try:
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    print("Responding...")
                    command = recognizer.recognize_google(audio)
                    print(f"You said: {command}")

                    processCommand(command)

                    if "jarvis" in command.lower():
                        print("Jarvis detected, responding with 'yaa'...")
                        speak("yaa")

                except sr.WaitTimeoutError:
                    print("Timeout: No speech detected.")
                except sr.UnknownValueError:
                    print("Jarvis could not understand audio.")
                except sr.RequestError as e:
                    print(f"Could not request results from Google Speech Recognition service; {e}")

        elif mode == 't':
            command = input("Type your command: ").strip()
            print(f"You typed: {command}")
            processCommand(command)

            if "jarvis" in command.lower():
                print("Jarvis detected, responding with 'yaa'...")
                speak("yaa")

        else:
            print("Invalid option. Please enter 's' to speak or 't' to type.")

