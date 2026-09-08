from datetime import date
from rentaroom import Room
from rentaroom import Guest
from rentaroom import Staff
from rentaroom import Payment


def main():
    # ===== ສ້າງ Object ພື້ນຖານ =====
    room1 = Room("R001", "101", "Standard", 150000)
    guest1 = Guest("G001", "ສົມສັກ", "020-1111")
    staff1 = Staff("S001", "ພະນັກງານ A")

    print("--- ສະຖານະຫ້ອງກ່ອນຈອງ ---")
    print(room1)

    # ===== 1. ຈອງຫ້ອງ =====
    print("\n--- ຈອງຫ້ອງ ---")
    booking1 = guest1.makeBooking(
        room1, date(2026, 9, 10), date(2026, 9, 13), staff1
    )
    print(booking1)
    print(room1)  # ຄາດວ່າຍັງ "available"

    # ===== 2. ຈ່າຍເງິນ =====
    print("\n--- ຈ່າຍເງິນ ---")
    payment1 = Payment("P001", booking1, "cash")
    payment1.pay(booking1)
    payment1.print_receipt()
    print(room1)  # ຄາດວ່າປ່ຽນເປັນ "occupied"

    # ===== 3. Check-in =====
    print("\n--- Check-in ---")
    staff1.check_in_guest(booking1)

    # ===== 4. Check-out =====
    print("\n--- Check-out ---")
    staff1.check_out_guest(booking1)
    print(room1)  # ຄາດວ່າປ່ຽນເປັນ "cleaning"

    # ===== 5. ເບິ່ງປະຫວັດການຈອງ =====
    print("\n--- ປະຫວັດການຈອງຂອງ ສົມສັກ ---")
    guest1.view_booking_history()


if __name__ == "__main__":
    main()
