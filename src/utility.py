# ----------------------------------------------------------------------
# File Name     : utility.py
# Author        : Worralop Srichainont
# Description   : Utility functions for the data handling in the seating
#                 arrangement application.
# Date          : 2025-10-13
# ----------------------------------------------------------------------

import os

import pandas as pd

import config
import logs
import room
import seat
import student


class Utility:
    """
    Utility functions for the data handling in the seating arrangement application.

    Attributes:
        None
    """

    @staticmethod
    def get_students_database():
        """
        Read the student CSV database file, then initialize Student object,
        and store them on the global variable STUDENTS_DB.
        """

        # Write logs.
        messages = ["get_students_database() CALLED"]
        logs.Logs.write_logs(messages)

        # Read the CSV file into a DataFrame.
        data_frame = pd.read_csv(config.STUDENTS_PATH)
        messages = [f"TOTAL STUDENTS READ FROM CSV = {len(data_frame)}"]
        logs.Logs.write_logs(messages)

        # Update the total number of students to the global variable.
        config.TOTAL_STUDENTS = len(data_frame)
        messages = [
            f"TOTAL STUDENTS UPDATED TO GLOBAL VARIABLE = {config.TOTAL_STUDENTS}"
        ]
        logs.Logs.write_logs(messages)

        # Iterate through each row in the DataFrame and create Student objects,
        # then store them in the global STUDENTS_DB dictionary.
        for row in data_frame.itertuples():
            # Create Student object.
            current_student = student.Student(row.student_id, row.student_name)

            # Store the Student object in the global STUDENTS_DB dictionary.
            config.STUDENTS_DB[row.student_id] = current_student

            # Write logs.
            messages = [
                "STUDENT OBJECT STORED IN STUDENTS_DB",
                f"ID = {current_student.student_id}",
                f"NAME = {current_student.student_name}",
            ]
            logs.Logs.write_logs(messages)

    @staticmethod
    def get_rooms_database():
        """
        Read the room CSV database file, then initialize Room object,
        and store them on the global variable ROOMS_DB.
        """

        # Write logs.
        messages = ["get_rooms_database() CALLED"]
        logs.Logs.write_logs(messages)

        # Read the CSV file into a DataFrame.
        data_frame = pd.read_csv(config.ROOMS_PATH)
        messages = [f"TOTAL ROOMS READ FROM CSV = {len(data_frame)}"]
        logs.Logs.write_logs(messages)

        # Iterate through each row in the DataFrame and create Room objects,
        # then store them in the global ROOMS_DB dictionary.
        for row in data_frame.itertuples():
            # Create Room object by calling get_room_object function.
            current_room = Utility.get_room_object(
                row.room_id, row.room_name, row.capacity
            )

            # Store the Room object in the global ROOMS_DB dictionary.
            config.ROOMS_DB[row.room_id] = current_room

            # Write logs.
            messages = [
                "ROOM OBJECT STORED IN ROOMS_DB",
                f"ID = {current_room.room_id}",
                f"NAME = {current_room.room_name}",
                f"CAPACITY = {current_room.capacity}",
                f"TOTAL SEATS = {len(current_room.seats_db)}",
                f"AVAILABLE SEATS = {len(current_room.available_seats_id)}",
            ]
            logs.Logs.write_logs(messages)

    @staticmethod
    def get_room_object(room_id, room_name, capacity):
        """
        Create the Room object by reading the corresponding seats CSV file.

        Args:
            room_id (str): The unique identifier for the room.
            room_name (str): The name of the room.
            capacity (int): The total capacity of the room.

        Returns:
            Room: An instance of the Room class containing seat objects and available seat IDs.
        """

        # Write logs.
        messages = ["get_room_object() CALLED", f"ROOM ID = {room_id}"]
        logs.Logs.write_logs(messages)

        # Construct the file path for the room's seats CSV file.
        FILENAME = f"{room_id}.csv"
        SEATS_DB_PATH = os.path.join(config.SEATS_PATH, FILENAME)

        # Read the CSV file into a DataFrame.
        data_frame = pd.read_csv(SEATS_DB_PATH)
        messages = [f"TOTAL SEATS READ FROM CSV = {len(data_frame)}"]
        logs.Logs.write_logs(messages)

        # Initialize seat objects dictionary and available seat IDs list.
        SEATS_DB = {}
        AVAILABLE_SEATS_IDS = []

        # Iterate through each row in the DataFrame and create Seat objects,
        for row in data_frame.itertuples():
            # Create Seat object.
            current_seat = seat.Seat(
                row.seat_id, row.seat_name, row.is_available, room_id
            )

            # If the seat is available, add its ID to the AVAILABLE_SEATS_IDS list.
            if row.is_available:
                AVAILABLE_SEATS_IDS.append(row.seat_id)

                # Write logs.
                messages = [
                    "SEAT AVAILABLE - ADDED TO AVAILABLE_SEATS_IDS",
                    f"SEAT ID = {row.seat_id}",
                    f"SEAT NAME = {row.seat_name}",
                    f"ROOM ID = {room_id}",
                ]
                logs.Logs.write_logs(messages)

            # Store the Seat object in the SEATS_DB dictionary.
            SEATS_DB[row.seat_id] = current_seat

            # Write logs.
            messages = [
                "SEAT OBJECT STORED IN SEATS_DB",
                f"ID = {current_seat.seat_id}",
                f"NAME = {current_seat.seat_name}",
                f"IS AVAILABLE = {current_seat.is_available}",
                f"ROOM ID = {current_seat.room_id}",
            ]
            logs.Logs.write_logs(messages)

        # Update the total number of available seats to the global counter variable TOTAL_AVAILABLE_SEATS.
        config.TOTAL_AVAILABLE_SEATS += len(AVAILABLE_SEATS_IDS)

        # Write logs.
        messages = [
            "TOTAL AVAILABLE SEATS UPDATED TO GLOBAL COUNTER",
            f"CURRENT VALUE = {config.TOTAL_AVAILABLE_SEATS}",
        ]
        logs.Logs.write_logs(messages)

        # Create and return the Room object.
        AVAILABLE_SEATS_IDS.sort()
        ROOM = room.Room(room_id, room_name, capacity, SEATS_DB, AVAILABLE_SEATS_IDS)
        return ROOM
