# ----------------------------------------------------------------------
# File Name     : config.py
# Author        : Worralop Srichainont
# Description   : Configuration settings and global variables for
#                 the seating arrangement application.
# Date          : 2025-10-13
# ----------------------------------------------------------------------

import os

# Define paths constants
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_PATH = os.path.join(ROOT_PATH, "database")
ROOMS_PATH = os.path.join(DB_PATH, "rooms", "rooms.csv")
SEATS_PATH = os.path.join(DB_PATH, "rooms", "seats")
STUDENTS_PATH = os.path.join(DB_PATH, "students", "students.csv")

GENERATED_PATH = os.path.join(ROOT_PATH, "generated")
GENERATED_STUDENT_PATH = os.path.join(GENERATED_PATH, "output_students.csv")
GENERATED_ROOMS_PATH = os.path.join(GENERATED_PATH, "rooms")

REPORT_PATH = os.path.join(GENERATED_PATH, "logs", "report.txt")
LOGS_PATH = os.path.join(GENERATED_PATH, "logs", "logs.txt")

# Initialize global variables for databases
STUDENTS_DB = {}
ROOMS_DB = {}

# Initialize global counters
TOTAL_STUDENTS = 0
TOTAL_AVAILABLE_SEATS = 0

# CSV file column names
STUDENT_NAME_COL = "ชื่อ-นามสกุล"
STUDENT_ID_COL = "รหัสนิสิต"
ROOM_COL = "ห้อง"
SEAT_COL = "เลขที่นั่ง"
ACTUAL_SEAT_COL = "เลขที่นั่งจริง"
SIGNATURE_COL = "ลงชื่อ"

# Output CSV Headers
OUTPUT_STUDENTS_CSV_HEADER = [
    STUDENT_ID_COL,
    STUDENT_NAME_COL,
    ROOM_COL,
    SEAT_COL,
]

HAS_DATA_COLS_AMOUNT = 3
OUTPUT_ROOM_CSV_HEADER = [
    STUDENT_ID_COL,
    STUDENT_NAME_COL,
    SEAT_COL,
    ACTUAL_SEAT_COL,
    SIGNATURE_COL,
]
