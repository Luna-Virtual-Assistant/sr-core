import speech_recognition as sr

class SR:
    def __init__(self):
        self.__recognizer = sr.Recognizer()
        self.__microphone = sr.Microphone()
        
    def recognize(self):
        print("Luna is listening...")

        while(True):
            try:
                with self.__microphone as source:
                    self.__recognizer.adjust_for_ambient_noise(source, duration=0.5)

                    audio = self.__recognizer.listen(source)

                    command = self.__recognizer.recognize_google(audio, language="pt-BR", key=None, show_all=False)
                    command = command.lower()

                    print(f"Command: {command}")
                    if "luna" in command:
                        return command

            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))

            except sr.UnknownValueError:
                print("unknown error occurred")