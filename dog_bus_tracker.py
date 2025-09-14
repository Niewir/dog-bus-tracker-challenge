import random
import threading
from time import sleep
from datetime import datetime, timedelta

# setup virtual time that runs 5 minutes for each .5 seconds real time
virtual_time = datetime.now().replace(hour=8, minute=40, second=0, microsecond=0)

def run_clock():
    global virtual_time
    while True:
        sleep(0.5)
        virtual_time += timedelta(minutes=10)

thread = threading.Thread(target=run_clock, daemon=True)
thread.start()

# random seat assignment for each dog
seat_assign = random.sample(range(1, 9), 8)

# list of dictionaries holding each dog's information
dog_roster = [
{"seat": seat_assign[0], "name": "Tony,", "breed": "golden retriever,",
 "pickup": datetime.now().replace(hour=9, minute=0, second=0, microsecond=0),
 "dropoff": datetime.now().replace(hour=9, minute=30, second=0, microsecond=0)},
{"seat": seat_assign[1], "name": "Robin,", "breed": "poodle,",
 "pickup": datetime.now().replace(hour=9, minute=10, second=0, microsecond=0),
 "dropoff": datetime.now().replace(hour=9, minute=50, second=0, microsecond=0)},
{"seat": seat_assign[5], "name": "Jerry,", "breed": "shihTzu,",
 "pickup": datetime.now().replace(hour=9, minute=20, second=0, microsecond=0),
 "dropoff": datetime.now().replace(hour=9, minute=30, second=0, microsecond=0)},
{"seat": seat_assign[2], "name": "Linda,", "breed": "wheaten terrier,",
 "pickup": datetime.now().replace(hour=10, minute=0, second=0, microsecond=0),
 "dropoff": datetime.now().replace(hour=10, minute=30, second=0, microsecond=0)},
{"seat": seat_assign[3], "name": "Jim,", "breed": "golden retriever,",
 "pickup": datetime.now().replace(hour=10, minute=0, second=0, microsecond=0),
 "dropoff": datetime.now().replace(hour=11, minute=0, second=0, microsecond=0)},
{"seat": seat_assign[6], "name": "Brent,", "breed": "poodle,",
 "pickup": datetime.now().replace(hour=10, minute=20, second=0, microsecond=0),
 "dropoff": datetime.now().replace(hour=11, minute=30, second=0, microsecond=0)},
{"seat": seat_assign[4], "name": "Bones,", "breed": "bulldog,",
 "pickup": datetime.now().replace(hour=10, minute=30, second=0, microsecond=0),
 "dropoff": datetime.now().replace(hour=11, minute=30, second=0, microsecond=0)},
{"seat": seat_assign[7], "name": "Arnold,", "breed": "bulldog,",
 "pickup": datetime.now().replace(hour=11, minute=10, second=0, microsecond=0),
 "dropoff": datetime.now().replace(hour=11, minute=30, second=0, microsecond=0)},
]

# roster printing the seat number, name, and pickup time of each dog on the bus schedule
print("Full roster (name and pickup time):")
for dog in dog_roster:
    print(f"Seat: {dog["seat"]}, {dog["name"]} Pickup at: {dog["pickup"]}")

# empty list for actual bus riders at a given time, starts empty and fills when virtual time reaches pickup/dropoff
bus = []

# loop that picks up and drops off dogs based on the current time and their pickup/dropoff values
while virtual_time < virtual_time.replace(hour=12, minute=0, second=0, microsecond=0):
    for dog in dog_roster:
        if virtual_time == dog["pickup"]:
            bus.append(dog)
            print(f"{dog['name']} pickup")
        elif virtual_time == dog["dropoff"]:
            if dog in bus:
                bus.remove(dog)
                print(f"{dog['name']} dropoff")
    sleep(0.5)