# import cv2
# import mediapipe as mp
# import numpy as np
# import speech_recognition as sr
# import pyttsx3
# import webbrowser
# import tkinter as tk
# from tkinter import Label, Button, Entry
# import threading
# import queue
# import requests
# import pywhatkit
# import datetime

# # Initialize Text-to-Speech engine
# engine = pyttsx3.init()
# speech_queue = queue.Queue()

# def process_speech_queue():
#     while True:
#         text = speech_queue.get()
#         engine.say(text)
#         engine.runAndWait()
#         speech_queue.task_done()

# # Start a dedicated thread for speech synthesis
# speech_thread = threading.Thread(target=process_speech_queue, daemon=True)
# speech_thread.start()

# def Say(text):
#     speech_queue.put(text)

# # Function to send WhatsApp message
# def send_whatsapp_message():
#     message = message_entry.get()
#     number = number_entry.get()
#     time = time_entry.get()
#     try:
#         hours, minutes = map(int, time.split(':'))
#         Say(f"The message will get delivered at {time}")
#         pywhatkit.sendwhatmsg(f"+91{number}", message, hours, minutes)
#         Say("Message delivered")
#     except ValueError:
#         Say("Invalid time format. Please enter in HH:MM format.")

# # Function to take voice input
# def take_voice_command():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         recognizer.pause_threshold = 1
#         try:
#             audio = recognizer.listen(source)
#             command = recognizer.recognize_google(audio, language="en-in").lower()
#             print(f"User said: {command}")
#             return command
#         except sr.UnknownValueError:
#             print("Could not understand the audio")
#             return ""
#         except sr.RequestError:
#             print("Could not request results; check your internet connection")
#             return ""

# # Process voice commands
# def process_voice_command():
#     command = take_voice_command()
#     if "open youtube" in command:
#         Say("Opening YouTube")
#         webbrowser.open("https://youtube.com")
#     elif "open facebook" in command:
#         Say("Opening Facebook")
#         webbrowser.open("https://facebook.com")
#     elif "open twitter" in command:
#         Say("Opening Twitter")
#         webbrowser.open("https://twitter.com")
#     elif "open google" in command:
#         Say("Opening Google")
#         webbrowser.open("https://google.com")
#     else:
#         Say("Searching Google for your query")
#         webbrowser.open(f"https://www.google.com/search?q={command}")

# # Initialize MediaPipe Hands
# mp_hands = mp.solutions.hands
# mp_drawing = mp.solutions.drawing_utils
# hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# def recognize_signs():
#     cap = cv2.VideoCapture(0)
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break
#         frame = cv2.flip(frame, 1)
#         rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         results = hands.process(rgb_frame)
#         if results.multi_hand_landmarks:
#             for hand_landmarks in results.multi_hand_landmarks:
#                 mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
#                 landmarks = [(lm.x, lm.y) for lm in hand_landmarks.landmark]
                
#                 if len(landmarks) > 8:
#                     if landmarks[8][1] < landmarks[6][1]:
#                         Say("Opening YouTube")
#                         webbrowser.open("https://youtube.com")
#                     elif landmarks[4][0] > landmarks[12][0]:
#                         Say("Opening Facebook")
#                         webbrowser.open("https://facebook.com")
#                     elif landmarks[8][1] > landmarks[6][1] and landmarks[12][1] > landmarks[10][1]:
#                         Say("Opening Twitter")
#                         webbrowser.open("https://twitter.com")
#                     elif landmarks[4][1] < landmarks[2][1]:
#                         Say("Opening Google")
#                         webbrowser.open("https://google.com")
#                     elif landmarks[20][1] > landmarks[18][1]:
#                         Say("Opening WhatsApp Web")
#                         webbrowser.open("https://web.whatsapp.com")
#         cv2.imshow('Sign Language Detection', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     cap.release()
#     cv2.destroyAllWindows()

# # Chatbot response function
# def chatbot_response():
#     question = chatbot_entry.get()
#     Say(f"Searching for {question}")
#     url = f"https://www.google.com/search?q={question}"
#     webbrowser.open(url)

