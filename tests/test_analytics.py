import unittest
from services.analytics import Analytics


class TestAnalytics(unittest.TestCase):

    def test_longest_streak_daily(self):
        """
        Test longest streak for daily habit.
        """
        dates = [
            "2026-02-01",
            "2026-02-02",
            "2026-02-03",
            "2026-02-04",
            "2026-02-06",
            "2026-02-07",
            "2026-02-08",
            "2026-02-10"
        ]

        # Longest streak
        result = Analytics.longest_streak(dates, "daily")
        self.assertEqual(result, 4)

    def test_longest_streak_weekly(self):
        """
        Test longest streak for weekly habit.
        """
        dates = [
            "2026-01-01",
            "2026-01-08",
            "2026-01-15",
            "2026-01-22"
        ]

        
        result = Analytics.longest_streak(dates, "weekly")
        self.assertEqual(result, 4)

    def test_total_completions(self):
        """
        Test total number of completions.
        """
        dates = [
            "2026-02-01",
            "2026-02-02",
            "2026-02-03"
        ]

        result = Analytics.total_completions(dates)
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()