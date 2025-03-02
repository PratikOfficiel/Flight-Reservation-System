import os
import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.auth import CLIAuthenticator  # Authenticator for login, signup, etc.
from datetime import datetime  # Useful for working with date and time related to flight schedules

from models.flight import Flight
from repositories.flight_repository import FlightRepository

class FlightController:
    def __init__(self):
        self.flight_repository = FlightRepository()

    def add_flight(self, user):

        if not user._is_admin():
            print("Only admins can add flights")
            
        print("Add Flight: ")
        airline_code = input("Airline Code: ")
        distance_km = float(input("Distance (in km): "))
        dep_time = input("Departure Time (YYYY-MM-DD): ")
        arri_time = input("Arrival Time (YYYY-MM-DD): ")
        dep_port = input("Departure Airport Code: ")
        arri_port = input("Arrival Port Code: ")
        flight = Flight(airline_code, distance_km, dep_time, arri_time, dep_port, arri_port)
        self.flight_repository.add_flight(flight)
        print("Flight added successfully.")

    def delete_flight(self,user):
        if not user._is_admin():
            print("Only admins can cancel flights")

        flight_no = input("Flight Number: ")
        
        if self.flight_repository.delete_flight(flight_no):
            print(f"{flight_no} deleted")
        else:
            print(f"Failed to delete flight: {flight_no}")
    

    
