task = input("Enter your task:")
priority = input("Priority (high/medium/low):").lower()
time_bound = input("Is it time-bound? (yes/no):").lower()
match priority:
    case "high":
        message = f"'{task}' is a high priority"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority level"
if time_bound == "yes":
    message += "that requiers immediate attention today!"
else:
    message = f"Note: {message}. Consider completing it when you have free time."
print("\nReminder:", message)