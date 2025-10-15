# ----------------------------------------------------------------------
# File Name     : logs.py
# Author        : Worralop Srichainont
# Description   : Utility functions for logging in the process of seating
#                 arrangement application.
# Date          : 2025-10-13
# ----------------------------------------------------------------------

import time

import config


class Logs:
    """
    Utility functions for logging in the process of seating arrangement application.

    Attributes:
        None
    """

    @staticmethod
    def init_logs():
        """
        Initialize the logs and report file by creating or clearing it.
        """

        # Create or clear the logs file.
        with open(config.LOGS_PATH, "w", encoding="utf-8") as log_file:
            log_file.write(f"{'='*34} PROGRAM LOGS FILE {'='*35}\n")
            log_file.write(f"LOGS INITIALIZED AT {Logs.get_time_str()}\n")
            log_file.write(f"{'='*88}\n\n")

        # Create or clear the report file.
        with open(config.REPORT_PATH, "w", encoding="utf-8") as report_file:
            report_file.write(f"{'='*33} PROGRAM REPORT FILE {'='*34}\n")
            report_file.write(f"REPORT INITIALIZED AT {Logs.get_time_str()}\n")
            report_file.write(f"{'='*88}\n\n")

    @staticmethod
    def end_logs():
        """
        End the logs file by appending an end message with a timestamp.
        """

        with open(config.LOGS_PATH, "a", encoding="utf-8") as log_file:
            log_file.write(f"\n{'='*37} END OF LOGS {'='*38}\n")
            log_file.write(f"LOGS ENDED AT {Logs.get_time_str()}\n")
            log_file.write(f"{'='*88}\n")

        with open(config.REPORT_PATH, "a", encoding="utf-8") as report_file:
            report_file.write(f"\n{'='*36} END OF REPORT {'='*37}\n")
            report_file.write(f"REPORT ENDED AT {Logs.get_time_str()}\n")
            report_file.write(f"{'='*88}\n")

    @staticmethod
    def write_logs(messages):
        """
        Write logs messages to the logs file with a timestamp.

        Args:
            messages (list[str]): The logs messages to write.
        """

        with open(config.LOGS_PATH, "a", encoding="utf-8") as log_file:
            current_time = time.strftime("%H:%M:%S", time.localtime())

            log_file.write(f"TIMESTAMP: [{current_time}]\n")
            for message in messages:
                log_file.write(f"  - {message}\n")

    @staticmethod
    def write_report(message):
        """
        Write a report message to the report file.

        Args:
            message (str): The report message to write.
        """

        with open(config.REPORT_PATH, "a", encoding="utf-8") as report_file:
            report_file.write(f"{message}\n")

    @staticmethod
    def get_time_str():
        """
        Get the current time as a formatted string.

        Returns:
            str: The current time formatted as "DAY, DD MMM YYYY HH:MM:SS".
        """

        return time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
