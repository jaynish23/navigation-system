import pyttsx3
import speech_recognition as sr
    
class voice_assistant:

    def __init__(self):
        self.recognizer = sr.Recognizer()

        self.engine = pyttsx3.init('sapi5')
        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', rate - 25)
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)

        self.assistant_active = False

    def speak(self,audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def listen(self, _duration, _timeout):
        with sr.Microphone() as source:
            try:
                self.recognizer.adjust_for_ambient_noise(source, duration=_duration)
                audio = self.recognizer.listen(source, timeout=_timeout)
                query = self.recognizer.recognize_google(audio)
                return query.lower()
            except sr.WaitTimeoutError:
                error="No speech detected within timeout period."
                print(error)
                #if self.assistant_active: self.speak(error)
                return None
            except sr.UnknownValueError:
                error="Sorry, I didn't catch that."
                print(error)
                if self.assistant_active: self.speak(error)

                return None
            except sr.RequestError:
                error="Sorry, I'm having trouble accessing the Google API. Please try again later."
                print(error)
                if self.assistant_active: self.speak(error)
                return None
            