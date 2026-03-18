from datetime import datetime


class Analytics:
    """
    Provides analytical functions for habit data.

    This class contains methods that calculate statistics
    about habit completions, such as the longest streak
    and the total number of completions.
    """

    @staticmethod
    def longest_streak(dates):
        """
        Calculates the longest consecutive completion streak.

        Args:
            dates (list): A list of completion dates in string format (YYYY-MM-DD).

        Returns:
            int: The length of the longest consecutive streak.
        """

        # If there are no completion dates
        if len(dates) == 0:
            return 0

        converted_dates = []
        for d in dates:
            converted_dates.append(datetime.strptime(d, "%Y-%m-%d"))

        converted_dates.sort()

        longest = 1
        current_streak = 1

        for i in range(1, len(converted_dates)):

            # Calculate difference in days between two dates
            difference = (converted_dates[i] - converted_dates[i - 1]).days

            if difference == 1:
                current_streak += 1
            else:
                current_streak = 1

            if current_streak > longest:
                longest = current_streak

        return longest

    @staticmethod
    def total_completions(dates):
        """
        Calculates the total number of habit completions.

        Args:
            dates (list): A list of completion dates.

        Returns:
            int: Total number of completions.
        """
        return len(dates)