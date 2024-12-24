from src.user_manager import UserManager
from celery_tasks.tasks import drop_temp_user_task

if __name__ == "__main__":
    manager = UserManager()
    temp_user = 'temp_user'
    temp_password = 'temp_password'
    
    print(f"Attempting to create temporary user '{temp_user}'...")
    manager.create_temp_user(temp_user, temp_password)
    print(f"Temporary user '{temp_user}' created. It will be deleted after 10 minutes.")

    # Schedule the task to drop the temporary user after 10 minutes
    drop_temp_user_task.apply_async((temp_user,), countdown=600)

    print("You can now use this user for database operations.")
    print("The deletion task is scheduled, ensuring the user will be dropped after the time expires, even if the program exits.")
