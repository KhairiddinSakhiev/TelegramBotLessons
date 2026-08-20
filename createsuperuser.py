from db_connection import get_connection, init_tables
from getpass import getpass
from security import hash_password1

init_tables()

def create_superuser():
    with get_connection() as conn:
        cur = conn.cursor()
        username = input("username: ")
        password = getpass("password: ")
        hash_pass = hash_password1(password)
        email = input("email: ")
        cur.execute("insert into users(username, password, email, is_superuser) values (%s,%s,%s, true);", (username, hash_pass,email) )
        conn.commit()
    print("superuser created")

create_superuser()