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

### Constraints on System:

#### Departure Date only available b/w 2024-01-01 to 2024-12-31

#### Available Airport Codes for Flight search:

- ABE
- ABQ
- ABR
- ABY
- ACT
- ACV
- ADK
- ADQ
- AEX
- AGS
- AKN
- ALB
- AMA
- ANC
- APN
- ASE
- ATL
- ATW
- AUS
- AVL
- AVP
- AZO
- BDL
- BET
- BFL
- BGM
- BGR
- BHM
- BIL
- BIS
- BJI
- BLI
- BMI
- BNA
- BOI
- BOS
- BPT
- BQK
- BRD
- BRO
- BRW
- BTM
- BTR
- BTV
- BUF
- BUR
- BWI
- BZN
- CAE
- CAK
- CDC
- CDV
- CEC
- CHA
- CHO
- CHS
- CID
- CIU
- CLD
- CLE
- CLL
- CLT
- CMH
- CMX
- CNY
- COD
- COS
- CPR
- CRP
- CRW
- CSG
- CVG
- CWA
- DAB
- DAL
- DAY
- DCA
- DEN
- DFW
- DHN
- DIK
- DLG
- DLH
- DRO
- DSM
- DTW
- DVL
- EAU
- ECP
- EKO
- ELM
- ELP
- ERI
- ESC
- EUG
- EVV
- EWN
- EWR
- EYW
- FAI
- FAR
- FAT
- FAY
- FCA
- FLG
- FLL
- FNT
- FSD
- FSM
- FWA
- GCC
- GCK
- GEG
- GFK
- GGG
- GJT
- GNV
- GPT
- GRB
- GRK
- GRR
- GSO
- GSP
- GST
- GTF
- GTR
- GUC
- HDN
- HIB
- HLN
- HNL
- HOB
- HOU
- HPN
- HRL
- HSV
- HYS
- IAD
- IAH
- ICT
- IDA
- ILM
- IMT
- IND
- INL
- ISN
- ITH
- JAC
- JAN
- JAX
- JFK
- JLN
- JMS
- JNU
- KOA
- KTN
- LAN
- LAR
- LAS
- LAW
- LAX
- LBB
- LCH
- LEX
- LFT
- LGA
- LGB
- LIH
- LIT
- LNK
- LRD
- LSE
- LWS
- MAF
- MBS
- MCI
- MCO
- MDT
- MDW
- MEI
- MEM
- MFE
- MFR
- MGM
- MHK
- MHT
- MIA
- MKE
- MKG
- MLB
- MLI
- MLU
- MMH
- MOB
- MOT
- MQT
- MRY
- MSN
- MSO
- MSP
- MSY
- MTJ
- MYR
- OAJ
- OAK
- OGG
- OKC
- OMA
- OME
- ONT
- ORD
- ORF
- OTH
- OTZ
- PAH
- PBI
- PDX
- PHF
- PHL
- PHX
- PIA
- PIB
- PIH
- PIT
- PLN
- PNS
- PSC
- PSG
- PSP
- PUB
- PVD
- PWM
- RAP
- RDD
- RDM
- RDU
- RHI
- RIC
- RKS
- RNO
- ROA
- ROC
- ROW
- RST
- RSW
- SAF
- SAN
- SAT
- SAV
- SBA
- SBN
- SBP
- SCC
- SCE
- SDF
- SEA
- SFO
- SGF
- SGU
- SHV
- SIT
- SJC
- SJT
- SLC
- SMF
- SMX
- SNA
- SPI
- SPS
- STC
- STL
- SUN
- SWF
- SYR
- TLH
- TPA
- TRI
- TUL
- TUS
- TVC
- TWF
- TXK
- TYR
- TYS
- VEL
- VLD
- VPS
- WRG
- WYS
- XNA
- YAK
- YUM
