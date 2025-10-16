# Seat Randomizer Application

This is the customized seat randomizer application using `pandas` library in
`Python`.

<div align="center">
    <h2>
        <a href="/docs/README.md">
            Project Documentation
        </a>
    </h2>
</div>

---

# Application Guide

## Installation

-   This application requires `python` version `3.8` or newer.
-   After installing Python, make sure that `pip` (Python Package Manager) is
    already installed. You can try running these command lines below.

```bash
python --version
pip --version
```

-   If `python` and `pip` are already installed, install the `pandas` library by
    using the command line below.

```bash
pip install pandas
```

---

## Database Setup

The user must prepare CSV database files inside `database` folder before running
an application.

The sample CSV database files are already attached in this repository.

### Student Database (`student.csv`) format

**File path:** `/database/students/students.csv`

serves as a student database file which has 2 columns as following

-   `student_id` is the ID of each student. <ins>**It must be unique.**</ins>
-   `student_name` is the name of each student including first name and last
    name.

**Sample Database**

```
student_id,student_name
6525683421,John Smith
6529497821,Jean Margaret
6543950921,Harry Brown
...
6788874621,Manuel Black
6789182321,Megan Scarlet
```

### Room Database (`rooms.csv`) format

**File path:** `/database/rooms/rooms.csv`

This serves as a examination room database file which has 3 columns as
following.

-   `room_id` is the ID of each examination room. <ins>**It must be
    unique.**</ins>
-   `room_name` is the name of each examination room.
-   `capacity` is the total seats inside this examination room.

**Sample Database**

Recommended `room_id` format: `R<room no.>`

```
room_id,room_name,capacity
R01,ROOM 01,40
R02,ROOM 02,40
R03,ROOM 03,40
R04,ROOM 04,49
R05,ROOM 05,49
```

### Seat Database (`<room_id>.csv`) format

**File path:** `/database/rooms/seats/<room_id>.csv`

This serves as a seat database file of `<room_id>` room which has 3 columns as
following.

-   `seat_id` is the ID of each seat inside the examination room. <ins>**It must
    be unique.**</ins>
-   `seat_name` is the name of each seat inside the examination room.
-   `is_available` is `True` or `False` value which indicates that the seat is
    available or not.

**Sample Database**

Recommended `seat_id` format: `R<room no.>-<seat no.>`

```
seat_id,seat_name,is_available
R01-01,01,True
R01-02,02,True
R01-03,03,True
...
R01-39,39,False
R01-40,40,False
```

---

## Running the Application

To run the application, just open `run.bat` file in `scripts` folder, and it
will run the application automatically.

Alternatively, you can open your code editor and directly run `main.py` file.

### Arrangement Mode

This application has 2 modes.

-   **NORMAL MODE** arranges the student to each seats by their `student_id` in
    ascending order.
-   **RANDOM MODE** arranges the student to each seats randomly.

### Customized Seed

The user can choose to customize their own seed, or just use the default seed.

-   **DEFAULT SEED** generated from the time value when they run the
    application.
-   **CUSTOMIZED SEED** can be any random string.

### Generated Results

After running the application, it generates the output files stored inside
`generated` folder.

-   **`students.csv`** indicates examination room and seat of each student
    sorted by `student_id`.
-   **`rooms/<room_id>.csv`** indicates student of each seat sorted by `seat_id`
    inside `room_id` room.

### Report & Logs

Aside from the generated CSV files, it also generates report and logs file for
validation stored inside `generated/logs` folder.

-   **`report.txt`** contains necessary report for the current result.
-   **`logs.txt`** contains all operation details executed by the application.

---

# Features

## Database System

-   The user must add student database containing `student_id` and
    `student_name` attributes on a CSV file.
-   The user must add room database containing `room_id`, `room_name` and
    `capacity` attributes on a CSV file.
-   The user must add seat database of each room containing `seat_id`,
    `seat_name` and `is_available` attributes on a CSV file.

## Handle Databases

-   This application can read all database from CSV files using `pandas`
    library.
-   The application can create `Student` object with attributes inside.
-   The application can create `Room` object with attributes inside.
-   The application can create `Seat` object with attributes inside.

## User Configurations

-   The user can choose **NORMAL MODE** to assign each student by their ID order
-   The user can choose **RANDOM MODE** to assign each student in random order.
-   The user can choose to specify seed for **RANDOM MODE**.

## Student Seat Assignments

-   The application can partition students to the unique rooms calculated by
    ratio of the available seats of each room by total available seats.
-   The application can correctly assign partitioned student inside each room to
    the unique seats.

## Output & Log System

-   The application can generate an output CSV file to indicate examination room
    and seat of each student sorted by `student_id`.
-   The application can generate an output CSV file for every examination room
    to indicate student of each seat sorted by `seat_id`.
-   The application can generate a result report of the current attempt.
-   The application can generate a log file of all operations of the current
    attempt.
