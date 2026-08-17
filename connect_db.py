import mysql.connector

try:
    # 1. Connect directly to your new project database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="my_project_db"  # <--- Connecting to your database now
    )

    if connection.is_connected():
        cursor = connection.cursor()
        
        # 2. SQL query to insert data
        insert_query = "INSERT INTO project_users (name, email) VALUES (%s, %s)"
        user_data = ("Shree", "shree@example.com")
        
        # 3. Execute and commit the changes
        cursor.execute(insert_query, user_data)
        connection.commit()  # <--- This saves the data permanently
        
        print("Success: New user added to the project table!")
        cursor.close()

except mysql.connector.Error as err:
    print(f"Error: Operation failed due to: {err}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connection closed safely.")
