from connect_mysql import connect_database

# Task 1: Add a Member
def add_member(name, age):
    if not isinstance(name, str):
        print(f"Cannot add: name must be a string. {name} is not a string.")
        return None
    elif not isinstance(age, int):
        print(f"Cannot add: age must be an integer. {age} is not an integer.")
        return None
    
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            new_member = (name, age)
            
            query = "insert into members (name, age) values (%s, %s)"
            
            cursor.execute(query, new_member)
            conn.commit()
            print("New member added successfully.")
        except Exception as e:
            print(f"Error: {e}.")
                
        finally:
            cursor.close()
            conn.close()
            
name = input("Name: ")
age = int(input("Age: "))
add_member(name, age)