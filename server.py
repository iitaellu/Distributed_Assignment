#https://www.youtube.com/watch?v=M1Tm4hnvEjA
#https://docs.python.org/3/library/xmlrpc.client.html#module-xmlrpc.client
#https://docs.python.org/3/library/xml.etree.elementtree.html

from xmlrpc.server import SimpleXMLRPCServer
import datetime
import xml.etree.ElementTree as ET

def note(topic, header, text):
    timestamp = datetime.datetime.today()
    message = xml_data(topic, header, text, timestamp)
    return "\n--------------------------------\n"+topic +"\n" + header + "\n" + text + "\n" + str(timestamp) + "\n--------------------------------\n" + message + "\n"

def xml_data(topic, header, texti, time):
    tree = ET.parse('db.xml')
    root = tree.getroot()
    for child in root.findall('topic'):
        name = child.get('name')
        if(name == topic):
            note = ET.Element("note")
            note.set('name', header )
            newN=ET.Element("text")
            newN.text = texti
            timestamp = ET.Element("timestamp")
            timestamp.text = str(time)
            note.append(newN)
            note.append(timestamp)
            child.append(note)
            tree.write("db.xml")
            return "\nText added to topic\n--------------------------------"


    newT=ET.Element("topic")
    newT.set('name', topic)
    
    note = ET.Element("note")
    note.set('name', header)
    newN=ET.Element("text")
    newN.text = texti
    timestamp = ET.Element("timestamp")
    timestamp.text = str(time)
    
    note.append(newN)
    note.append(timestamp)
    newT.append(note)
    root.append(newT)
    tree.write("db.xml")
    return "\nNew topic added\n--------------------------------"


def print_all():
    tree = ET.parse('db.xml')
    root = tree.getroot()
    for child in root.findall('topic'):
        print("\nTopic: "+ child.get("name"))
        for no in child.findall('note'):
            print("Note: " + no.get('name'))
            print("Text: " + no.find("text").text)
            print("Time: " + no.find("timestamp").text+"\n--------------")
    return "\nPrinted to server side\n--------------------------------"

def findTopic(topic):
    tree = ET.parse('db.xml')
    root = tree.getroot()
    lst = []
    for child in root.findall('topic'):
        print(child.attrib)
        name = child.get('name')
        if(name == topic):
            print("\nTopic: "+ child.get("name"))
            for no in child.findall('note'):
                print("Note: " + no.get('name').strip())
                print("Text: " + no.find("text").text.strip())
                print("Time: " + no.find("timestamp").text.strip()+"\n--------------")
                message = "\nNote: " + no.get('name').strip() + "\nText: " + no.find("text").text.strip() + "\nTime: " + no.find("timestamp").text.strip()+"\n--------------"
                lst.append(message)
            return lst
    lst.append("\nCould't find topic\n--------------------------------")
    return lst

server = SimpleXMLRPCServer(("localhost", 3000))
print("Listening on port 3000...")
server.register_function(note, "note")
server.register_function(print_all, "print_all")
server.register_function(findTopic, "findTopic")
server.serve_forever()
