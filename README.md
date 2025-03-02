# Flight Booking and Management System

## Overview
The **Flight Booking and Management System** is a CLI application that allows users to book flights, manage their bookings, and enables admin users to manage flight schedules. This system simplifies the process of flight booking and enhances the user experience by providing an intuitive interface for both passengers and administrators.

## Features

### User Features:
- **Flight Search**: Users can search for available flights based on the departure and destination cities, travel dates, and other criteria.
- **Flight Booking**: Users can select available flights, choose seat preferences, and proceed with payment for booking.
- **Booking Management**: Users can view, modify, or cancel their bookings.

### Admin Features:
- **Flight Management**: Admins can add, update, or delete flight schedules.

### System Features:
- **All Possible Routes**: System can generate all possible routes between two destinations with max K stops.
- **Cheapest Route**: System can find cheapest route among all direct/indirect routes

## Technologies Used

- **Backend**:
  - Python

- **Database**:
  - MySQL

## Getting Started

### Prerequisites
Make sure you have the following installed on your system:


### Clone the Repository

To get started with the project, first, clone the repository to your local machine:

```bash
git clone https://github.com/PratikOfficiel/Flight-Reservation-System.git
```
Change Directory and create a virtual env:

```bash
cd Flight-Reservation-System
python -m venv venv
source venv/bin/activate
```
Install required packages:
```bash
pip install -r requirements.txt
```
Set up .env file and create the corresponding database then run these files:
```bash
python3 repositories/tables.py
python3 repositories/seed.py
```

You are ready run run the code:
```bash
python3 main.py
```

