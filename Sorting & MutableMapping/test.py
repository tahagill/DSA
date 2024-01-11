from flight import  FlightDatabase

# Example usage
flight_db = FlightDatabase()

# Read flights from a file
flight_db.read_flights_from_file("flights.csv")

# Display all flights in the database
flight_db.display_all_flights()



# Example usage of additional methods
print("\nChecking seat availability for UA789 on 09May at 14:45 (First Class):")
print(f"Available seats: {flight_db.check_seat_availability('LAX', 'SFO', '09May', '14:45', 'first')}")

print("\nBooking a seat for UA789 on 09May at 14:45 (Coach Class):")
if flight_db.book_seat('LAX', 'SFO', '09May', '14:45', 'coach'):
    print("Booking successful.")
else:
    print("Booking failed. No available seats.")

print("\nCancelling a booking for UA789 on 09May at 14:45 (First Class):")
if flight_db.cancel_booking('LAX', 'SFO', '09May', '14:45', 'first'):
    print("Cancellation successful.")
else:
    print("Cancellation failed. No booking found.")

print("\nCalculating flight duration for UA789 on 09May at 14:45:")
duration = flight_db.calculate_flight_duration('LAX', 'SFO', '09May', '14:45')
print(f"Flight duration: {duration}")
