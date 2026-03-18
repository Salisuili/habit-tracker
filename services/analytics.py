from datetime import datetime
from functools import reduce

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
        Calculates the longest consecutive completion streak using functional programming.

        Args:
            dates (list): A list of completion dates in string format (YYYY-MM-DD).

        Returns:
            int: The length of the longest consecutive streak.
        """

        if len(dates) == 0:
            return 0

        converted_dates = list(map(lambda d: datetime.strptime(d, "%Y-%m-%d"), dates))
        
        # Sort dates chronologically
        converted_dates = sorted(converted_dates)

        # Calculate streaks using reduce
        # This builds a list of all streak lengths
        def calculate_streaks(acc, date_pair):
            streaks_list, prev_date = acc
            current_date = date_pair
            
            if prev_date is None:
                return (streaks_list + [1], current_date)
            
            if (current_date - prev_date).days == 1:
                updated_streaks = streaks_list[:-1] + [streaks_list[-1] + 1]
                return (updated_streaks, current_date)
            else:
                return (streaks_list + [1], current_date)
        
        initial_acc = ([], None)
        streak_lengths, _ = reduce(calculate_streaks, converted_dates, initial_acc)
        
        if not streak_lengths:
            return 0
        
        longest = reduce(lambda x, y: x if x > y else y, streak_lengths)
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
    
    @staticmethod
    def get_completion_dates(habit_completions):
        """
        Extracts just the date strings from completion objects using map.
        
        Args:
            habit_completions (list): List of completion objects/dictionaries.
            
        Returns:
            list: List of date strings.
        """
        return list(map(lambda c: c['date'] if isinstance(c, dict) else c.date, habit_completions))
    
    @staticmethod
    def filter_completions_by_period(completions, start_date, end_date):
        """
        Filters completions within a specific date range using filter.
        
        Args:
            completions (list): List of completion date strings.
            start_date (str): Start date in YYYY-MM-DD format.
            end_date (str): End date in YYYY-MM-DD format.
            
        Returns:
            list: Filtered list of completion date strings.
        """
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        
        def is_in_range(date_str):
            date = datetime.strptime(date_str, "%Y-%m-%d")
            return start <= date <= end
        
        return list(filter(is_in_range, completions))