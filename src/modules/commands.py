import os
import wikipedia
import webbrowser
from random import random
from datetime import datetime

def joke():
    speak("ok")
    a="Why do we tell actors to break a leg?"+"  Because every play has a cast"
    b="What do dentists call their x-rays?"+"  Tooth pics!"
    c="Do you want to hear a construction joke?"+" Sorry, I\'m still working on it."
    d="Why do ducks have feathers?"+" To cover their butt quacks!"
    e="What does a nosey pepper do?"+" It gets jalapeño business. "
    f="Why did the bullet end up losing his job?"+" He got fired."
    g="How do you measure a snake?"+" In inches—they don\'t have feet."
    lst1=[a,b,c,d,e,f]
    joke=random.choice(lst1)
    print(joke)
    speak(joke)
    speak("ha ha ha ha ha")

def getResult():
    if "wikipedia"in query:
        print("Searching in wikipeia")
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=1)
        return results

    elif ("tell me a joke" in query) or ("tell joke" in query) or ("joke" in query):
        return joke()

    elif"hai"in query:
        return "hi master"

    elif "open youtube"in query:
        webbrowser.open("youtube.com")
        return "opening youtube"

    elif "open google"in query:
        webbrowser.open("google.com")
        return "opening Google"

    elif "open geeks for geeks"in query:
        webbrowser.open_new_tab("geeksforgeeks.org")
        return "opening geeks for geeks "
        
    elif "play music" in query:
        print("opening music player")
        music="C:\\Users\\home\\Desktop\\songs"
        songs=os.listdir(music)
        print(songs)
        a=random.choice(songs)
        print(a)
        os.startfile(os.path.join(music,a))
        return "Playing Music"

    elif "open whatsapp"in query:
        webbrowser.open("web.whatsapp.com")
        return "Opening Whatsapp"

    elif "play movie"in query:
        speak("playing a movie")
        kmovie="C:\\Users\\home\\Desktop\\sanjay"
        movie="C:\\Users\\home\\Desktop\\movie\\movie"
        
        k=[kmovie,movie]
        c=random.choice(k)
        film=os.listdir(c)
        print(film)
        b=random.choice(film)
        print(b)
        os.startfile(os.path.join(movie,b))
        return "Showing Movies"

    elif "open chrome"in query:
        codepath="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe "
        os.startfile(codepath)
        return "opening chrome"

    elif "time now"in query:
        time=datetime.datetime.now().strftime("%H:%M")
        return time

    elif "nothing"in query:
        return "Bye master"
        exit()

    elif "search in youtube"in query:
        print("what to search in youtube")
        search=mycommand()
        webbrowser.open("https://www.youtube.com/results?search_query="+search)
        return "Search Result For "+search

    elif"play in youtube" in query:
        playinyt()
        return "Playing On Youtube"

    elif"search in google"in query:
        print("what to search in google")
        search=mycommand()
        print("searching for"+search)
        webbrowser.open("https://www.google.com/search?q="+search)
        return "Search Result From Google"