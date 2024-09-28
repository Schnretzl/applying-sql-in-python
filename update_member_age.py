from connect_mysql import connect_database

# Task 3: Updating Member Information
def update_member_age(member_id, new_age):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            member_test_query = "select * from members where id = %s"
            cursor.execute(member_test_query, (member_id,))
            member = cursor.fetchone()
            if member is None:
                print(f"Cannot update: member with id {member_id} does not exist.")
                return None
            
            query = "update members set age = %s where id = %s"
            cursor.execute(query, (new_age, member_id))
            conn.commit()
            print("Member age updated successfully.")
        except Exception as e:
            print(f"Error: {e}.")
                
        finally:
            cursor.close()
            conn.close()
            
member_id = int(input("Member ID: "))
new_age = int(input("New Age: "))
update_member_age(member_id, new_age)