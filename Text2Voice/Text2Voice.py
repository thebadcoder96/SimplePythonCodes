import pyttsx3

#initialize object
engine = pyttsx3.init()

#Setting voice rate
crate="My voice rate is: " + str(engine.getProperty('rate')) + ". Would you like to change it?"
print(crate)
engine.say(crate)
engine.runAndWait()
inp=input().lower()

if inp=='yes':
    print("Please enter the new voice rate: ")
    engine.say("Please enter the new voice rate: ")
    engine.runAndWait()
    engine.setProperty('rate', int(input()))

#setting gender
cvoice="Would you like to change the gender of my voice?"
print(cvoice)
engine.say(cvoice)
engine.runAndWait()
inp=input().lower()

if inp=='yes':
    engine.setProperty('voice', engine.getProperty('voices')[1].id)


#Text to Speech
text="Enter the text you want me to speak: "
print(text)
engine.say(text)
engine.runAndWait()

engine.say(input())
engine.runAndWait()


