'''import pyttsx3
engine = pyttsx3.init()
def speech_text(text):
    engine.say(text)
speech_text("hello, I am honey")
speech_text("What's, your plan Today")
engine.runAndWait()

import pyttsx3
engine = pyttsx3.init()
def speech_text(text):
    print(text)
    engine.say(text)
speech_text("hello, I am honey")
speech_text("What's, your plan today")
engine.runAndWait()


import pyttsx3
engine = pyttsx3.init()
def speech_text(text):
    engine.say(text)

user_text = input("Enter your message: ").lower() 

name = "User"
if "my name is" in user_text:
    name = user_text.split("my name is")[-1].strip()
elif "name is" in user_text:
    name = user_text.split("name is")[-1].strip()

if user_text in ["hi", "hello", "hey"]:
    response = "Hello! How can I help you?"
elif "name" in user_text:
    response = f"Hello {name}, how can I help you?"
else:
    response = "sorry, I didn't understand that."
print(response)
speech_text(response)
engine.runAndWait()'''





import pyttsx3
engine=pyttsx3.init()
def speech_text(text):
    print(text)
    engine.say(text)
def Swiggy_help():
    print("Welcome to Swiggy Help Center")
    engine.say("Welcome to Swiggy Help Center")
    user_choice=int(input("Enter:\n1.Order not delivered\n2.Wrong order\n3.Payment issue\n4.Cancel order\n5.Exit\n"))
    if user_choice==1:
        response="Sorry, your order is delayed. Please wait or contact delivery partner."
    elif user_choice==2:
        response="You received a wrong order. You can request a refund or replacement."
    elif user_choice==3:
        response="If payment was deducted, it will be refunded in 3 to 5 days."
    elif user_choice==4:
        response="Your cancellation request is being processed."
    elif user_choice==5:
        response="Thank you for using Swiggy Help Center"
    else:
        response="Invalid choice"
    speech_text(response)
    engine.runAndWait()
Swiggy_help()


