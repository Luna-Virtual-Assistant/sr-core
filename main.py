from mqtt_connection.start import start
from app.core import CommandRecognizer

if __name__ == "__main__":
    recognizer = CommandRecognizer()
    recognizer.recognize_command()