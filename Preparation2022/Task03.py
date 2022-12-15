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