from datetime import datetime


class Analytics:
    """
    Provides analytical functions for habit data.
    """

    @staticmethod
    def longest_streak(dates, frequency):
        """
        Calculates the longest streak based on habit frequency.

        Args:
            dates (list): List of completion dates (YYYY-MM-DD)
            frequency (str): "daily" or "weekly"

        Returns:
            int: Longest streak length
        """

        if len(dates) == 0:
            return 0

        # Convert to datetime objects
        converted_dates = []
        for d in dates:
            converted_dates.append(datetime.strptime(d, "%Y-%m-%d"))

        converted_dates.sort()

        # Determine expected gap
        if frequency == "daily":
            expected_gap = 1
        else:
            expected_gap = 7

        longest = 1
        current_streak = 1

        for i in range(1, len(converted_dates)):
            difference = (converted_dates[i] - converted_dates[i - 1]).days

            if difference == expected_gap:
                current_streak += 1
            else:
                current_streak = 1

            if current_streak > longest:
                longest = current_streak

        return longest

    @staticmethod
    def total_completions(dates):
        return len(dates)