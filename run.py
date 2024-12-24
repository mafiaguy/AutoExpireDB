from src.user_manager import UserManager
from src.timer import Timer  # Import the Timer class

if __name__ == "__main__":
    manager = UserManager()
    temp_user = 'temp_user'
    temp_password = 'temp_password'
    
    print(f"Attempting to create temporary user '{temp_user}'...")
    manager.create_temp_user(temp_user, temp_password)
    print(f"Temporary user '{temp_user}' created. It will be deleted after 10 minutes.")

    # Initialize timer for 10 minutes
    print("Starting timer for 10 minutes...")
    t = Timer(10, manager.drop_temp_user, args=(temp_user,))
    t.start()

    print("You can now use this user for database operations.")
    print("The program will exit, but the timer will continue to delete the user after the time expires.")
