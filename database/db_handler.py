import sqlite3
from datetime import datetime


class DatabaseHandler:
    """
    Handles all database operations for the habit tracking application.

    This class is responsible for creating the database tables,
    storing habits, recording habit completions, and retrieving
    habit data from the SQLite database.
    """

    def __init__(self, db_name="habits.db"):
        """
        Initializes the database connection.

        Args:
            db_name (str): Name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """
        Creates the required database tables if they do not already exist.

        Tables:
        - habits: stores information about each habit
        - completions: stores the dates when a habit was completed
        """
        cursor = self.conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            frequency TEXT NOT NULL,
            start_date TEXT NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS completions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            habit_id INTEGER,
            completion_date TEXT,
            FOREIGN KEY (habit_id) REFERENCES habits(id)
        )
        """)

        self.conn.commit()

    def add_habit(self, habit):
        """
        Adds a new habit to the database.

        Args:
            habit (Habit): Habit object containing the habit details.
        """
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO habits (name, frequency, start_date) VALUES (?, ?, ?)",
            (habit.name, habit.frequency, habit.start_date)
        )
        self.conn.commit()

    def get_habits(self):
        """
        Retrieves all habits stored in the database.

        Returns:
            list: A list of tuples containing habit records.
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM habits")
        return cursor.fetchall()

    def complete_habit(self, habit_id):
        """
        Records the completion of a habit for the current date.

        Args:
            habit_id (int): The ID of the habit being completed.
        """
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO completions (habit_id, completion_date) VALUES (?, ?)",
            (habit_id, datetime.today().strftime("%Y-%m-%d"))
        )
        self.conn.commit()

    def get_completions(self, habit_id):
        """
        Retrieves all completion dates for a specific habit.

        Args:
            habit_id (int): The ID of the habit.

        Returns:
            list: A list of completion dates.
        """
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT completion_date FROM completions WHERE habit_id = ?",
            (habit_id,)
        )
        return [row[0] for row in cursor.fetchall()]