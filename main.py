import os
import sys

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controllers.user_controller import UserController
from controllers.flight_controller import FlightController
from controllers.reservation_controller import ReservationController

def main():
    user_controller = UserController()

    while (user_controller.current_user == None):

        print("\n1. Login\n2. Signup\n3. Exit")
        option = input("Select an option: ")

        if option == "1":
            user_controller.login()
        elif option == "2":
            if (user_controller.signup()):
                user_controller.login()

        elif option == "3":
            return
        else:
            print("Please select a valid input")

    if (user_controller.current_user):

        user = user_controller.current_user

        flightController = FlightController()
        reservationController = ReservationController()

        while True:

            print("1. Search/Reserve flights")
            print("2. View reservations")
            print("3. Cancel the reservation")
            print("4. Add the flight (for admin only)")
            print("5. Cancel the flight (for admin only)")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                reservationController.search_flights(user)
            elif choice == "2":
                reservationController.view_reservations(user)
            elif choice == "3":
                reservationController.cancel_reservation(user)
            elif choice == "4":
                flightController.add_flight(user)
            elif choice == "5":
                flightController.delete_flight(user)
            elif choice == "6":
                break
            else:
                print("Invalid choice, try again.")

    return


if __name__ == "__main__":
    main()
