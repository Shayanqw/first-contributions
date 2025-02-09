"""
Author: Shayan Pourahmad
Student ID: 101474651
CRN: 
Assignment: #1
"""

# Step 1.B: Create 5 variables:
gym_member = "Shayan"       # str
preferred_weight_kg = 10.5  # float
highest_reps = 15           # int
membership_active = True    # bool

# Step 1.C: Create a dictionary named workout_stats:
# This dictionary holds the workout minutes for different activities for each friend by Tuple
workout_stats = {
    "Shayan": (30, 45, 20),  # this is the dictionary with key and value for yoga, Running anfd Cycling:
    "Shamisa": (40, 35, 25),
    "Ali": (20, 50, 30),
    "Sahand": (45, 60, 25),
    "Amir": (40, 10, 75),
    "Mayson": (200, 0, 50),
    "Jim": (100, 0, 50),
    "Sarah": (0, 15, 100),
    "Hamed": (200, 0, 0),
}

# Step 1.D: this for loop will calculate the total workout minutes for each friend:
# and add a new entry to the dictionary with their total.
friends = list(workout_stats.keys())  # Get a list of all friends' names
for friend in friends:
    stats = workout_stats[friend]  # Get the workout minutes for the current friend
    total_minutes = sum(stats)  # Add up the minutes for all activities
    workout_stats[f"{friend}_Total"] = total_minutes  # Add the total to the dictionary


# Step 1.E: Create a 2-dimensional (nested) list called workout_lis:
# Each row represents a friend, and each column represents an activity (Yoga, Running, Cycling).
workout_list = [list(stats) for stats in workout_stats.values() if isinstance(stats, tuple)]

# Step 1.F: Slice the workout_list:
# First, the program print the yoga and Running minutes for all friends
print("yoga and Running Minutes:")
for friend in workout_list:
    print(f"yoga: {friend[0]} minutes, Running: {friend[1]} minutes")

# Next, the program print the Cycling minutes for the last two friends in the list
print("\nCycling Minutes for Last Two Friends:")
for friend in workout_list[-2:]:  # Last two friends
    print(f"Cycling: {friend[2]} minutes")

# Step 1.G: Use an if-statement within a loop :
# the code is going to check if any member(friend ) total workout time is more than 120 minutes(>= 120), it will print:
# *Great job staying active*
print("\nChecking for friends with total workout minutes >= 120:")
for friend, stats in workout_stats.items():
    if isinstance(stats, int) and stats >= 120:  # Check if total minutes >= 120
        print(f"Great job staying active, {friend.replace('_Total', '')}!")

# Step 1.H: Add a feature to allow the user to input a friend’s name. Check if the name exists in the dictionary:
# The user can enter a friend's name, and the program display their workout details if they exist in the dictionary.
friend_name = input("\nEnter a friend's name: \n\t")
if friend_name in workout_stats:
    print(f"\nWorkout stats for {friend_name}:")
    print(f"yoga: {workout_stats[friend_name][0]} minutes")
    print(f"Running: {workout_stats[friend_name][1]} minutes")
    print(f"Cycling: {workout_stats[friend_name][2]} minutes")
    print(f"Total: {workout_stats[f'{friend_name}_Total']} minutes")
# if the friend name did not exist in the dictionary:
else:
    print(f"\nFriend {friend_name} not found in the records.")

# Step 1.I: Include a section at the end of your program:
# the program will determine which friend has the highest and lowest total workout minutes.
totals = {friend.replace('_Total', ''): total for friend, total in workout_stats.items() if isinstance(total, int)}
max_friend = max(totals, key=totals.get)
min_friend = min(totals, key=totals.get)

# final print that shows the friend with the highest workout time and the friend with the lowest:
print(f"\nFriend with the highest total workout minutes: {max_friend} ({totals[max_friend]} minutes)")
print(f"Friend with the lowest total workout minutes: {min_friend} ({totals[min_friend]} minutes)")
