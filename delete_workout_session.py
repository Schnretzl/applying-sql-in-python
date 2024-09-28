from connect_mysql import connect_database

# Task 4: Delete a Workout Session
def delete_workout_session(session_id):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            session_test_query = "select * from workoutsessions where session_id = %s"
            cursor.execute(session_test_query, (session_id,))
            session = cursor.fetchone()
            if session is None:
                print(f"Cannot delete: workout session with session_id {session_id} does not exist.")
                return None
            
            query = "delete from workoutsessions where session_id = %s"
            cursor.execute(query, (session_id,))
            conn.commit()
            print("Workout session deleted successfully.")
        except Exception as e:
            print(f"Error: {e}.")
                
        finally:
            cursor.close()
            conn.close()
            
session_id = int(input("Workout Session ID: "))
delete_workout_session(session_id)