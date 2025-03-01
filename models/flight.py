from amadeus import Client, ResponseError

class Flight:
    def __init__(self, airline_code, distance_km, dep_time, arri_time, dep_port, arri_port, booked_seats=0,
                 flight_no=None):
        self.__flight_no = flight_no
        self.__airline_code = airline_code
        self.__distance_km = distance_km
        self.__dep_time = dep_time
        self.__arri_time = arri_time
        self.__dep_port = dep_port
        self.__arri_port = arri_port
        self.__total_seats = 50  # Set total seats to 50
        self.__booked_seats = 0  # Initialize booked seats to 0

    # Getters
    def get_flight_no(self):
        return self.__flight_no

    def get_airline_code(self):
        return self.__airline_code

    def get_distance_km(self):
        return self.__distance_km

    def get_dep_time(self):
        return self.__dep_time

    def get_arri_time(self):
        return self.__arri_time

    def get_dep_port(self):
        return self.__dep_port

    def get_arri_port(self):
        return self.__arri_port

    def get_booked_seats(self):
        return self.__booked_seats

    # Method to get the number of available seats
    def get_available_seats(self):
        return self.__total_seats - self.__booked_seats

    # Setters
    def set_flight_no(self, flight_no):
        self.__flight_no = flight_no

    def set_airline_code(self, airline_code):
        self.__airline_code = airline_code

    def set_dep_time(self, dep_time):
        self.__dep_time = dep_time

    def set_arri_time(self, arri_time):
        self.__arri_time = arri_time

    def set_dep_port(self, dep_port):
        self.__dep_port = dep_port

    def set_arri_port(self, arri_port):
        self.__arri_port = arri_port

    def set_dep_port(self, dep_port):
        self.__dep_port = dep_port

    def __repr__(self):
        return (f"Flight No: {self.__flight_no}, Airline Code: {self.__airline_code}, "
                f"Departure from: {self.__dep_port} at {self.__dep_time}, "
                f"Arrival at: {self.__arri_port} at {self.__arri_time}")

    def book_seats(num):
        available_seats = self.get_available_seats()
        if num > available_seats:
            raise Exception(f"Not enough seats available. Onlyl {self.get_available_seats()} left.")
        else:
            self.__booked_seats += num
            print(f"{num} seats(s) booked successfully")

    def get_ticket_price():
        pass

    def get_ticket_price(self):

        amadeus = Client(
            client_id="q3zb4c0LTZeJztzhS3lLqXgtaApmGq9T",
            client_secret="QCQsVn7zes3HSyIJ"
        )

        try:
            flights = amadeus.shopping.flight_offers_search.get(
                originLocationCode=self.__dep_port,
                destinationLocationCode=self.__arri_port,
                departureDate=self.__dep_time.strftime("%Y-%m-%d"),
                adults=1,
                currencyCode="INR"
            ).data

            response_one_flight = amadeus.shopping.flight_offers.pricing.post(
                flights[0]
            )

            prices = [offer['price']['total'] for offer in response_one_flight.data['flightOffers']]

            if prices:
                return prices[0]

            return None

        except ResponseError as e:
            print(f"Error fetching flight price: {e}")
            return None

    def __lt__(self, other):
        return self.get_ticket_price() < other.get_ticket_price()