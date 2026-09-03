class Room:
    def __init__(self,room_id,roomNumber,roomType,price):
        self._room_id = room_id
        self._roomNumber = roomNumber
        self._roomType = roomType
        self._price = price
        self._status = "available"

    def is_Available(self):
        return self._status == "available"

    def set_status(self,new_status):
        self._status = new_status

    def __str__(self):
        return f"Room {self._room_id} {self._roomNumber} ({self._roomType}) {self._price}kip/nige {self._status}"

    def get_price(self):
        return self._price


room = Room("roo1", "101", "standard", 150000)
print(room)

room.set_status("occupied")
print(room.is_Available())

        