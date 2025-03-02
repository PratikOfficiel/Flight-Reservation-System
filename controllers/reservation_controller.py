# Add the project root directory to sys.path
import os
import sys
import heapq
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from datetime import datetime
import mysql.connector

from models.flight import Flight
from models.flight_reservation import FlightReservation
from repositories.flight_repository import FlightRepository
from repositories.reservation_repository import ReservationRepository


__all__ = ['ReservationController']
class ReservationController:
    def __init__(self):
        # Establish a database connection
        self.connection = mysql.connector.connect(
            host="localhost",
            user="educative",
            password="secret",
            database="flight"
        )

        self.flight_repo = FlightRepository()
        self.reservation_repo = ReservationRepository()

    # A helper function to create Flight objects out of database tuples
    def create_flight_object(self, flight_data):
        # Reorder tuple to match the Flight initializer
        reordered_flight_data = flight_data[1:] + (flight_data[0],)
        return Flight(*reordered_flight_data)

    def view_reservations(self, user):
        print("In the function View Reservations:")
        reservations = self.reservation_repo.get_reservations_by_user(user)
        if not reservations :
            print("No reservations found for you")
            return
        for reservation in reservations:
            print(reservation)

    def cancel_reservation(self,user):

        reservation_number = input("Please enter the reservation number to cancel: ")

        if not reservation_number:
            print("Reservation number is required to cancel the reservation")
            return
        
        user_reservation = self.reservation_repo.get_reservations_by_user(user)

        if reservation_number not in user_reservation:
            print(f"User {user.username} is not authorized to cancel this reservation: {reservation_number}")
            return
        
        try:
            self.reservation_repo.cancel_reservation(reservation_number)
            print(f"Reservation {reservation_number} is successfully cancelled")
        except Exception as e:
            print(f"Error cancelling reservation : {e}")


    def process_payment(self, user, price):
        print(f"Processing payment for {user.username} for total price of: ${price}")
        return
    
    def make_reservation(self, user, direct_flight=None, itinerary=None):
        print("Initiating reservation process...")
        num_seats = int(input("How many seats do you want to book?: "))

        if direct_flight:
            available_seats = direct_flight.get_available_seats()
            if num_seats > available_seats:
                print(f"Sorry, only {available_seats} seats available for this flight.")
                return 

            total_price = float(direct_flight.get_ticket_price())*num_seats
            print(f"Total price for {num_seats} seat(s) is: Rs{total_price}")

            self.reservation_repo.create_reservation(user, flight_no=direct_flight.get_flight_no(), seats=num_seats, creation_date=datetime.now(), payment_amount=total_price)
            
            print(f"Reservation for flight {direct_flight.get_flight_no()} made successfully.")
            
        elif itinerary:
            
            total_price = 0
            all_available = True

            for flight in itinerary:

                available_seats = flight.get_available_seats()
                if num_seats > available_seats:
                    print(f"Sorry, only {available_seats} seats available for flight {flight.get_flight_no()}")
                    all_available = False
                    break
                total_price += float(flight.get_ticket_price())* num_seats

            if not all_available:
                return

            print(f"Total price for {num_seats} seat(s) across the itinerary is: Rs{total_price}")

            for flight in itinerary:
                self.reservation_repo.create_reservation(user, flight_no=flight.get_flight_no(), seats=num_seats, creation_date=datetime.now(), payment_amount=float(flight.get_ticket_price())*num_seats)
            
            print("Itinerary reservation made successfully.")
        return

    def search_flights(self,user):
        date = input("Flying Date (YYYY-MM-DD): ")
        departure_airport = input("Origin airport: ")
        destination_airport = input("Destination Airport: ")

        flights, itineraries = self.flight_repo.find_flights(date, departure_airport, destination_airport)

        shortest_flight=None
        dis_shortest_flight = float('inf')
        dis_shortest_itinerary = float('inf')
        shortest_itinerary = None

        for flight in flights:
            flight_obj = self.create_flight_object(flight)
            if flight_obj.get_distance_km() < dis_shortest_flight:
                dis_shortest_flight = flight_obj.get_distance_km()
                shortest_flight = flight_obj
        
        for itinerary in itineraries:

            itinerary_flights = [self.create_flight_object(flight) for flight in itinerary]
            total_dis = sum(flight.get_distance_km() for flight in itinerary_flights)
            
            if total_dis<dis_shortest_itinerary:
                dis_shortest_itinerary = total_dis
                shortest_itinerary = itinerary_flights
        
        if shortest_itinerary:
            print("\n\nShortest Itinerary found:")
            total_price = 0
            for flight in shortest_itinerary:
                price = flight.get_ticket_price()
                if price:
                    total_price += float(price)
                    print(flight)
                    print(price, "$")
            print(f"Total ticket price for the itinerary: {total_price} \n")
        else:
            print("No itineraries found.")

        if shortest_flight:
            print(f"\n\nShortest Direct Flight: {shortest_flight}")
            print(f"Ticket price: ", shortest_flight.get_ticket_price(), "$")
        else:
            print("No direct flights found. \n")

        cheapest_option = self._find_cheapest_route((flights,itineraries), departure_airport, destination_airport)

        if cheapest_option:
            print("Cheapest flight or itinerary found: ")
            for flight in cheapest_option:
                print(flight)
        else:
            print("No available flights or itinerary found")

        self._handle_user_choice(user, shortest_itinerary, shortest_flight, cheapest_option)


    def _find_cheapest_route(self, flight_or_itineraries, departure_airport, destination_airport):
        graph = {}

        flights, itineraries = flight_or_itineraries

        for flight in flights:
            flight_obj = self.create_flight_object(flight)
            dep_airport = flight_obj.get_dep_port()
            arr_airport = flight_obj.get_arri_port()
            price = flight_obj.get_ticket_price()

            if dep_airport not in graph:
                graph[dep_airport] = []
            graph[dep_airport].append((arr_airport, price, flight))

        for itinerary in itineraries:
            itinerary_obj = [self.create_flight_object(flight) for flight in itinerary]
            dep_airport = itinerary_obj[0].get_dep_port()
            arr_airport = itinerary_obj[-1].get_arri_port()
            total_price = sum(float(flight.get_ticket_price()) for flight in itinerary_obj)

            if dep_airport not in graph:
                graph[dep_airport] = []
            
            graph[dep_airport].append((arr_airport, total_price, itinerary_obj))


        pq = [(0, departure_airport, [])]
        visited = {}

        while pq:
            current_cost, current_airport, route = heapq.heappop(pq)

            if current_airport == destination_airport:
                return route
            
            if current_airport in visited and current_cost >= visited[current_airport]:
                continue

            visited[current_airport] = current_cost

            for neighbor_airport, flight_price, flight_data in graph.get(current_airport, []):
                new_cost = current_cost + flight_price
                new_route = route + [flight_data]

                heapq.heappush(pq, (new_cost, neighbor_airport, new_route))

        
        return None


    def _handle_user_choice(self, user, shortest_itinerary, shortest_flight, cheapest_option):
        print("Select one of the following route")

        if shortest_itinerary:
            print("1. Shortest Itinerary")
        if shortest_flight:
            print("2. Shortest Direct Flight")
        if cheapest_option:
            print("3. Cheapest Option")

        choice = input("Enter the number of your choice (1/2/3): ")

        if choice=="1" and shortest_itinerary:
            self.make_reservation(user,itinerary = shortest_itinerary)
        elif choice=="2" and shortest_flight:
            self.make_reservation(user, direct_flight=shortest_flight)
        elif choice=="3" and cheapest_option:
            self.make_reservation(user, itinerary=cheapest_option)
        else:
            print("Invalid choice or option not available.")
        