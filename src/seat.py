# ----------------------------------------------------------------------
# File Name     : seat.py
# Author        : Worralop Srichainont
# Description   : Seat class definition for the seating arrangement application.
# Date          : 2025-10-13
# ----------------------------------------------------------------------

import logs


class Seat:
    """
    Seat class for representing a seat in the exam room.

    Attributes:
        seat_id (str): The unique identifier for the seat.
        seat_name (str): The name of the seat.
        is_available (bool): Whether the seat is currently available.
        room_id (str): The ID of the room to which the seat belongs.
        student (Student or None): The student assigned to this seat, if any.
    """

    def __init__(self, seat_id, seat_name, is_available, room_id):
        """
        Initialize a Seat object.

        Args:
            seat_id (str): The unique identifier for the seat.
            seat_name (str): The name of the seat.
            is_available (bool): Whether the seat is currently available.
            room_id (str): The ID of the room to which the seat belongs.
        """

        # Initialize attributes.
        self.seat_id = seat_id
        self.seat_name = seat_name
        self.is_available = is_available
        self.room_id = room_id

        # Attribute to be assigned later.
        self.student = None

        # Write logs.
        messages = [
            "SEAT OBJECT CREATED",
            f"ID = {self.seat_id}",
            f"NAME = {self.seat_name}",
            f"ROOM ID = {self.room_id}",
            f"AVAILABLE = {'YES' if self.is_available else 'NO'}",
            f"STUDENT = {self.student.student_name if self.student else 'UNASSIGNED'}",
        ]
        logs.Logs.write_logs(messages)

    def __lt__(self, other):
        """
        Seat comparison based on room ID and seat ID.

        Args:
            other (Seat): The other seat object to compare against.

        Returns:
            bool: True if this seat's room ID is less than the other seat's room ID,
            or if they are equal, if this seat's ID is less than the other seat's ID.
        """

        if self.room_id != other.room_id:
            return self.room_id < other.room_id
        return self.seat_id < other.seat_id

    def get_seat_info(self):
        """
        Get the information of the seat.

        Returns:
            tuple: A tuple containing the room name, seat name, and student name assigned to the seat.
        """
        # Write logs.
        messages = [
            "SEAT INFO RETRIEVED",
            f"ID = {self.seat_id}",
            f"NAME = {self.seat_name}",
            f"ROOM ID = {self.room_id}",
            f"AVAILABLE = {'YES' if self.is_available else 'NO'}",
            f"STUDENT = {self.student.student_name if self.student else 'UNASSIGNED'}",
        ]
        logs.Logs.write_logs(messages)

        # Return the seat information.
        return (
            self.student.student_id if self.student else None,
            self.student.student_name if self.student else None,
            self.seat_name,
        )
