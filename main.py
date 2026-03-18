import questionary
from database.db_handler import DatabaseHandler
from services.habit_manager import HabitManager


def main():
    """
    Entry point of the Habit Tracking Application.

    This function initializes the database handler and habit manager,
    then starts the command-line interface (CLI) loop. The user is
    presented with a menu that allows them to:

    - Create a new habit
    - List existing habits
    - Mark a habit as completed
    - Analyse habit performance
    - Exit the application

    The loop continues running until the user selects the "Exit" option.
    """

    db = DatabaseHandler()
    manager = HabitManager(db)

    while True:
        choice = questionary.select(
            "Choose an option:",
            choices=[
                "Create Habit",
                "List Habits",
                "Complete Habit",
                "Analyze Habit",
                "Exit"
            ]
        ).ask()

        if choice == "Create Habit":
            name = questionary.text("Habit name:").ask()
            frequency = questionary.select(
                "Frequency:",
                choices=["daily", "weekly"]
            ).ask()
            manager.create_habit(name, frequency)
            print("Habit created successfully.\n")

        elif choice == "List Habits":
            habits = manager.list_habits()
            for habit in habits:
                print(habit)

        elif choice == "Complete Habit":
            habit_id = questionary.text("Enter habit ID:").ask()
            manager.complete_habit(int(habit_id))
            print("Habit marked as completed.\n")

        elif choice == "Analyze Habit":
            habit_id = questionary.text("Enter habit ID:").ask()
            result = manager.analyze_habit(int(habit_id))
            print(result)

        elif choice == "Exit":
            break


if __name__ == "__main__":
    main()