import psycopg2
from config.db_config import DB_CONFIG

class UserManager:
    def __init__(self):
        self.conn = psycopg2.connect(**DB_CONFIG)
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()

    def create_temp_user(self, user, pwd):
        self.drop_temp_user(user)  # Drop existing user if it exists
        create_user_sql = f"CREATE USER {user} WITH PASSWORD '{pwd}';"
        self.cursor.execute(create_user_sql)
        # Grant permissions to the user
        self.grant_permissions(user)

    def drop_temp_user(self, user):
        try:
            # Revoke all privileges before dropping the user
            revoke_permission_sql = f"REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM {user};"
            self.cursor.execute(revoke_permission_sql)

            # Drop the user
            drop_user_sql = f"DROP USER IF EXISTS {user};"
            self.cursor.execute(drop_user_sql)
        except psycopg2.Error as e:
            print(f"Error when dropping user '{user}': {e}")

    def grant_permissions(self, user):
        # Grant SELECT permission on a specific table
        grant_permission_sql = f"GRANT SELECT ON TABLE admin_users TO {user};"
        self.cursor.execute(grant_permission_sql)

    def __del__(self):
        self.cursor.close()
        self.conn.close()
