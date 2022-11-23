from modules.audio import listenInput, speak, start, aboutMe
from modules.commands import getResult

if(__name__ == "__main__"):
    
    start()
    aboutMe()

    while(True):
        query = listenInput().lower()
        result = getResult(query)
        speak(result)
        print(result)