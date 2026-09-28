from random import randrange

class Pflanzen: 
    pflegeZustand = ["gegossen", "Bald gießen", "neu"]
    # eien Zahl zwischen 2 und 10 :
    # Einheit in Tagen
    
    def __init__(self, name, saison, pflegeZustand):
        self.name = name
        self.saison = saison
        self.pflegeZustand = pflegeZustand
        self.faelligkeit = 0
        self.naechsterTermin = randrange(2, 10, 1)
            
    def display(self):
        print(f"{self.name} + {self.saison} + {self.pflegeZustand} + {self.faelligkeit}  +  {self.naechsterTermin}")
        
    def pflegen(self): 
        a = randrange(2, 10, 1)
        
        ## Hat keinen richtigen Sinn, als die match statement zu verwenden
        ## Das könnte auch mit elif gleich funktionieren
        if self.naechsterTermin < a:
            print(" Fällig")
        else:  # <--- ELSE Beispiel
            print(" Noch nicht fällig")
                
        match self.saison:
            case "ganzjährig": 
                self.naechsterTermin = randrange(3, 5, 1)
            case "Frühjahr-Sommer": 
                self.naechsterTermin = randrange(3, 7, 1)
            case "Herbst-Winter": 
                self.naechsterTermin = randrange(5, 8, 1)
            case _: 
                print("Not vaild")

    # Falls die Datenbank größer wird. Im Mmomentan nur als Platzhalter
    def suchen(self):
        pass  # <--- PASS Beispiel (Platzhalter)


p1 = Pflanzen("Anthurium", "ganzjährig", Pflanzen.pflegeZustand[2])
p2 = Pflanzen("Pfingstrose", "Frühjahr-Sommer", Pflanzen.pflegeZustand[2])
p3 = Pflanzen("Weihnachtsstern", "Herbst-Winter", Pflanzen.pflegeZustand[2])

list = []
list.append(p1)
list.append(p2)
list.append(p3)


def showList(meine_liste=None):
    if meine_liste is None:
        meine_liste = []
        
    for pflanze in meine_liste:
        # Beispiel CONTINUE: Wenn eine Pflanze "neu" ist, überspringen wir die Anzeige
        if pflanze.pflegeZustand == "neu":
            continue  # <--- CONTINUE Beispiel
            
        pflanze.display()


# Schleife über die Pflanzenliste mit WHILE und BREAK
index = 0
while index < len(list):  # <--- WHILE Beispiel
    if index == 2:
        break  # <--- BREAK Beispiel (bricht nach der 2. Pflanze ab)
    list[index].pflegen()
    index = index + 1


# Bedingter Ausdruck (Ternary Operator / Inline IF)
# <--- BEDINGTER AUSDRUCK Beispiel
status = "Gießen nötig" if p1.naechsterTermin < 4 else "Alles gut"
print(f"Status von {p1.name}: {status}")


showList(list)

# TRY-EXCEPT Beispiel
try:  # <--- TRY-EXCEPT Beispiel
    p1.display()
except:
    print("An errro occured")