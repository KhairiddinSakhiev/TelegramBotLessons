import psycopg2

def get_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            user="postgres",
            database="task_manager_db",
            password="Sakhi2000@postgres",
            port=5432
        )
        return conn
    except Exception as er:
        print("Connection error: ", er)

def init_tables():
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                create table if not exists users(
                    id serial primary key,
                    username varchar(50) not null unique,
                    password varchar(50) not null,
                    email varchar(100) not null unique
                );
                create table if not exists tasks(
                    id serial primary key,
                    title varchar(150) not null,
                    user_id int references users(id) on delete cascade,
                    due_date timestamp default now(),
                    is_completed boolean default false,
                    created_at timestamp default now()
                ); 
            """)
            conn.commit()
    except Exception as er:
        print("Creation tables error: ", er)
