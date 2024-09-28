from connect_mysql import connect_database

# Task 1: SQL BETWEEN Usage
def get_members_in_age_range(start_age, end_age):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            query = "select * from members where age between %s and %s"
            cursor.execute(query, (start_age, end_age))
            members = cursor.fetchall()
            if members is not None and len(members) > 0:
                for member in members:
                    print(f"Member ID: {member[0]}, Name: {member[1]}, Age: {member[2]}")
            else:
                print("No members found.")
        except Exception as e:
            print(f"Error: {e}.")
                
        finally:
            cursor.close()
            conn.close()
            
get_members_in_age_range(25, 30)