# ----------------------------------------------------------------------
# File Name     : randomizer.py
# Author        : Worralop Srichainont
# Description   : Randomizer class for randomizing seat assignments to
#                 students in the seating arrangement application.
# Date          : 2025-10-13
# ----------------------------------------------------------------------

import random
import time

import config
import logs


class Randomizer:
    """
    Randomizer class for randomizing seat assignments to students in the seating arrangement application.

    Attributes:
        is_random_mode_enable (bool): Flag to enable or disable random mode.
        seed (float or int or str): Seed value for random number generation.
    """

    def __init__(self, is_random_mode=True, seed=time.time()):
        """
        Initialize Randomizer object with random mode flag and seed value.

        Args:
            is_random_mode_enable (bool, optional): Flag to enable or disable random mode. Defaults to True.
            seed (float or int or str, optional): Seed value for random number generation. Defaults to time.time().
        """

        # Initialize attributes.
        self.is_random_mode = is_random_mode
        self.seed = seed

        # Write logs.
        messages = [
            "RANDOMIZER OBJECT CREATED",
            f"RANDOM MODE = {'ENABLED' if self.is_random_mode else 'DISABLED'}",
            f"SEED = {self.seed}",
        ]
        logs.Logs.write_logs(messages)

        # Set the random seed for reproducibility.
        random.seed(self.seed)

        # Write logs.
        logs.Logs.write_logs(["RANDOM SEED SET"])

    def assign_seats_to_students(self):
        """
        Assign seats to students based on the randomized seating arrangement.
        """
        # Write logs.
        logs.Logs.write_logs(["assign_seats_to_students() CALLED"])

        # First, partition students and assign to each exam room, and get the occupied seat IDs.
        self.get_occupied_seats_id()

        # Then, for each room, assign the selected seat IDs to the assigned students.
        for room_id, room_obj in config.ROOMS_DB.items():
            # Get the occupied seat IDs in sorted order.
            occupied_seats_id = sorted(room_obj.occupied_seats_id)

            # Get the students assigned to the current room.
            students = list(room_obj.students.values())

            # Write logs.
            messages = [
                "SEATS ASSIGNED TO STUDENTS IN ROOM",
                f"ROOM ID = {room_id}",
                f"ASSIGNED STUDENTS = {len(students)}",
                f"OCCUPIED SEATS = {len(occupied_seats_id)}",
            ]
            logs.Logs.write_logs(messages)

            # Assign each occupied seat ID to the corresponding student in the room.
            for idx, seat_id in enumerate(occupied_seats_id):
                # Set the Seat object's student attribute to the Student object.
                config.ROOMS_DB[room_id].seats_db[seat_id].student = students[idx]

                # Set the Student object's seat attribute to the Seat object.
                students[idx].seat = config.ROOMS_DB[room_id].seats_db[seat_id]

                # Write logs.
                messages = [
                    "SEAT ASSIGNED TO STUDENT",
                    f"STUDENT ID = {students[idx].student_id}",
                    f"ROOM ID = {room_id}",
                    f"SEAT ID = {seat_id}",
                ]
                logs.Logs.write_logs(messages)

    def get_occupied_seats_id(self):
        """
        Get the occupied seat IDs for each exam room after partitioning students.
        """
        # Write logs.
        logs.Logs.write_logs(["get_occupied_seats_id() CALLED"])

        # First, separate students into partitions and assign to each exam room.
        self.partition_students()

        # Then, for each room, randomly select seat IDs for the assigned students.
        for room_id, room_obj in config.ROOMS_DB.items():
            # Get the number of students assigned to the current room.
            seat_amount = len(room_obj.students)

            # If random mode is enabled, randomly select seat IDs from the available seats in the room.
            # Assign the selected seat IDs to the room's occupied_seats_id attribute.
            if self.is_random_mode:
                config.ROOMS_DB[room_id].occupied_seats_id = list(
                    sorted(random.sample(room_obj.available_seats_id, seat_amount))
                )

            # If random mode is disabled, select the first 'seat_amount' seat IDs.
            else:
                room_obj.occupied_seats_id = room_obj.available_seats_id[:seat_amount]

            # Write logs.
            messages = [
                "OCCUPIED SEATS ID SELECTED",
                f"ROOM ID = {room_id}",
                f"OCCUPIED SEATS = {len(config.ROOMS_DB[room_id].occupied_seats_id)}",
            ]
            logs.Logs.write_logs(messages)

    def partition_students(self):
        """
        Separate student into partitions, then assign to each exam room.
        """

        # Write logs.
        logs.Logs.write_logs(["partition_students() CALLED"])

        # Get the partitioned seat amount dictionary.
        partitioned_amount = self.get_partitioned_seat_amount()

        # Get all student IDs.
        all_student_ids = sorted(config.STUDENTS_DB.keys())
        logs.Logs.write_logs(["ALL STUDENT IDs RETRIEVED"])

        # Shuffle the student IDs if random mode is enabled.
        if self.is_random_mode:
            random.shuffle(all_student_ids)
            logs.Logs.write_logs(["ALL STUDENT IDs SHUFFLED"])

        # Assign students to each room based on the partitioned seat amount.
        idx = 0
        for room_id, seat_amount in partitioned_amount.items():
            # Get the student IDs for the current room.
            student_ids = all_student_ids[idx : idx + seat_amount]
            messages = [
                "STUDENTS PARTITIONED AND ASSIGNED TO ROOM",
                f"ROOM ID = {room_id}",
                f"ASSIGNED STUDENTS = {len(student_ids)}",
            ]
            logs.Logs.write_logs(messages)

            # Map student IDs to Student objects, and set each Student object to the room.
            ROOM_STUDENTS = {}
            for student_id in student_ids:
                # Set each Student object's room attribute to the current Room object.
                config.STUDENTS_DB[student_id].room = config.ROOMS_DB[room_id]

                # Add the Student object to the ROOM_STUDENTS dictionary.
                ROOM_STUDENTS[student_id] = config.STUDENTS_DB[student_id]

                # Write logs.
                messages = [
                    "STUDENT ASSIGNED TO ROOM",
                    f"STUDENT ID = {student_id}",
                    f"ROOM ID = {room_id}",
                ]
                logs.Logs.write_logs(messages)

            # Assign the dictionary of Student objects to the room.
            config.ROOMS_DB[room_id].students = ROOM_STUDENTS

            # Write logs.
            messages = [
                "ROOM STUDENTS ASSIGNED",
                f"ROOM ID = {room_id}",
                f"TOTAL STUDENTS = {len(config.ROOMS_DB[room_id].students)}",
            ]
            logs.Logs.write_logs(messages)

            # Increment the index for the next partition.
            idx += seat_amount

    def get_partitioned_seat_amount(self):
        """
        Get a dictionary contains number of students assigned on each exam room.

        Returns:
            dict: A dictionary mapping room IDs to the number of students assigned.
        """

        # Write logs.
        logs.Logs.write_logs(["get_partitioned_seat_amount() CALLED"])

        # Initialize remaining students counter and partitioned seat amount dictionary.
        remaining_students = config.TOTAL_STUDENTS
        PARTITIONED_AMOUNT = {}

        # Iterate through each room and calculate the number of students to assign.
        for idx, [room_id, room_obj] in enumerate(config.ROOMS_DB.items()):
            # Calculate the ratio of available seats in the room to the total available seats.
            current_available_seats = len(room_obj.available_seats_id)
            ratio = current_available_seats / config.TOTAL_AVAILABLE_SEATS

            # Calculate the number of students to assign to the room based on the ratio.
            current_seat_amount = round(ratio * config.TOTAL_STUDENTS)

            # If it's the last room, assign all remaining students to it.
            if idx == len(config.ROOMS_DB) - 1:
                current_seat_amount = remaining_students

            # Store the calculated number of students in the PARTITIONED_AMOUNT dictionary.
            PARTITIONED_AMOUNT[room_id] = current_seat_amount

            # Update the remaining students counter.
            remaining_students -= current_seat_amount

            # Write logs.
            messages = [
                "PARTITIONED SEAT AMOUNT CALCULATED",
                f"ROOM ID = {room_id}",
                f"ASSIGNED STUDENTS = {current_seat_amount}",
                f"REMAINING STUDENTS = {remaining_students}",
            ]
            logs.Logs.write_logs(messages)

        # Return the partitioned seat amount dictionary.
        return PARTITIONED_AMOUNT
