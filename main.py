import speech_recognition
import webbrowser



class Jarvis():

    def record_and_recognize_audio(*args: tuple):
        """
        Запись и распознавание аудио
        """
        recognizer = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as mic:
            recognized_data = ""

            # регулирование уровня окружающего шума
            recognizer.adjust_for_ambient_noise(mic, duration=2)

            try:
                print("Listening...")
                audio = recognizer.listen(mic, 5, 5)

            except speech_recognition.WaitTimeoutError:
                print("Can you check if your microphone is on, please?")
                return

            # использование online-распознавания через Google
            try:
                print("Started recognition...")
                recognized_data = recognizer.recognize_google(audio, language="ru").lower()

            except speech_recognition.UnknownValueError:
                pass

            # в случае проблем с доступом в Интернет происходит выброс ошибки
            except speech_recognition.RequestError:
                print("Check your Internet Connection, please")

            return recognized_data
    def open_browser(self):
        url = "https://ya.ru/"
        webbrowser.open(url=url)
        print(webbrowser.name)

    def query_in_yandex(self,query=" "):
        url = f"https://yandex.ru/search/?text={query}"
        webbrowser.open(url=url)
        print(webbrowser.name)

    def query_in_youtube(self,query):
        url = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(url=url)
        return webbrowser.name

    def execute_command_with_name(self,query):
        query.split(" ")
        if query[0]=="включи":
            Jarvis.query_in_youtube(self,query[1])
        print(query[1])
while True:
    voice_input = Jarvis().record_and_recognize_audio()
    print(voice_input)
    try:
        Jarvis.execute_command_with_name(Jarvis(),voice_input)
    except:
        pass
