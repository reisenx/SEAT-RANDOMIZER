# ----------------------------------------------------------------------
# File Name     : room.py
# Author        : Worralop Srichainont
# Description   : Room class definition for the seating arrangement application.
# Date          : 2025-10-13
# ----------------------------------------------------------------------

import config
import logs


class Room:
    """
    Room class for representing an exam room.

    Attributes:
        room_id (str): The unique identifier for the room.
        room_name (str): The name of the room.
        capacity (int): The maximum number of students that can be seated in the room.
        seats_db (dict): A dictionary containing seat objects indexed by seat ID.
        available_seats_id (list): A list of seat IDs that are currently available.
        students (dict or None): A dictionary of students assigned to the room.
        occupied_seats_id (list or None): A list of seat IDs that are currently occupied.
    """

    def __init__(self, room_id, room_name, capacity, seats_db, available_seats_id):
        """
        Initialize a Room object.

        Args:
            room_id (str): The unique identifier for the room.
            room_name (str): The name of the room.
            capacity (int): The maximum number of students that can be seated in the room.
            seats_db (dict): A dictionary containing seat objects indexed by seat ID.
            available_seats_id (list): A list of seat IDs that are currently available.
        """

        # Initialize attributes.
        self.room_id = room_id
        self.room_name = room_name
        self.capacity = capacity
        self.seats_db = seats_db
        self.available_seats_id = available_seats_id

        # Attributes to be assigned later.
        self.students = None
        self.occupied_seats_id = None

        # Write logs.
        messages = [
            "ROOM OBJECT CREATED",
            f"ID = {self.room_id}",
            f"NAME = {self.room_name}",
            f"CAPACITY = {self.capacity}",
            f"TOTAL SEATS = {len(self.seats_db)}",
            f"AVAILABLE SEATS = {len(self.available_seats_id)}",
            f"STUDENTS = {len(self.students) if self.students else 0}",
            f"OCCUPIED SEATS = {len(self.occupied_seats_id) if self.occupied_seats_id else 0}",
        ]
        logs.Logs.write_logs(messages)

    def __lt__(self, other):
        """
        Room comparison based on room ID.

        Args:
            other (Room): The other room object to compare against.

        Returns:
            bool: True if this room's ID is less than the other room's ID, False otherwise.
        """

        return self.room_id < other.room_id

    def get_room_info(self):
        """
        Get the information of the room.

        Returns:
            tuple: A tuple containing the room's name, capacity, number of available seats,
            number of occupied seats, number of remaining seats, and a list of remaining seat names.
        """

        # Get the names of the remaining available seats.
        remaining_seat_names = (
            config.ROOMS_DB[self.room_id][seat_id].seat_name
            for seat_id in sorted(
                set(self.available_seats_id) - set(self.occupied_seats_id)
            )
        )

        # Write logs.
        messages = [
            "ROOM INFO RETRIEVED",
            f"ID = {self.room_id}",
            f"NAME = {self.room_name}",
            f"CAPACITY = {self.capacity}",
            f"TOTAL SEATS = {len(self.seats_db)}",
            f"AVAILABLE SEATS = {len(self.available_seats_id)}",
            f"OCCUPIED SEATS = {len(self.occupied_seats_id) if self.occupied_seats_id else 0}",
            f"REMAINING SEATS = {len(remaining_seat_names)}",
            f"REMAINING SEAT NAMES = {sorted(remaining_seat_names)}",
        ]
        logs.Logs.write_logs(messages)

        # Return the room information as a tuple.
        return (
            self.room_name,
            self.capacity,
            len(self.available_seats_id),
            len(self.occupied_seats_id) if self.occupied_seats_id is not None else 0,
            len(remaining_seat_names),
            sorted(remaining_seat_names),
        )
