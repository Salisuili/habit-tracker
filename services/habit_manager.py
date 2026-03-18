from models.habit import Habit
from services.analytics import Analytics


class HabitManager:
    """
    Manages habit-related operations in the application.

    This class acts as a controller between the user interface (CLI),
    the database layer, and the analytics module. It coordinates
    the creation of habits, retrieval of habits, completion tracking,
    and analysis of habit data.
    """

    def __init__(self, db_handler):
        """
        Initializes the HabitManager.

        Args:
            db_handler (DatabaseHandler): The database handler used
            to store and retrieve habit data.
        """
        self.db = db_handler

    def create_habit(self, name, frequency):
        """
        Creates a new habit and stores it in the database.

        Args:
            name (str): The name of the habit.
            frequency (str): The frequency of the habit
                             (e.g., daily or weekly).
        """
        habit = Habit(name, frequency)
        self.db.add_habit(habit)

    def list_habits(self):
        """
        Retrieves all habits stored in the database.

        Returns:
            list: A list of habit records.
        """
        return self.db.get_habits()

    def complete_habit(self, habit_id):
        """
        Marks a habit as completed.

        Args:
            habit_id (int): The ID of the habit to mark as completed.
        """
        self.db.complete_habit(habit_id)

    def analyze_habit(self, habit_id):
        """
        Analyses a habit's completion data.

        This method calculates statistics such as the total number
        of completions and the longest completion streak.

        Args:
            habit_id (int): The ID of the habit to analyse.

        Returns:
            dict: A dictionary containing:
                - total: total number of completions
                - longest_streak: longest consecutive completion streak
        """
        dates = self.db.get_completions(habit_id)
        return {
            "total": Analytics.total_completions(dates),
            "longest_streak": Analytics.longest_streak(dates)
        }