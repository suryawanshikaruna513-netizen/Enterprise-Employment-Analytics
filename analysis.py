import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="employee_analyzer"
)

cursor = conn.cursor()

print("\n--- EMPLOYEE PERFORMANCE ANALYZER ---")

cursor.execute("""
    SELECT 
        e.emp_id,
        e.name,
        e.department_id,
        e.salary,
        e.designation,
        a.present_days,
        a.total_days,
        ROUND((a.present_days / a.total_days) * 100, 2) AS attendance_percentage,
        p.task_assigned,
        p.task_completed,
        ROUND((p.task_completed / p.task_assigned) * 100, 2) AS task_completion_percentage,
        p.quality_score
    FROM employees e
    JOIN (
        SELECT
            emp_id,
            SUM(status = 'Present') AS present_days,
            COUNT(*) AS total_days
        FROM attendances
        GROUP BY emp_id
    ) a ON e.emp_id = a.emp_id
    JOIN performance p ON e.emp_id = p.emp_id
    ORDER BY p.quality_score DESC
""")

employees = cursor.fetchall()

print("\n--- EMPLOYEE PERFORMANCE REPORT ---")

for row in employees:
    print(
        "\nEmployee ID:", row[0],
        "\nName:", row[1],
        "\nDepartment:", row[2],
        "\nSalary:", row[3],
        "\nDesignation:", row[4],
        "\nAttendance:", str(row[7]) + "%",
        "\nTasks Assigned:", row[8],
        "\nTasks Completed:", row[9],
        "\nTask Completion:", str(row[10]) + "%",
        "\nQuality Score:", row[11]
    )

cursor.execute("""
    SELECT 
        SUM(status = 'Present'),
        COUNT(*),
        ROUND((SUM(status = 'Present') / COUNT(*)) * 100, 2)
    FROM attendances
""")

attendance = cursor.fetchone()

print("\n--- OVERALL ATTENDANCE ---")
print("Present Days:", attendance[0])
print("Total Attendance Records:", attendance[1])
print("Overall Attendance Percentage:", attendance[2], "%")

cursor.execute("""
    SELECT
        SUM(task_assigned),
        SUM(task_completed),
        ROUND((SUM(task_completed) / SUM(task_assigned)) * 100, 2)
    FROM performance
""")

tasks = cursor.fetchone()

print("\n--- TASK COMPLETION ---")
print("Total Tasks Assigned:", tasks[0])
print("Total Tasks Completed:", tasks[1])
print("Task Completion Percentage:", tasks[2], "%")

cursor.execute("""
    SELECT
        d.dept_name,
        COUNT(e.emp_id),
        ROUND(AVG(e.salary), 2),
        ROUND(AVG(p.quality_score), 2)
    FROM departments d
    JOIN employees e ON d.dept_id = e.department_id
    JOIN performance p ON e.emp_id = p.emp_id
    GROUP BY d.dept_id, d.dept_name
""")

department_data = cursor.fetchall()

print("\n--- DEPARTMENT PERFORMANCE ---")

for row in department_data:
    print(
        "Department:", row[0],
        "| Employees:", row[1],
        "| Average Salary:", row[2],
        "| Average Quality Score:", row[3]
    )

cursor.execute("""
    SELECT
        e.emp_id,
        e.name,
        p.quality_score
    FROM employees e
    JOIN performance p ON e.emp_id = p.emp_id
    ORDER BY p.quality_score DESC
    LIMIT 5
""")

top_employees = cursor.fetchall()

print("\n--- TOP 5 PERFORMERS ---")

for row in top_employees:
    print(
        "Employee ID:", row[0],
        "| Name:", row[1],
        "| Quality Score:", row[2]
    )

cursor.close()
conn.close()

print("\nConnection closed safely")