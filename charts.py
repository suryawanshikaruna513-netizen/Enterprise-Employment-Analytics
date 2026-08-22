import mysql.connector
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="employee_analyzer"
)

cursor = conn.cursor()

cursor.execute("""
    SELECT emp_id, task_assigned, task_completed
    FROM performance
    ORDER BY emp_id
""")

data = cursor.fetchall()

cursor.close()
conn.close()

if not data:
    print("No performance data found.")
else:
    emp_ids = [row[0] for row in data]
    assigned = [row[1] for row in data]
    completed = [row[2] for row in data]

    x = range(len(emp_ids))

    plt.figure(figsize=(10, 6))
    plt.bar(x, assigned, width=0.4, label="Tasks Assigned")
    plt.bar([i + 0.4 for i in x], completed, width=0.4, label="Tasks Completed")

    plt.title("Tasks Assigned vs Completed")
    plt.xlabel("Employee ID")
    plt.ylabel("Number of Tasks")
    plt.xticks([i + 0.2 for i in x], emp_ids, rotation=45)

    plt.legend()
    plt.tight_layout()
    plt.show()