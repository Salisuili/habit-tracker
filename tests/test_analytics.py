import unittest
from services.analytics import Analytics


class TestAnalytics(unittest.TestCase):

    def test_longest_streak(self):
        dates = [
            "2026-02-01",
            "2026-02-02",
            "2026-02-03",
            "2026-02-04"
        ]
        self.assertEqual(Analytics.longest_streak(dates), 3)

    def test_total_completions(self):
        dates = ["2026-02-01", "2026-02-02"]
        self.assertEqual(Analytics.total_completions(dates), 2)


if __name__ == "__main__":
    unittest.main()