# ----------------------------------------------------------------------
# File Name     : student.py
# Author        : Worralop Srichainont
# Description   : Student class definition for the seating arrangement application.
# Date          : 2025-10-13
# ----------------------------------------------------------------------

import logs


class Student:
    """
    Student class for representing a student in the exam room.

    Attributes:
        student_id (str): The unique identifier for the student.
        student_name (str): The name of the student.
        room (Room or None): The room to which the student is assigned, if any.
        seat (Seat or None): The seat assigned to the student, if any.
    """

    def __init__(self, student_id, student_name):
        """Initialize a Student object.

        Args:
            student_id (str): The unique identifier for the student.
            student_name (str): The name of the student.
        """

        # Initialize attributes.
        self.student_id = student_id
        self.student_name = student_name

        # Attributes to be assigned later.
        self.room = None
        self.seat = None

        # Write logs.
        messages = [
            "STUDENT OBJECT CREATED",
            f"ID = {self.student_id}",
            f"NAME = {self.student_name}",
            f"ROOM = {self.room.room_name if self.room else 'UNASSIGNED'}",
            f"SEAT = {self.seat.seat_name if self.seat else 'UNASSIGNED'}",
        ]
        logs.Logs.write_logs(messages)

    def __lt__(self, other):
        """
        Student comparison based on student ID.

        Args:
            other (Student): The other student object to compare against.

        Returns:
            bool: True if this student's ID is less than the other student's ID, False otherwise.
        """

        return self.student_id < other.student_id

    def get_student_info(self):
        """
        Get the information of the student.

        Returns:
            tuple: A tuple containing the student's ID, name, room name, and seat name.
        """

        # Write logs.
        messages = [
            "STUDENT INFO RETRIEVED",
            f"ID = {self.student_id}",
            f"NAME = {self.student_name}",
            f"ROOM = {self.room.room_name if self.room else 'UNASSIGNED'}",
            f"SEAT = {self.seat.seat_name if self.seat else 'UNASSIGNED'}",
        ]
        logs.Logs.write_logs(messages)

        # Return the student information.
        return (
            self.student_id,
            self.student_name,
            self.room.room_name if self.room else None,
            self.seat.seat_name if self.seat else None,
        )
