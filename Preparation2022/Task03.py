


Person(name,reservations):
    make_reservation(start_date,end_date,room):
        start_date
        end_date


Reservation(room,start_date,end_date):

Room(room_number):


make_reservation('10.12.2022', '12.12.2022', '301')


# Anagram
def anagram(word1, word2):
    f1 = frequency_char(word1)
    f2 = frequency_char(word2)

    return f1 == f2


print(anagram("listen", "silent"))

Frage
3
Vollständig
Erreichbare
Punkte: 9, 00
Frage
markieren
Fragetext
Betrachten
Sie
das
folgende
UML - Diagramm, in dem
eine
Person
null
oder
mehr
Reservierungen
vornehmen
kann
und
eine
Reservierung
ein
einzelnes
Zimmer
bucht.

Implementieren
Sie
die
verschiedenen
Klassen
sowie
die
Methode
make_reservation()
der
Klasse
Person.Diese
Methode
muss
eine
reservation - Objekt
anlegen
und
dann
die
Verbindungen
zwischen
den
person -, reservation - und
room - Objekten
herstellen.Es
ist
nicht
notwendig
zu
prüfen, ob
das
room - Objekt
zum
gewünschten
Zeitraum
bereits
reserviert
ist
oder
ob
die
Daten
relevant
sind.Sie
können
die
Darstellung
der
Daten
frei
wählen
Antworttext


# classic solution
def frequency_char(word):
    res = {}
    for c in word:
        if c in res:
            res[c] += 1
        else:
            res[c] = 1
    return res


# dictionary comprehension
def frequency_char2(word):
    res = {c: 0 for c in word}
    for c in word:
        res[c] += 1
    return res


# using get method of dictionary
def frequency_char3(word):
    res = {}
    for c in word:
        # the method get returns res[c] if this value exists, 0 otherwise
        res[c] = res.get(c, 0) + 1
    return res


print(frequency_char("the aviator"))
# displays {'t': 2, 'h': 1, 'e': 1, ' ': 1, 'a': 2, 'v': 1, 'i': 1, 'o': 1, 'r': 1}


Antwortdateien
Feedback


class Room:

    def __init__(self, room_number):
        self.room_number = room_number

    def __str__(self):
        return "Room[number=" + str(self.room_number) + "]"


class Reservation:
    def __init__(self, start_date: str, end_date: str, room: Room) -> None:
        self.start_date = start_date
        self.end_date = end_date
        self.room: Room = room

    def __str__(self):
        return "Reservation[start_date=" + self.start_date + ",end_date=" + self.end_date + ",room=" + str(
            self.room) + "]"


class Person:

    def __init__(self, name):
        self.name = name
        self.reservations = []

    def make_reservation(self, start_date: str, end_date: str, room: Room) -> None:
        self.reservations.append(Reservation(start_date, end_date, room))

    def __str__(self):
        output: str = 'Person[name=' + self.name + ",reservations=["
        for inx, reservation in enumerate(self.reservations):
            output += "reservation=" + str(reservation)
            if inx < len(self.reservations) - 1:
                output += ","
        output += "]]"
        return output


def main():
    hans = Person("Hans")
    room_1 = Room(1)
    room_2 = Room(2)
    hans.make_reservation("10.11.2021", "11.11.2021", room_1)
    print(hans)
    hans.make_reservation("12.11.2021", "13.11.2021", room_2)
    print(hans)


if __name__ == "__main__":
    main()