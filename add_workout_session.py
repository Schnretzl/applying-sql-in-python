from connect_mysql import connect_database
import datetime

# Task 2: Add a Workout Session
def add_workout_session(member_id, date, duration_minutes, calories_burned):
    if not isinstance(date, datetime.datetime):
        print(f"Cannot add: date must be a datetime object. {date} is not a datetime object.")
        return None
    elif not isinstance(duration_minutes, int):
        print(f"Cannot add: duration_minutes must be an integer. {duration_minutes} is not an integer.")
        return None
    elif not isinstance(calories_burned, int):
        print(f"Cannot add: calories_burned must be an integer. {calories_burned} is not an integer.")
        return None
    
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            member_test_query = "select * from members where id = %s"
            cursor.execute(member_test_query, (member_id,))
            member = cursor.fetchone()
            if member is None:
                print(f"Cannot add: member with id {member_id} does not exist.")
                return None
            
            query = "insert into workoutsessions (member_id, session_date, duration_minutes, calories_burned) values (%s, %s, %s, %s)"
            new_workout_session = (member_id, date, duration_minutes, calories_burned)
            
            cursor.execute(query, new_workout_session)
            conn.commit()
            print("New workout session added successfully.")
        except Exception as e:
            print(f"Error: {e}.")
                
        finally:
            cursor.close()
            conn.close()
            
member_id = int(input("Member ID: "))
date = input("Date (YYYY-MM-DD): ")
date = datetime.datetime.strptime(date, "%Y-%m-%d")
duration_minutes = int(input("Duration (minutes): "))
calories_burned = int(input("Calories burned: "))
add_workout_session(member_id, date, duration_minutes, calories_burned)