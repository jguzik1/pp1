ICAO = {
    "a":"Alfa",
    "b":"Bravo",
    "c":"Charlie",
    "d":"Delta",
    "e":"Echo",
    "f":"Foxtrot",
    "g":"Golf",
    "h":"Hotel",
    "i":"India",
    "j":"Juliett",
    "k":"Kilo",
    "l":"Lima",
    "m":"Mike",
    "n":"November",
    "o":"Oscar",
    "p":"Papa",
    "q":"Quebec",
    "r":"Romeo",
    "s":"Sierra",
    "t":"Tango",
    "u":"Uniform",
    "v":"Victor",
    "w":"Whiskey",
    "y":"Yankee",
    "z":"Zulu",
    " ": ""
}
with open("08-DictionariesStacksAndQueues/ICAO.txt","w",encoding="UTF-8") as f:
    a = ""
    for item in ICAO:
        a = a + item + " " + ICAO[item] + "\n"

    f.write(a)