# def start_chatbot_voice():
#     question = take_voice_command()
#     chatbot_entry.delete(0, tk.END)
#     chatbot_entry.insert(0, question)
#     chatbot_response()

# def exit_program():
#     root.destroy()

# def main_ui():
#     global root, chatbot_entry, message_entry, number_entry, time_entry
#     root = tk.Tk()
#     root.title("Sign Language & Voice Assistant")
#     root.geometry("500x600")
#     root.configure(bg="#222831")
    
#     Label(root, text="Sign Language & Voice Assistant", font=("Arial", 16, "bold"), bg="#222831", fg="white").pack(pady=10)
    
#     Button(root, text="Start Sign Detection", font=("Arial", 12), bg="#00ADB5", fg="white", command=lambda: threading.Thread(target=recognize_signs).start()).pack(pady=5)
#     Button(root, text="Voice Command", font=("Arial", 12), bg="#00ADB5", fg="white", command=lambda: threading.Thread(target=process_voice_command).start()).pack(pady=5)
    
#     chatbot_entry = Entry(root, font=("Arial", 12), width=30)
#     chatbot_entry.pack(pady=10)
    
#     Button(root, text="Ask Chatbot", font=("Arial", 12), bg="#00ADB5", fg="white", command=lambda: threading.Thread(target=chatbot_response).start()).pack(pady=5)
    
#     Label(root, text="WhatsApp Message", font=("Arial", 12, "bold"), bg="#222831", fg="white").pack(pady=10)
#     Label(root, text="Message:", bg="#222831", fg="white").pack()
#     message_entry = Entry(root)
#     message_entry.pack()
    
#     Label(root, text="Number:", bg="#222831", fg="white").pack()
#     number_entry = Entry(root)
#     number_entry.pack()
    
#     Label(root, text="Time (HH:MM):", bg="#222831", fg="white").pack()
#     time_entry = Entry(root)
#     time_entry.pack()
    
#     Button(root, text="Send WhatsApp Message", font=("Arial", 12), bg="#00ADB5", fg="white", command=lambda: threading.Thread(target=send_whatsapp_message).start()).pack(pady=5)
#     Button(root, text="Exit", font=("Arial", 12), bg="#FF3E4D", fg="white", command=exit_program).pack(pady=10)
#     root.mainloop()

# if __name__ == "__main__":
#     main_ui()




import cv2
import mediapipe as mp
import numpy as np
import speech_recognition as sr
import pyttsx3
import webbrowser
import tkinter as tk
from tkinter import Label, Button, Entry
import threading
import queue
import requests
import pywhatkit
import datetime
import time as systime  # For delay in gesture action

# Initialize Text-to-Speech engine
engine = pyttsx3.init()
speech_queue = queue.Queue()

def process_speech_queue():
    while True:
        text = speech_queue.get()
        engine.say(text)
        engine.runAndWait()
        speech_queue.task_done()

# Start a dedicated thread for speech synthesis
speech_thread = threading.Thread(target=process_speech_queue, daemon=True)
speech_thread.start()

def Say(text):
    speech_queue.put(text)

# Function to send WhatsApp message
def send_whatsapp_message():
    message = message_entry.get()
    number = number_entry.get()
    time = time_entry.get()
    try:
        hours, minutes = map(int, time.split(':'))
        Say(f"The message will get delivered at {time}")
        pywhatkit.sendwhatmsg(f"+91{number}", message, hours, minutes)
        Say("Message delivered")
    except ValueError:
        Say("Invalid time format. Please enter in HH:MM format.")

# Function to take voice input
def take_voice_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio, language="en-in").lower()
            print(f"User said: {command}")
            return command
        except sr.UnknownValueError:
            print("Could not understand the audio")
            return ""
        except sr.RequestError:
            print("Could not request results; check your internet connection")
            return ""

