import matplotlib.pyplot as plt

employee_numbers = [45, 12, 30, 55, 20]  # Number of employees

# 2. Aapka Performance aur Attendance ka data (Percentage mein)
performance_scores = [88, 79, 85, 92, 81]  # Average Performance %
attendance_rates = [94, 89, 91, 95, 88]    # Average Attendance %

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Enterprise Employment & Performance Analytics Dashboard', fontsize=16, fontweight='bold')

# GRAPH 1: Department wise Employee Strength (Bar Chart)
ax1.bar(departments, employee_numbers, color='#2b5c8f', edgecolor='black', alpha=0.9)
ax1.set_title('Employee Distribution by Department', fontsize=12, fontweight='bold')
ax1.set_xlabel('Departments')
ax1.set_ylabel('Number of Employees')
ax1.grid(axis='y', linestyle='--', alpha=0.5)

# GRAPH 2: Performance vs. Attendance Comparison (Line Graph)
ax2.plot(departments, performance_scores, marker='o', color='#e056fd', linewidth=2.5, label='Avg Performance (%)')
ax2.plot(departments, attendance_rates, marker='s', color='#10ac84', linewidth=2.5, label='Avg Attendance (%)')
ax2.set_title('Performance & Attendance Trends', fontsize=12, fontweight='bold')
ax2.set_xlabel('Departments')
ax2.set_ylabel('Percentage (%)')
ax2.set_ylim(70, 100)  # Percentage range set kiya hai
ax2.legend()
ax2.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
print("Opening your enterprise performance dashboard window...")
plt.show()
