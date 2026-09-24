import csv

def create_students_csv(filename: str) -> None:
    with open(filename, "w", newline="", encoding="utf-8") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["student_id", "name", "midterm", "final"])
        csv_writer.writerow([101, "Amir Hussain", 85, 99])
        csv_writer.writerow([102, "Ahmad Jan", 78, 72])
        csv_writer.writerow([103, "Amir Mohammad", 75, 94])
        csv_writer.writerow([104, "Suliman", 50, 85])
        csv_writer.writerow([105, "Amir Ali", 86, 91])
        csv_writer.writerow([105, "Amir, Ali", 86, 91])

#========================================================================

def read_students_csv(filename:str) -> None:
    with open(filename, "r", newline="", encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            print(row["student_id"], row["name"], row["midterm"], row["final"])

#========================================================================

def calculate_results(filename: str, threshold: int) -> None:
    with open(filename, "r", newline="", encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        with open("results.csv", "w", newline="", encoding="utf-8") as result_file:
            csv_writer = csv.writer(result_file)
            csv_writer.writerow(["student_id", "name", "midterm", "final", "total", "average", "status"])
            print("names " + " total " + " average")
            for row in csv_reader:
                isPassed = False
                midterm = int(row["midterm"])
                final = int(row["final"])
                total = midterm + final
                average = (midterm + final) / 2
                if average > threshold:
                    isPassed = True
                csv_writer.writerow([row["student_id"], row["name"], midterm, final, total, average, "passed" if isPassed else "failed"])
                print(row["name"], total, average, "passed" if isPassed else "failed")

#========================================================================

# {1} creating the csv file:
# create_students_csv("students.csv")

#========================================================================

# {2} reading the csv file
# read_students_csv("students.csv")

#========================================================================

# {3} calculating students total and average
# calculate_results("students.csv", 70)


