from datetime import date
import json

HABIT_FILE = "habit_log.json"

# Load habit log
try:
    with open(HABIT_FILE, "r") as file:
        habit_log = json.load(file)
except FileNotFoundError:
    habit_log = {}

today_str = str(date.today())
if today_str not in habit_log:
    habit_log[today_str] = {}

def save_habits():
    with open(HABIT_FILE, "w") as file:
        json.dump(habit_log, file, indent=4)

def add_habit():
    habit = input("Enter the habit to add: ").strip()
    if habit in habit_log[today_str]:
        print("Habit already exists for today.")
    else:
        habit_log[today_str][habit] = False
        save_habits()
        print(f"Added habit '{habit}' for today.")

def view_today():
    if not habit_log[today_str]:
        print("No habits set for today.")
    else:
        print("\nToday's Habits:")
        for i, (habit, status) in enumerate(habit_log[today_str].items(), 1):
            mark = "[x]" if status else "[ ]"
            print(f"{i}. {mark} {habit}")

def toggle_habit():
    habits = list(habit_log[today_str].keys())
    if not habits:
        print("No habits to toggle today.")
        return

    view_today()
    try:
        n = int(input("Enter the number of the habit to toggle: "))
        if 1 <= n <= len(habits):
            habit = habits[n - 1]
            habit_log[today_str][habit] = not habit_log[today_str][habit]
            save_habits()
            print(f"Toggled '{habit}' to {'done' if habit_log[today_str][habit] else 'not done'}.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Enter a valid number.")

def delete_habit():
    habits = list(habit_log[today_str].keys())
    if not habits:
        print("No habits to delete today.")
        return

    view_today()
    try:
        n = int(input("Enter the number of the habit to delete: "))
        if 1 <= n <= len(habits):
            habit = habits[n - 1]
            del habit_log[today_str][habit]
            save_habits()
            print(f"Deleted habit '{habit}'.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Enter a valid number.")

def view_history():
    if not habit_log:
        print("No habit history found.")
        return

    print("\nHabit History:")
    for log_date in sorted(habit_log.keys()):
        print(f"\nDate: {log_date}")
        for habit, status in habit_log[log_date].items():
            mark = "[x]" if status else "[ ]"
            print(f"  {mark} {habit}")

def run_habit_tracker():
    while True:
        print("\nHabit Tracker Menu")
        print("1. View Today's Habits")
        print("2. Add Habit")
        print("3. Toggle Habit Status")
        print("4. Delete Habit")
        print("5. View Habit History")
        print("6. Return to Main Menu")
        try:
            choice = int(input("> "))
            if choice == 1:
                view_today()
            elif choice == 2:
                add_habit()
            elif choice == 3:
                toggle_habit()
            elif choice == 4:
                delete_habit()
            elif choice == 5:
                view_history()
            elif choice == 6:
                break
            else:
                print("Invalid choice. Choose 1-6.")
        except ValueError:
            print("Please enter a valid number.")
