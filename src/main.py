# ----------------------------------------------------------------------
# File Name     : main.py
# Author        : Worralop Srichainont
# Description   : Main script to run the seating arrangement application.
# Date          : 2025-10-13
# ----------------------------------------------------------------------

import time

import generator
import logs
import randomizer
import utility


class Main:
    """
    Main class to run the seating arrangement application.

    Attributes:
        None
    """

    def __init__(self):
        """
        Initialize the Main class.
        """

        # Initialize logs.
        logs.Logs.init_logs()

        # Display welcome message.
        print(f"{'='*31} SEAT RANDOMIZER PROGRAM {'='*32}")

        # Get user input for random mode.
        random_choice = (
            input("Do you want to enable random mode? (y/n): ").strip().lower()
        )
        is_random_mode = True
        if random_choice == "y":
            print("Random mode enabled.")
        elif random_choice == "n":
            is_random_mode = False
            print("Random mode disabled.")

        # Get user input for seed value if random mode is enabled.
        seed = time.time()
        if is_random_mode:
            seed_choice = (
                input("Do you want to set a custom seed? (y/n): ").strip().lower()
            )
            if seed_choice == "y":
                seed = input("Enter your custom seed: ").strip()
            elif seed_choice == "n":
                print("Using current time as seed.")

        # Display configuration summary.
        print("\nConfiguration Summary:")
        print(f"Random Mode: {'Enabled' if is_random_mode else 'Disabled'}")
        print(f"Seed: {seed}")
        print("=" * 88)

        # Initialize randomizer object.
        self.randomizer = randomizer.Randomizer(is_random_mode, seed)

        # Write report.
        logs.Logs.write_report(f"{'='*32} CONFIGURATION SUMMARY {'='*33}")
        logs.Logs.write_report(f"SEED: {self.randomizer.seed}")
        logs.Logs.write_report(
            f"RANDOM MODE: {'ENABLED' if is_random_mode else 'DISABLED'}"
        )
        logs.Logs.write_report(f"{'='*88}\n")

    def main(self):
        """
        Main method to run the seating arrangement application.
        """

        # Load student database from CSV file.
        print("Get Students Database from CSV file...")
        utility.Utility.get_students_database()
        print("Students Database loaded successfully.\n")

        # Load room and seat database from CSV file.
        print("Get Rooms and Seats Database from CSV file...")
        utility.Utility.get_rooms_database()
        print("Rooms and Seats Database loaded successfully.\n")

        # Assign seats to students.
        print("Assigning seats to students...")
        self.randomizer.assign_seats_to_students()
        print("Seats assigned to students successfully.\n")

        # Generate output CSV file with seating arrangement.
        print("Generating output CSV files...")
        generator.Generator.generate_output_students_csv()
        generator.Generator.generate_output_all_rooms_csv()
        print("Output CSV files generated successfully.\n")

        # Display completion message.
        print("=" * 88)
        print("Seating randomization process completed successfully.")
        print("The results have been saved to the 'generated' folder.")
        print("Please check the output CSV files and logs for details.")
        print("=" * 88)

        # End the logs.
        logs.Logs.end_logs()


# Call the main function to run the program.
if __name__ == "__main__":
    main_app = Main()
    main_app.main()
