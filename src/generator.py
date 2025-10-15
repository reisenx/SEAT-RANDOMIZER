# ----------------------------------------------------------------------
# File Name     : generator.py
# Author        : Worralop Srichainont
# Description   : Generator class for generating seating arrangements as CSV files.
# Date          : 2025-10-13
# ----------------------------------------------------------------------

import os

import pandas as pd

import config
import logs


class Generator:
    """
    Generator class for generating seating arrangements as CSV files.

    Attributes:
        None
    """

    @staticmethod
    def generate_output_students_csv():
        """
        Generate the output CSV file for students with their assigned rooms and seats.
        """

        # Write logs.
        messages = ["generate_output_students_csv() CALLED"]
        logs.Logs.write_logs(messages)

        # Initialize an empty dictionary to hold the data for the output CSV.
        REPORT_DATA = {}

        # Initialize empty lists for each header in the output CSV.
        for header in config.OUTPUT_STUDENTS_CSV_HEADER:
            REPORT_DATA[header] = []
        messages = [
            "REPORT_DATA INITIALIZED WITH HEADERS",
            f"{', '.join(config.OUTPUT_STUDENTS_CSV_HEADER)}",
        ]
        logs.Logs.write_logs(messages)

        # Populate the REPORT_DATA dictionary with student information.
        for student_id, student_obj in sorted(config.STUDENTS_DB.items()):
            # Get the current student's information.
            current_student_info = student_obj.get_student_info()

            # Append each piece of information to the corresponding list in REPORT_DATA.
            for idx, data in enumerate(current_student_info):
                # Get the corresponding header for the current index.
                header = config.OUTPUT_STUDENTS_CSV_HEADER[idx]

                # Append the data to the appropriate list in REPORT_DATA.
                REPORT_DATA[header].append(data)

                # Write logs.
                messages = [
                    "STUDENT INFO ADDED TO REPORT_DATA",
                    f"STUDENT ID = {student_id}",
                    f"HEADER = {header}",
                    f"DATA = {data}",
                ]
                logs.Logs.write_logs(messages)

        # Create a DataFrame from the REPORT_DATA dictionary.
        report_data_frame = pd.DataFrame(REPORT_DATA)

        # Write the DataFrame to a CSV file.
        report_data_frame.to_csv(
            config.GENERATED_STUDENT_PATH, index=False, encoding="utf-8-sig"
        )

        # Write logs.
        messages = [
            "OUTPUT STUDENTS CSV GENERATED",
            f"PATH = {config.GENERATED_STUDENT_PATH}",
            f"TOTAL STUDENTS = {len(report_data_frame)}",
        ]
        logs.Logs.write_logs(messages)

        # Write report.
        logs.Logs.write_report("Output students CSV generated successfully.")
        logs.Logs.write_report(f"Total Students: {len(report_data_frame)}")

    @staticmethod
    def generate_output_all_rooms_csv():
        """
        Generate the output CSV files for all rooms.
        """
        # Write logs.
        messages = ["generate_output_all_rooms_csv() CALLED"]
        logs.Logs.write_logs(messages)

        # Write report.
        logs.Logs.write_report("-" * 88)
        logs.Logs.write_report("Generating output CSV files for all rooms.")

        # Generate the output CSV file for each room.
        for _, room_obj in sorted(config.ROOMS_DB.items()):
            Generator.generate_output_room_csv(room_obj)

    @staticmethod
    def generate_output_room_csv(room):
        """
        Generate the output CSV file for a specific room.

        Args:
            room (Room): The room object containing seat information.
        """

        # Write logs.
        messages = ["generate_output_room_csv() CALLED"]
        logs.Logs.write_logs(messages)

        # Initialize an empty dictionary to hold the data for the output CSV.
        REPORT_DATA = {}

        # Initialize empty lists for the first 3 columns in the output CSV.
        for header in config.OUTPUT_ROOM_CSV_HEADER[: config.HAS_DATA_COLS_AMOUNT]:
            REPORT_DATA[header] = []

        # Write logs.
        messages = [
            "REPORT_DATA INITIALIZED WITH HEADERS",
            f"{', '.join(config.OUTPUT_ROOM_CSV_HEADER[: config.HAS_DATA_COLS_AMOUNT])}",
        ]
        logs.Logs.write_logs(messages)

        # Populate the REPORT_DATA dictionary with seat information.
        unassigned_seats = []
        for _, seat_obj in sorted(room.seats_db.items()):
            # Get the current seat's information.
            current_seat_info = seat_obj.get_seat_info()

            # Skip unassigned seats
            if current_seat_info[:2] == (None, None):
                unassigned_seats.append(seat_obj.seat_name)

                # Write logs.
                messages = [
                    "SEAT UNASSIGNED, SKIPPED",
                    f"ROOM ID = {room.room_id}",
                    f"SEAT ID = {seat_obj.seat_id}",
                    f"SEAT NAME = {seat_obj.seat_name}",
                ]
                logs.Logs.write_logs(messages)
                continue

            # Append each piece of information to the corresponding list in REPORT_DATA.
            for idx, data in enumerate(current_seat_info):
                # Get the corresponding header for the current index.
                header = config.OUTPUT_ROOM_CSV_HEADER[idx]

                # Append the data to the appropriate list in REPORT_DATA.
                REPORT_DATA[header].append(data)

                # Write logs.
                messages = [
                    "SEAT INFO ADDED TO REPORT_DATA",
                    f"ROOM ID = {room.room_id}",
                    f"SEAT ID = {seat_obj.seat_id}",
                    f"SEAT NAME = {seat_obj.seat_name}",
                    f"HEADER = {header}",
                    f"DATA = {data}",
                ]
                logs.Logs.write_logs(messages)

        # Initialize empty lists for the remaining columns in the output CSV.
        rows_amount = len(REPORT_DATA[config.OUTPUT_ROOM_CSV_HEADER[0]])
        for header in config.OUTPUT_ROOM_CSV_HEADER[config.HAS_DATA_COLS_AMOUNT :]:
            REPORT_DATA[header] = [None] * rows_amount

        # Write logs.
        messages = [
            "REPORT_DATA COMPLETED WITH EMPTY HEADERS",
            f"{', '.join(config.OUTPUT_ROOM_CSV_HEADER[config.HAS_DATA_COLS_AMOUNT :])}",
        ]
        logs.Logs.write_logs(messages)

        # Create a DataFrame from the REPORT_DATA dictionary.
        report_data_frame = pd.DataFrame(REPORT_DATA)

        # Write the DataFrame to a CSV file.
        GENERATED_ROOM_PATH = os.path.join(
            config.GENERATED_ROOMS_PATH, f"{room.room_id}.csv"
        )
        report_data_frame.to_csv(GENERATED_ROOM_PATH, index=False, encoding="utf-8-sig")

        # Write logs.
        messages = [
            "OUTPUT ROOM CSV GENERATED",
            f"PATH = {GENERATED_ROOM_PATH}",
            f"TOTAL ASSIGNED SEATS = {len(report_data_frame)}",
            f"TOTAL UNASSIGNED SEATS = {len(unassigned_seats)}",
            f"UNASSIGNED SEAT NAMES = {sorted(unassigned_seats)}",
        ]
        logs.Logs.write_logs(messages)

        # Write report.
        logs.Logs.write_report(
            f"Output room CSV generated for Room Name: {room.room_name}"
        )
        logs.Logs.write_report(f"Room Capacity: {room.capacity}")
        logs.Logs.write_report(f"Total Assigned Seats: {len(report_data_frame)}")
        logs.Logs.write_report(f"Total Unassigned Seats: {len(unassigned_seats)}")
        logs.Logs.write_report(f"Unassigned Seat Names: {sorted(unassigned_seats)}")
        logs.Logs.write_report("-" * 88)
