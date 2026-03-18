# Habit Tracking Application

A sleek, command-line tool developed in **Python** designed to help you build consistency and master your daily routines. This application allows you to create, track, and analyze habits with a focus on data-driven progress.


## Overview
The **Habit Tracking Application** simplifies personal development by recording habit completions and providing insightful analytics, such as total completions and "longest streak" milestones. All your data is stored locally and securely using SQLite.

## Features
* **Habit Management:** Create, view, and manage your personalized habit list.
* **Progress Tracking:** Mark habits as completed and maintain a full completion history.
* **Analytical Insights:** * Calculate total completions for any habit.
    * Identify your longest completion streaks to stay motivated.
* **Interactive Interface:** A user-friendly CLI powered by `Questionary`.
* **Data Persistence:** Reliable storage using a local SQLite database.


## Technologies Used
Tool

* **Python 3** Core programming language.
* **SQLite3** Lightweight relational database for persistent storage.
* **Questionary** Interactive and aesthetic command-line prompts.
* **Unittest** Framework for automated testing and reliability


## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository**
   ```bash
   git clone https://github.com/Salisuili/habit-tracker.git
   cd habit-tracker
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   * **Windows:** `.venv\Scripts\activate`
   * **macOS/Linux:** `source .venv/bin/activate`

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application
To launch the tracker, execute the following command:
```bash
python main.py
```
> [!TIP]
> Once started, simply follow the on-screen interactive menu to manage your habits!


## Testing
Keep the application robust by running the built-in test suite:
```bash
python -m unittest discover tests
```

## Future Improvements
* **GUI:** Development of a graphical user interface for a desktop experience.
* **Notifications:** Integration of habit reminders and "nudge" notifications.
* **Visual Analytics:** Implementation of graphs and charts to visualize progress over time.
