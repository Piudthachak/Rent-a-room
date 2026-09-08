# Hotel Booking System (ລະບົບຈອງຫ້ອງພັກ)

ໂປຣເຈັກຝຶກຫັດ OOAD (Object-Oriented Analysis and Design) — ລະບົບຈັດການການຈອງຫ້ອງພັກ
ຂຽນດ້ວຍ Python ໂດຍໃຊ້ຫຼັກການ Object-Oriented Programming (Encapsulation, Information Expert)

## 📋 Requirement

ຮ້ານເຊົ່າຫ້ອງພັກຕ້ອງການລະບົບໃຫ້ພະນັກງານ (Staff) ສາມາດຈັດການຫ້ອງພັກ (Room) ແລະ
ຮັບການຈອງ (Booking) ຈາກແຂກ (Guest) ໄດ້. ແຂກສາມາດຈອງຫ້ອງໄດ້ໂດຍລະບຸວັນທີເຂົ້າ-ອອກ.
ຕ້ອງຈ່າຍເງິນກ່ອນຈຶ່ງຈະສາມາດ Check-in ໄດ້, ຄິດຄ່າຫ້ອງຕາມຈຳນວນຄືນທີ່ພັກ.

## 🏗️ Class Diagram

```
Guest (1) ──── (*) Booking (*) ──── (1) Room
                    │
                    │ (1)
                    ▼
                 Payment (1)

Staff (1) ──── (*) Booking
```

| Class | Attribute | Method |
|---|---|---|
| **Room** | room_id, room_number, room_type, price, status | is_Available(), set_status(), get_price() |
| **Guest** | guest_id, name, phone, bookings | makeBooking(), view_booking_history() |
| **Staff** | staff_id, name | check_in_guest(), check_out_guest() |
| **Booking** | booking_id, guest, room, staff, checkin_date, checkout_date, payment | calculate_nights(), is_paid(), get_room() |
| **Payment** | payment_id, booking, payment_type, price, paid | pay(), print_receipt() |

## 🔄 ວົງຈອນສະຖານະຫ້ອງ (Room Status Flow)

```
available → (ຈ່າຍເງິນສຳເລັດ) → occupied → (check-out) → cleaning → available
```

## 📂 ໂຄງສ້າງໂປຣເຈັກ

```
hotel-booking-system/
├── src/
│   |__rentaroom.py    # Class Room,  Class Guest ,  Class Staff, Class Booking, Class Payment
│   └── main.py        # ຈຸດເລີ່ມຕົ້ນ ທົດລອງລະບົບ
├── README.md
└── .gitignore
```

## ▶️ ວິທີ Run

```bash
cd src
python3 main.py
```

## 🎓 ຫຼັກການ OOAD ທີ່ໃຊ້ໃນໂປຣເຈັກນີ້

- **Encapsulation**: Attribute ທັງໝົດໃຊ້ `_` ນຳໜ້າ (private), ເຂົ້າເຖິງຜ່ານ Method ເທົ່ານັ້ນ
- **Information Expert**: Method ຖືກວາງໄວ້ໃນ Class ທີ່ "ຮູ້ຈັກ" ຂໍ້ມູນທີ່ຈຳເປັນທີ່ສຸດ
  (ເຊັ່ນ `calculate_nights()` ຢູ່ໃນ `Booking` ເພາະມັນຮູ້ຈັກວັນທີເຂົ້າ-ອອກ)
- **Association**: Object ອ້າງອີງເຊິ່ງກັນແລະກັນຜ່ານການເກັບ Object ໄວ້ໃນ Attribute
  (ເຊັ່ນ `Booking` ເກັບ `Room`, `Guest`, `Payment` ໄວ້)
