import sys
import os

# Add the project directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.db_config import DB_CONFIG
import psycopg2

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
    sql_query = "SELECT * FROM admin_users;"  # Replace 'your_table_name' with the actual table name

    temp_user = 'temp_user'
    temp_password = 'temp_password'
    
    execute_query(sql_query, temp_user, temp_password)
