# To handle operations related to the Flight table.
import mysql.connector
from datetime import datetime, timedelta
from collections import deque
from config.database_config import get_db_connection  

class FlightRepository:
    def __init__(self):
        self.connection = get_db_connection()
        self.cursor = self.connection.cursor()

    def add_flight(self, flight):
        
        airlineCode = flight.get_airline_code()
        distance = flight.get_distance_km()
        depTime =  flight.get_dep_time()
        arrTime = flight.get_arri_time()
        depPort = flight.get_dep_port()
        arrPort = flight.get_arri_port()
        bookedSeats = flight.get_booked_seats()

        query = "INSERT INTO Flight(airline_code, distance_km, dep_time, arri_time, dep_port, arri_port) Values(%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(query,(airlineCode, distance, depTime,arrTime,depPort,arrPort))

        self.connection.commit()

        inserted_flight_no = self.cursor.lastrowid

        print(f"Flight added successfully. Flight Number: {inserted_flight_no}")
        return inserted_flight_no
    
    def delete_flight(self, flightNo):
        query = "DELETE FROM Flight where flight_no=%s"

        deleted_flight_no = self.cursor.execute(query, (flightNo, ))
        self.connection.commit()

        if self.cursor.rowcount>0:
            return True
        else:
            return False

    def _find_direct_flights(self, date, departure_airport, destination_airport):
        
        query = "SELECT * FROM Flight WHERE dep_port=%s and arri_port=%s and DATE(dep_time)=%s"
        self.cursor.execute(query, (departure_airport, destination_airport,date))
        return self.cursor.fetchall()

    def _find_itineraries(self, date, departure_airport, destination_airport, max_stops):
        
        itinerary_list = []
        queue = deque()
        queue.append((departure_airport,[],None,0))

        visited = set()

        query = "SELECT * FROM Flight WHERE dep_port=%s and DATE(dep_time)=%s"

        while queue:
            current_airport, flights_taken, last_time, stops = queue.popleft()

            if((current_airport in visited) or stops>max_stops):
                continue

            visited.add(current_airport)

            self.cursor.execute(query,(current_airport,date))
            connecting_flights = self.cursor.fetchall()

            for flight in connecting_flights:

                new_flights_taken = flights_taken + [flight]

                flight_no, airline_code, distance_km, dep_time, arri_time, dep_port, arri_port, seats = flight

                if dep_port==departure_airport and arri_port==destination_airport:
                    continue
                
                if last_time is None or (dep_time-last_time<=timedelta(hours=1)):
                    continue

                if arri_port==destination_airport:
                    itinerary_list.append(new_flights_taken)
                else:
                    queue.append((arri_port, new_flights_taken, arri_time, stops+1))

        return itinerary_list        

    def find_flights(self, date, departure_airport, destination_airport):
        max_stops = int(input("What's the maximum number of allowed stops: "))

        direct_flights = self._find_direct_flights(date, departure_airport, destination_airport)
        indirect_flights = self._find_itineraries(date, departure_airport, destination_airport, max_stops)

        return (direct_flights, indirect_flights)
        

 