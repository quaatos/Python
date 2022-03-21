import webbrowser

#script asks the user were and what he want to search 
print("options are: youtube, wikipedia, google, DuckDuckGo")
options = input("where do you want to search: ")

#checks if the input is valid.
if options != "wikipedia" and options != "google" and options != "youtube" and options != "DuckDuckGo":
    print ("Enter a correct input")
    exit()

#Enter what's up on your mind
question = input("type what you want to know: ")


#code will search on one of the given websites
if options == "google":
    print ("this the result on google for:", question)
    webbrowser.open("https://google.com/search?q={}".format(question))

elif options == "youtube":
    print ("This is the result on youtube for:", question)
    webbrowser.open("https://youtube.com/search?q={}".format(question))

elif options == "wikipedia":
    print ("This is the result on wikipedia for:", question)
    webbrowser.open("https://wikipedia.org/wiki/{}".format(question))

elif options == "DuckDuckGo":
    print ("This is the result on DuckDuckGo for:", question)
    webbrowser.open("https://duckduckgo.com/?t=ffab&q={}".format(question))

#developed by Quaatos with <3
#last updated:
#3/21/2022 
#11:27 AM
