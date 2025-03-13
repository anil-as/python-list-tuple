attendance_records = [
    (101, "2025-03-01", "Present"),
    (102, "2025-03-01", "Absent"),
    (103, "2025-03-01", "Present"),
    (104, "2025-03-01", "Present"),
    (105, "2025-03-01", "Absent"),
]

employees = [
    (101, "Alice Johnson", "HR"),
    (102, "Bob Smith", "IT"),
    (103, "Charlie Brown", "Finance"),
    (104, "David White", "IT"),
    (105, "Eve Black", "Marketing")
]

def mark_attendance():
    emp_id = int(input("Enter employee ID: "))
    att_date = input("Enter date (YYYY-MM-DD): ")
    status = input("Enter Status (Present/Absent): ")
    
    attendance_records.append((emp_id, att_date, status)) 
    print(f"Attendance marked for {emp_id} as {status} on {att_date} successfully.\n")

def att_search():
    emp_id = int(input("Enter employee ID: "))
    found = False
    print(f"\nAttendance records for Employee ID {emp_id}:")
    
    for record in attendance_records:
        if record[0] == emp_id:
            print(f"Date: {record[1]}, Status: {record[2]}")
            found = True
    if not found:
        print("No attendance records found.\n")


while True:
    print("\nOptions")
    print("-------")
    print("1. Mark Attendance")
    print("2. View Attendance Record")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        mark_attendance()
    elif choice == 2:
        att_search()
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
