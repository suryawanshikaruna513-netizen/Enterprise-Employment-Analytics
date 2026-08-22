import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="emp"
)

cursor = conn.cursor()

# Employee Data
cursor.execute("SELECT * FROM emp")
data = cursor.fetchall()

print("\n--- Employee Data ---")

for row in data:
    print(row)

# Salary Analysis
cursor.execute("SELECT MAX(salary) FROM emp")
highest_salary = cursor.fetchone()[0]

cursor.execute("SELECT MIN(salary) FROM emp")
lowest_salary = cursor.fetchone()[0]

cursor.execute("SELECT AVG(salary) FROM emp")
average_salary = cursor.fetchone()[0]

print("\n--- Salary Analysis ---")
print("Highest Salary:", highest_salary)
print("Lowest Salary:", lowest_salary)
print("Average Salary:", round(average_salary, 2))

# Department-wise Average Salary
cursor.execute("""
    SELECT department_id, AVG(salary)
    FROM emp
    GROUP BY department_id
""")

department_salary = cursor.fetchall()

print("\n--- Department-wise Average Salary ---")

for department in department_salary:
    print(
        "Department:", department[0],
        "| Average Salary:", round(department[1], 2)
    )

# Performance Analysis
cursor.execute("""
    SELECT SUM(task_assigned),
           SUM(task_completed),
           AVG(quality_score)
    FROM performance
""")

performance = cursor.fetchone()

print("\n--- Performance Analysis ---")
print("Total Tasks Assigned:", performance[0])
print("Total Tasks Completed:", performance[1])
print("Average Quality Score:", round(performance[2], 2))

# Top Performer
cursor.execute("""
    SELECT emp_id, quality_score
    FROM performance
    ORDER BY quality_score DESC
    LIMIT 1
""")

top_performer = cursor.fetchone()

print("Top Performer Employee ID:", top_performer[0])
print("Highest Quality Score:", top_performer[1])

# Close connection
cursor.close()
conn.close()

print("\nConnection closed safely")