import unittest
from database.db_handler import DatabaseHandler
from services.habit_manager import HabitManager


class TestHabitManager(unittest.TestCase):

    def setUp(self):
        self.db = DatabaseHandler(":memory:")  # temporary DB
        self.manager = HabitManager(self.db)

    def test_create_habit(self):
        self.manager.create_habit("Exercise", "daily")
        habits = self.manager.list_habits()
        self.assertEqual(len(habits), 1)

    def test_complete_habit(self):
        self.manager.create_habit("Read", "daily")
        habit_id = self.manager.list_habits()[0][0]

        self.manager.complete_habit(habit_id)
        completions = self.db.get_completions(habit_id)

        self.assertEqual(len(completions), 1)


if __name__ == "__main__":
    unittest.main()