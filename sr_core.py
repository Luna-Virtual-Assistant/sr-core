import speech_recognition as sr

def start_sr():
    print("Luna is listening...")
    recognizer = sr.Recognizer()

    while(True):
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)

                audio = recognizer.listen(source)

                command = recognizer.recognize_google(audio, language="pt-BR", key=None, show_all=False)
                command = command.lower()

                print(f"Command: {command}")

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("unknown error occurred")


if __name__ == "__main__":
    start_sr()