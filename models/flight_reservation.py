
from datetime import date
class FlightReservation:
    def __init__(self, reservation_number, user_id, flight, seat_count, creation_date, total_amount):
        self.__reservation_number = reservation_number
        self.__user_id = user_id
        self.__flight = flight
        self.__seat_count = seat_count
        self.__creation_date = creation_date
        self.__total_amount = total_amount

    def get_reservation_number(self):
        return self.__reservation_number

    def get_seat_count(self):
        return self.__seat_count

    def update_seat(self, seat_count):
        if self.__seat_count > 0:
            self.__seat_count = seat_count
            print(f"Seat count updated to {seat_count}.")
        else:
            print(f"Seat {seat_count} not available.")

    def __repr__(self):
        return (f"FlightReservation(reservation_number={self.__reservation_number}, "
                f"user_id={self.__user_id}, flight={self.__flight}, "
                f"seat_count={self.__seat_count}, status='{self.__status}', "
                f"creation_date='{self.__creation_date}', total_amount={self.__total_amount})")