# Process voice commands
def process_voice_command():
    command = take_voice_command()
    if "open youtube" in command:
        Say("Opening YouTube")
        webbrowser.open("https://youtube.com")
    elif "open facebook" in command:
        Say("Opening Facebook")
        webbrowser.open("https://facebook.com")
    elif "open twitter" in command:
        Say("Opening Twitter")
        webbrowser.open("https://twitter.com")
    elif "open google" in command:
        Say("Opening Google")
        webbrowser.open("https://google.com")
    else:
        Say("Searching Google for your query")
        webbrowser.open(f"https://www.google.com/search?q={command}")

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Gesture handling cooldown
last_gesture_time = 0
gesture_cooldown = 3  # seconds

def recognize_signs():
    global last_gesture_time
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)
        current_time = systime.time()

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                landmarks = [(lm.x, lm.y) for lm in hand_landmarks.landmark]

                if len(landmarks) > 8 and (current_time - last_gesture_time) > gesture_cooldown:
                    if landmarks[8][1] < landmarks[6][1]:
                        Say("Opening YouTube")
                        webbrowser.open("https://youtube.com")
                        last_gesture_time = current_time
                    elif landmarks[4][0] > landmarks[12][0]:
                        Say("Opening Facebook")
                        webbrowser.open("https://facebook.com")
                        last_gesture_time = current_time
                    elif landmarks[8][1] > landmarks[6][1] and landmarks[12][1] > landmarks[10][1]:
                        Say("Opening Twitter")
                        webbrowser.open("https://twitter.com")
                        last_gesture_time = current_time
                    elif landmarks[4][1] < landmarks[2][1]:
                        Say("Opening Google")
                        webbrowser.open("https://google.com")
                        last_gesture_time = current_time
                    elif landmarks[20][1] > landmarks[18][1]:
                        Say("Opening WhatsApp Web")
                        webbrowser.open("https://web.whatsapp.com")
                        last_gesture_time = current_time

        cv2.imshow('Sign Language Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# Chatbot response function
def chatbot_response():
    question = chatbot_entry.get()
    Say(f"Searching for {question}")
    url = f"https://www.google.com/search?q={question}"
    webbrowser.open(url)

def start_chatbot_voice():
    question = take_voice_command()
    chatbot_entry.delete(0, tk.END)
    chatbot_entry.insert(0, question)
    chatbot_response()

def exit_program():
    root.destroy()

def main_ui():
    global root, chatbot_entry, message_entry, number_entry, time_entry
    root = tk.Tk()
    root.title("Sign Language & Voice Assistant")
    root.geometry("500x600")
    root.configure(bg="#222831")

    Label(root, text="Sign Language & Voice Assistant", font=("Arial", 16, "bold"), bg="#222831", fg="white").pack(pady=10)

    Button(root, text="Start Sign Detection", font=("Arial", 12), bg="#00ADB5", fg="white",
           command=lambda: threading.Thread(target=recognize_signs).start()).pack(pady=5)
    Button(root, text="Voice Command", font=("Arial", 12), bg="#00ADB5", fg="white",
           command=lambda: threading.Thread(target=process_voice_command).start()).pack(pady=5)

    chatbot_entry = Entry(root, font=("Arial", 12), width=30)
    chatbot_entry.pack(pady=10)

    Button(root, text="Ask Chatbot", font=("Arial", 12), bg="#00ADB5", fg="white",
           command=lambda: threading.Thread(target=chatbot_response).start()).pack(pady=5)

    Label(root, text="WhatsApp Message", font=("Arial", 12, "bold"), bg="#222831", fg="white").pack(pady=10)
    Label(root, text="Message:", bg="#222831", fg="white").pack()
    message_entry = Entry(root)
    message_entry.pack()

    Label(root, text="Number:", bg="#222831", fg="white").pack()
    number_entry = Entry(root)
    number_entry.pack()

    Label(root, text="Time (HH:MM):", bg="#222831", fg="white").pack()
    time_entry = Entry(root)
    time_entry.pack()

    Button(root, text="Send WhatsApp Message", font=("Arial", 12), bg="#00ADB5", fg="white",
           command=lambda: threading.Thread(target=send_whatsapp_message).start()).pack(pady=5)
    Button(root, text="Exit", font=("Arial", 12), bg="#FF3E4D", fg="white", command=exit_program).pack(pady=10)
    root.mainloop()

if __name__ == "__main__":
    main_ui()
