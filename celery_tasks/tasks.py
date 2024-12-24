from celery import Celery
import psycopg2
from config.db_config import DB_CONFIG

# Initialize Celery
app = Celery('tasks', broker='redis://localhost:6379/0')  # Update with appropriate broker URL

@app.task
def drop_temp_user_task(user):
    conn = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        conn.autocommit = True
        cursor = conn.cursor()
        
        # Revoke privileges
        revoke_permission_sql = f"REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM {user};"
        cursor.execute(revoke_permission_sql)

        # Drop the user
        drop_user_sql = f"DROP USER IF EXISTS {user};"
        cursor.execute(drop_user_sql)
        print(f"User '{user}' successfully dropped.")
        
    except psycopg2.Error as e:
        print(f"Error occurred while dropping user: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()
