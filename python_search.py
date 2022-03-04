import webbrowser

#script asks the user were and what he want to search 
print("options are: youtube, wikipedia, google,")
options = input("where do you want to search: ")

#checks if the input is valid.
if options != "wikipedia" and options != "google" and options != "youtube":
    print ("Enter a correct input")
    exit()

#Enter what's up on your mind
question = input("type what you want to know: ")


#code will search on one of the given websites
if options == "google":
    print ("this the result on google for:", question)
    webbrowser.open("https://google.com/search?q={}".format(question))

if options == "youtube":
    print ("This is the result on youtube for:", question)
    webbrowser.open("https://youtube.com/search?q={}".format(question))

if options == "wikipedia":
    print ("This is the result on wikipedia for:", question)
    webbrowser.open("https://wikipedia.org/wiki/{}".format(question))


#developed by Quaatos with <3
