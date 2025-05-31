#!/usr/bin/py

# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process based on priority using match-case
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Note: '{task}' has an unknown priority level"

# Add extra note if time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    if priority in ["high", "medium"]:
        reminder += ". Try to plan accordingly."
    else:
        reminder += ". Consider completing it when you have free time."

# Print the final reminder
print("Reminder: \n" + reminder)
