import psycopg2

def get_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            user="postgres",
            database="online_menu_db",
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
                    password varchar not null,
                    email varchar(100) not null unique,
                    is_superuser boolean default false,
                    is_active boolean default true
                );
                create table if not exists foods(
                    id serial primary key,
                    title varchar(150) not null,
                    price numeric(9,2) 
                );
                create table if not exists orders(
                    id serial primary key,
                    customer_id int references users(id) on delete cascade,
                    table_number smallint,
                    total_price numeric(9,2),
                    order_date timestamp default now(),
                    status varchar default 'pending'
                );
                create table if not exists order_item(
                    id serial primary key,
                    order_id int references orders(id),
                    food_id int references foods(id),
                    quantity smallint default 1
                );
            """)
            conn.commit()
    except Exception as er:
        print("Creation tables error: ", er)
