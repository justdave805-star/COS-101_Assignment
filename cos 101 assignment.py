# COS 101 Assignment - 16/11/26
# Loops, Functions, Physics Operations, Data Structures

# --- PART 1: FOR LOOP EXAMPLES FROM CLASS ---
print("--- For Loop Examples ---")
for i in range(0, 10):
    print(i)

print("--- With steps of 2 ---")
for i in range(0, 10, 2):
    print(i)

print("--- 0 to 100 step 2 ---")
for i in range(0, 100, 2):
    print(i)

# --- PART 2: PHYSICS FUNCTIONS ---

def calculate_velocity():
    d = float(input("Enter distance: "))
    t = float(input("Enter Time: "))
    if t == 0:
        print("Error: Time cannot be 0")
        return
    v = d / t
    print(f"Velocity = {v}")
    return v

def calculate_distance():
    v = float(input("Enter velocity: "))
    t = float(input("Enter Time: "))
    d = v * t
    print(f"Distance = {d}")
    return d

def calculate_time():
    d = float(input("Enter distance: "))
    v = float(input("Enter velocity: "))
    if v == 0:
        print("Error: Velocity cannot be 0")
        return
    t = d / v
    print(f"Time = {t}")
    return t

def calculate_acceleration():
    v = float(input("Enter final velocity: "))
    u = float(input("Enter initial velocity: "))
    t = float(input("Enter Time: "))
    if t == 0:
        print("Error: Time cannot be 0")
        return
    a = (v - u) / t
    print(f"Acceleration = {a}")
    return a

def calculate_force():
    m = float(input("Enter mass: "))
    a = float(input("Enter acceleration: "))
    f = m * a
    print(f"Force = {f}")
    return f

def calculate_average(*numbers):
    if len(numbers) == 0:
        print("Error: No numbers provided")
        return
    avg = sum(numbers) / len(numbers)
    print(f"Average = {avg}")
    for num in numbers:
        if num > avg:
            print(f"Error: {num} passes the average {avg}")
    return avg

# --- PART 3: DATA STRUCTURE - List and Dictionary ---
physics_operations = ["velocity", "distance", "time", "acceleration", "force", "average"]

physics_formulas = {
    "velocity": "v = d / t",
    "distance": "d = v * t",
    "time": "t = d / v",
    "acceleration": "a = (v - u) / t",
    "force": "F = m * a",
    "average": "sum / count"
}

print("\nList of operations:", physics_operations)
print("Dictionary of formulas:", physics_formulas)

# --- PART 4: PROGRAM SHOULD RUN IN A WHILE LOOP ---
while True:
    print("\n--- COS 101 Physics Calculator ---")
    print("1. Velocity")
    print("2. Distance")
    print("3. Time")
    print("4. Acceleration")
    print("5. Force")
    print("6. Average (1,2,3,4)")
    print("0. Exit")

    choice = input("Choose an operation (0-6): ")

    if choice == "1":
        calculate_velocity()
    elif choice == "2":
        calculate_distance()
    elif choice == "3":
        calculate_time()
    elif choice == "4":
        calculate_acceleration()
    elif choice == "5":
        calculate_force()
    elif choice == "6":
        calculate_average(1, 2, 3, 4)
    elif choice == "0":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Error: Invalid choice, try again")