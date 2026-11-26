
import sqlite3

# -----------------------------
# 1. Connect to the database
# -----------------------------

connection = sqlite3.connect("university.db")
cursor = connection.cursor()

# -----------------------------
# 2. Create the students table
# -----------------------------

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        department TEXT NOT NULL,
        semester INTEGER
    )
""")

connection.commit()

print("Students table created successfully.")

# -----------------------------
# 3. Insert at least five students
# -----------------------------

students = [
    ("Ali", 20, "Computer Science", 3),
    ("Sara", 21, "Information Technology", 4),
    ("Ahmad", 22, "Software Engineering", 5),
    ("Maryam", 19, "Computer Science", 2),
    ("Omar", 23, "Information Systems", 6)
]

cursor.executemany("""
    INSERT INTO students (name, age, department, semester)
    VALUES (?, ?, ?, ?)
""", students)

connection.commit()

print("\nFive students inserted successfully.")

# -----------------------------
# 4. Display all records
# -----------------------------

print("\n--- ALL STUDENTS ---")

cursor.execute("SELECT * FROM students")
records = cursor.fetchall()

for student in records:
    print(student)

# -----------------------------
# 5. Search students by semester
# -----------------------------

search_semester = 3

print(f"\n--- STUDENTS IN SEMESTER {search_semester} ---")

cursor.execute(
    "SELECT * FROM students WHERE semester = ?",
    (search_semester,)
)

records = cursor.fetchall()

if records:
    for student in records:
        print(student)
else:
    print("No students found in this semester.")

# -----------------------------
# 6. Update one student's department
# -----------------------------

student_id = 1
new_department = "Software Engineering"

cursor.execute(
    "UPDATE students SET department = ? WHERE id = ?",
    (new_department, student_id)
)

connection.commit()

if cursor.rowcount > 0:
    print(f"\nStudent with ID {student_id} updated successfully.")
else:
    print(f"\nNo student found with ID {student_id}.")

# -----------------------------
# 7. Delete one record by ID
# -----------------------------

delete_id = 5

cursor.execute(
    "DELETE FROM students WHERE id = ?",
    (delete_id,)
)

connection.commit()

if cursor.rowcount > 0:
    print(f"Student with ID {delete_id} deleted successfully.")
else:
    print(f"No student found with ID {delete_id}.")

# -----------------------------
# 8. Print the final table contents
# -----------------------------

print("\n--- FINAL STUDENT RECORDS ---")

cursor.execute("SELECT * FROM students")
final_records = cursor.fetchall()

if final_records:
    for student in final_records:
        print(student)
else:
    print("The students table is empty.")

# -----------------------------
# 9. Close the database connection
# -----------------------------

connection.close()

print("\nDatabase connection closed.")
