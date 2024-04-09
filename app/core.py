import speech_recognition as sr

class SpeechRecognizer:
    def __init__(self):
        self.__recognizer = sr.Recognizer()
        self.__microphone = sr.Microphone()

    def get_audio(self):
        with self.__microphone as source:
            self.__recognizer.adjust_for_ambient_noise(source, duration=0.5)
            return self.__recognizer.listen(source)

    def get_recognizer(self):
        return self.__recognizer

class SpeechAdapter:
    def __init__(self, speech_recognizer):
        self.__speech_recognizer = speech_recognizer

    def recognize(self, audio):
        return self.__speech_recognizer.recognize_google(audio, language="pt-BR", key=None, show_all=False)

class TextProcessor:
    def process_text(self, text):
        text = text.lower()
        print("You said: " + text)
        return "luna" in text

class CommandRecognizer:
    def __init__(self):
        self.__speech_recognizer = SpeechRecognizer()
        self.__speech_recognizer_api_adapter = SpeechAdapter(self.__speech_recognizer.get_recognizer())
        self.__text_processor = TextProcessor()

    def recognize_command(self):
        print("Luna is listening...")
        while True:
            try:
                audio = self.__speech_recognizer.get_audio()
                command = self.__speech_recognizer_api_adapter.recognize(audio)
                self.__text_processor.process_text(command)
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
            except sr.UnknownValueError:
                print("unknown error occurred")
