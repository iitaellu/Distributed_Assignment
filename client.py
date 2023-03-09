#https://www.youtube.com/watch?v=M1Tm4hnvEjA

import xmlrpc.client
import xml.etree.ElementTree as ET

def main():
    proxy = xmlrpc.client.ServerProxy("http://localhost:3000/")
    userInput = -1
    while(userInput != "0"):
        print("\nMenu options:")
        print("1: Add note")
        print("2: Print all notes")
        print("3: Get contents by given topic")
        print("0: Quit")
        userInput = input("What do you want to do? ")
        if userInput == "1":
            topic = input("Topic of note: ")
            note = input("Header of topic: ")
            texts = input("Note: ")
            result = proxy.note(topic, note, texts)
            print(f"{result}")
        if userInput == "2":
            message = proxy.print_all()
            print(message)
        if userInput == "3":
           topic = input("Give topic you want to find: ")
           messages = proxy.findTopic(topic)
           for msg in messages:
               print(msg)
        if userInput == "0":
            print("Ending software...")
        #if userInput != "0" or "1" or "2" or "3":  
         #   print("\nGive number 1,2,3 or 0. Try again\n--------------------------------")

    

main()
