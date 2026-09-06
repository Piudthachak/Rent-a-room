from datetime import date

class Room:
    def __init__(self,room_id,room_number,roomType,price):
        self._room_id = room_id
        self._room_number = room_number
        self._roomType = roomType
        self._price = price
        self._status = "available"

    def is_Available(self):
        return self._status == "available"

    def set_status(self,new_status):
        self._status = new_status

    def __str__(self):
        return f"Room {self._room_id} {self._room_number} ({self._roomType}) {self._price}kip/nige {self._status}"

    def get_price(self):
        return self._price

class Booking:
     def __init__(self, booking_id, guest, room, staff, checkin_date, checkout_date):
        self._booking_id = booking_id
        self._guest = guest
        self._room = room
        self._staff = staff        
        self._checkin_date = checkin_date
        self._checkout_date = checkout_date
        self._payment = None
        self._actual_checkout = None
        self._actual_checkin = None

     def __str__(self):
        return f"Booking {self._booking_id}: Room {self._room._room_number}, " \
               f"{self._checkin_date} to {self._checkout_date}"

     def set_actual_checkin(self, checkin_date):
         self._actual_checkin = checkin_date

     def set_payment(self, payment):
         self._payment = payment

     def is_paid(self):
         if self._payment is None:
             return False
         return self._payment._paid
     
     def set_actual_checkout(self, checkout_date):
        self._actual_checkout = checkout_date

     def calculate_nights(self):
         return (self._checkout_date - self._checkin_date).days

     def get_room(self):
         return self._room 
        

class Guest:
    def __init__(self,guest_id,name,phone):
        self._guest_id = guest_id
        self._name = name
        self._phone = phone
        self._bookings = []

    def makeBooking(self,room,checkin_date,checkout_date,staff):
        if not room.is_Available():
            print("Sorry")
            return None

        new_booking = Booking(
            booking_id=f"BK{len(self._bookings)+1:03d}",
            guest=self,
            room=room,
            staff=staff,
            checkin_date=checkin_date,
            checkout_date=checkout_date
        )
        self._bookings.append(new_booking)

        room.set_status("occupied")

        return new_booking

    def view_booking_history(self):
        for b in self._bookings:
            print(b)


class Staff:
    def __init__(self,staff_id,name):
        self._staff_id = staff_id
        self._name = name

    def check_in_guest(self, booking):
        if not booking.is_paid():
            print("ຍັງບໍ່ຈ່າຍເງິນ, ບໍ່ສາມາດ Check in ໄດ້")
            return False
        
        booking.set_actual_checkin(date.today())   # ✅ ແກ້ໃຫ້ຖືກ, ໃຊ້ checkIN
        print(f"Check in ສໍາເລັດ ຫ້ອງ{booking.get_room()._room_number}")
        return True

    def check_out_guest(self, booking):

        booking.set_actual_checkout(date.today())

        room = booking.get_room()

        room.set_status("cleaning")

        print(f"Check_out ສຳເລັດ ສຳລັບ Booking {booking._booking_id}")

    

class Payment:
    def __init__(self,payment_id, booking, payment_type):
        self._payment_id = payment_id
        self._booking  = booking
        self._payment_type = payment_type
        self._price = 0
        self._paid = False
        booking.set_payment(self)

    def pay(self, booking):
        room = booking.get_room()
        nights = booking.calculate_nights()
        self._price = room.get_price() * nights
        self._paid = True
        room.set_status("occupied")
        return True


