
import random

# ENVIRONMENT
# Ask the user for the initial condition of each room.
environment = {}

for room in ["A", "B", "C"]:
    while True:
        state = input(
            f"Is room {room} Dirty or Clean? "
        ).strip().capitalize()

        if state in ["Dirty", "Clean"]:
            environment[room] = state
            break
        else:
            print("Invalid input. Please enter Dirty or Clean.")


# Function to check whether a room is dirty.
def is_dirty(room):
    return environment[room] == "Dirty"


# Function to clean a room.
def clean_room(room):
    environment[room] = "Clean"
    print(f"Room {room} has been cleaned.")


# VACUUM AGENT

class VacuumAgent:
    def __init__(self):
        # The agent starts in room A.
        self.location = "A"

    # Display a text-based grid of all rooms.
    def display_grid(self):
        print("\n--- ROOM GRID ---")

        for room in ["A", "B", "C"]:
            if room == self.location:
                agent_symbol = "[A-Agent]"
            else:
                agent_symbol = "         "

            if environment[room] == "Dirty":
                room_symbol = "[D-Dirty]"
            else:
                room_symbol = "[C-Clean]"

            print(f"Room {room}: {room_symbol} {agent_symbol}")

        print("-----------------\n")

    # Move to a randomly selected room.
    def move(self, target_room):
        self.location = target_room
        print(f"Moving to room {self.location}")

    # Decide whether to clean or move.
    def perceive_and_act(self):
        print(f"Agent is currently in room {self.location}")

        # Rule 1: Clean the current room if it is dirty.
        if is_dirty(self.location):
            clean_room(self.location)

        # Rule 2: If the current room is clean,
        # randomly choose a dirty room to visit.
        else:
            dirty_rooms = [
                room for room in environment
                if is_dirty(room)
            ]

            if dirty_rooms:
                next_room = random.choice(dirty_rooms)
                self.move(next_room)

            else:
                print("All rooms are clean! Agent is idle.")


# RUN SIMULATION

agent = VacuumAgent()

while True:
    try:
        steps = int(
            input("\nHow many steps should the agent run? ")
        )

        if steps > 0:
            break
        else:
            print("Please enter a positive number.")

    except ValueError:
        print("Invalid input. Enter a whole number.")


# Execute the simulation.
for step in range(1, steps + 1):
    print(f"\nSTEP {step} ")

    # Show the agent and room conditions before acting.
    agent.display_grid()

    # Let the agent perceive and act.
    agent.perceive_and_act()

    # Show the updated environment.
    print("Environment state:", environment)

    # Stop if all rooms are clean.
    if all(
        state == "Clean"
        for state in environment.values()
    ):
        print("\nAll rooms are clean! Agent is idle.")
        agent.display_grid()
        break

print("\nSimulation finished.")