import sys
import os
import psycopg2

# Add the project directory to the Python path
# Assuming the script is in the scripts folder, adjust the relative path accordingly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.db_config import DB_CONFIG
from src.user_manager import UserManager

def execute_query(query, user, password):
    temp_user_config = {
        'host': DB_CONFIG['host'],
        'database': DB_CONFIG['database'],
        'user': user,
        'password': password,
        'port': DB_CONFIG['port']
    }
    
    try:
        conn = psycopg2.connect(**temp_user_config)
        conn.autocommit = True
        cursor = conn.cursor()
        
        cursor.execute(query)
        results = cursor.fetchall()
        
        for row in results:
            print(row)
            
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # SQL query to run with the temporary user
    sql_query = "SELECT * FROM admin_users;"  # Replace 'admin_users' with your actual table name if different

    # Initialize the UserManager
    manager = UserManager()

    # Create the temporary user
    temp_user = 'sid_user'
    temp_password = 'sid_password'

    print(f"Setting up test environment by creating temporary user '{temp_user}'...")
    manager.create_temp_user(temp_user, temp_password)
    
    try:
        print("Executing the test query with the temporary user...")
        execute_query(sql_query, temp_user, temp_password)
    finally:
        # Ensure clean-up by dropping the user even if the script encounters an error
        print(f"Cleaning up by dropping temporary user '{temp_user}'...")
        manager.drop_temp_user(temp_user)
