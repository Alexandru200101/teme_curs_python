class Room:
    def __init__(self, number, available=True):
        self.number = number
        self.available = available

    def __str__(self):
        status = "Disponibilă" if self.available else "Ocupată"
        return f"Camera {self.number}: {status}"


class Hotel:
    def __init__(self, rooms=None):
        # rooms e o listă de obiecte Room
        self.rooms = rooms if rooms is not None else []

    def check_in(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                if room.available:
                    room.available = False
                    return f"Ați făcut check-in în camera {room_number}."
                else:
                    return f"Camera {room_number} este deja ocupată."
        return f"Camera {room_number} nu există."

    def check_out(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                if not room.available:
                    room.available = True
                    return f"Ați făcut check-out din camera {room_number}."
                else:
                    return f"Camera {room_number} este deja liberă."
        return f"Camera {room_number} nu există."

    def available_rooms(self):
        disponibile = [room.number for room in self.rooms if room.available]
        if disponibile:
            return f"Camere disponibile: {', '.join(map(str, disponibile))}"
        else:
            return "Nu există camere disponibile."


# Exemplu de utilizare
if __name__ == "__main__":
    camere = [Room(101), Room(102), Room(103)]
    hotel = Hotel(camere)

    print(hotel.available_rooms())
    print(hotel.check_in(101))
    print(hotel.available_rooms())
    print(hotel.check_in(101))
    print(hotel.check_out(101))
    print(hotel.available_rooms())
