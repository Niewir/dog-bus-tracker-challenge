MAX_SEATS = 5

# dictionary holding all current passengers on bus
bus = {
    "Seat 2": {"name": "Tony", "breed": "golden", "pickup": "9:00", "dropoff": "9:30"},
    "Seat 4": {"name": "Robin", "breed": "poodle", "pickup": "9:00", "dropoff": "9:50"},
    "Seat 3": {"name": "Jerry", "breed": "shihTzu", "pickup": "9:00", "dropoff": "9:30"},
    "Seat 1": {"name": "Linda", "breed": "wheaten", "pickup": "9:00", "dropoff": "10:00"},
}

# print the starting roster showing each passenger's seat, name, and pickup time
def roster_pickup():
    for key, value in bus.items():
        print(key, "→", value["name"], "→", value["pickup"], "Pickup")
    return
print("Starting bus roster is:")
roster_pickup()

# identify which seats are taken and determine which seat is available for new passenger
taken_seats = [int(seat.split()[1]) for seat in bus.keys()]
for seat in range(1, MAX_SEATS + 1):
    if seat not in taken_seats:
        next_seat = seat
        break

# add new passenger to bus at the available seat
bus[f"Seat {next_seat}"] = {
    "name": "Brent",
    "breed": "bulldog,",
    "pickup": "9:00",
    "dropoff": "9:30",
}

# print an updated version of the starting roster which includes the new added passenger and their seat number
print("\nUpdated roster after pickup:")
roster_pickup()

# ask for user input to determine which passenger has to leave early, then remove them from the bus dictionary
leaving = input("Who is getting off the bus early? Enter their name: ")
for seat, pet in bus.items():
    if pet["name"].strip() == leaving.strip():
        print(f"{pet['name']} has gone home early." )
        del bus[seat]
        break

# a list of the passengers remaining after removal, and their dropoff times
def roster_dropoff():
    for key, value in bus.items():
        print(key, "→", value["name"], "→", value["dropoff"], "Dropoff")
    return
print("\nRemaining pets and their dropoff times:")
roster_dropoff()