
# Sign Language & Voice Assistant

A Python-based desktop application that combines **sign language detection**, **voice commands**, **chatbot functionality**, and **WhatsApp message scheduling** into one intuitive interface. This system is designed to enhance accessibility and automate tasks using hand gestures and voice input.

---

## 🚀 Features

### ✋ Sign Language Detection (via webcam)

* Detects predefined hand gestures using **MediaPipe** and **OpenCV**.
* Opens specific websites based on gesture recognition:

  * **YouTube**
  * **Facebook**
  * **Twitter**
  * **Google**
  * **WhatsApp Web**

### 🎤 Voice Command Support

* Accepts spoken instructions using **SpeechRecognition** and processes them.
* Opens websites or searches Google for the spoken query.

### 💬 Chatbot (Text + Voice)

* Users can ask queries via text input or voice.
* Automatically performs a Google search for any question asked.

### 📱 WhatsApp Message Scheduler

* Send scheduled WhatsApp messages using **PyWhatKit**.
* Requires message, phone number, and time in `HH:MM` format.

---

## 🛠️ Tech Stack

* **Python 3.x**
* **OpenCV**
* **MediaPipe**
* **SpeechRecognition**
* **Pyttsx3** (Text-to-Speech)
* **Tkinter** (GUI)
* **PyWhatKit**
* **WebBrowser**
* **Threading & Queue**

---

## 🔧 Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/sign-language-voice-assistant.git
   cd sign-language-voice-assistant
   ```

2. Install dependencies:

   ```bash
   pip install opencv-python mediapipe SpeechRecognition pyttsx3 pywhatkit
   ```

3. Run the application:

   ```bash
   python app.py
   ```

---

## ✅ Usage Instructions

* **Start Sign Detection**: Launches webcam to detect hand gestures.
* **Voice Command**: Speak instructions like “open YouTube”.
* **Ask Chatbot**: Type or speak a question to search Google.
* **WhatsApp Message**: Enter a message, phone number (`without +91`), and time (`HH:MM`) to schedule sending.

---

## 🧠 Example Gestures Mapped

| Gesture Description                   | Action            |
| ------------------------------------- | ----------------- |
| Index finger pointing up              | Open YouTube      |
| Thumb crossing palm towards right     | Open Facebook     |
| Two fingers bent (8 and 12 landmarks) | Open Twitter      |
| Thumb up gesture                      | Open Google       |
| Pinky finger down                     | Open WhatsApp Web |

📝 Notes

* Make sure your **microphone** and **webcam** are enabled.
* Use **24-hour format** for scheduling WhatsApp messages.
* Internet connection is required for:

  * Voice recognition
  * Google search
  * WhatsApp message delivery

🙌 Credits

* [MediaPipe](https://mediapipe.dev/)
* [PyWhatKit](https://pypi.org/project/pywhatkit/)
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
* [OpenCV](https://opencv.org/)
  

📄 License

This project is open-source and free to use under the [MIT License](LICENSE).


