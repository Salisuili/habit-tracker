from datetime import datetime


class Habit:
    """
    Represents a single habit defined by the user.

    A habit contains basic information such as its name,
    how often it should be performed (frequency), and the
    date it was created.
    """

    def __init__(self, name: str, frequency: str, start_date: str = None):
        """
        Initializes a new Habit object.

        Args:
            name (str): The name of the habit (e.g., "Exercise").
            frequency (str): The habit frequency (e.g., daily or weekly).
            start_date (str, optional): The date the habit was created.
                                        If not provided, today's date is used.
        """
        self.name = name
        self.frequency = frequency
        self.start_date = start_date or datetime.today().strftime("%Y-%m-%d")

    def to_dict(self):
        """
        Converts the habit object into a dictionary format.

        Returns:
            dict: A dictionary containing the habit's name,
                  frequency, and start date.
        """
        return {
            "name": self.name,
            "frequency": self.frequency,
            "start_date": self.start_date
        }