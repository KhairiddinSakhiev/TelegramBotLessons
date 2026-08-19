from db_connection import get_connection

def register(username, password, email):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
                   insert into users(username, password, email) values
                   ('{username}', '{password}', '{email}')        
            """)
            conn.commit()
            print("user registred")
    except Exception as er:
        print("Registration error: ", er)

def get_user(username):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
                   select * from users where username='{username}'     
            """)
            user=cursor.fetchone()
            return user
    except Exception as er:
        print("Get user error: ", er)

  
def login(username, password):
    user_exists = get_user(username)
    if user_exists:
        if password == user_exists[2]:
            return user_exists
        else:
            print("Incorrect password")
    else:
        print("User not found")

