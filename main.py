from db_connection import init_tables
from services import register, get_user, login

init_tables()

logged_in_user = None

while True:
    choice = input("""
        1 => register user
        2 => login
        3 => get profile
        4 => change_password -> baroi ivaz kardani parol paroli peshinaro bo username medihem va paroli navro update kunad
        5 => exit -> baroi purra barnomaro stop kardan
    """)
    match choice:
        case '1':
            print("------ Registration Form -------")
            username = input("username: ")
            password = input("password: ")
            email = input("email: ")
            register(username, password, email)
        case '2':
            print("------ Login Form -------")
            username = input("username: ")
            password = input("password: ")
            user = login(username, password)
            if user:
                logged_in_user = user
                print(f"Welcome {user[1]}")
                while logged_in_user:
                    choice = input("""
                        1 => add task -> ilova kardani task dar tablitsa ki az useri login shuda avtomatom id ro megirad agar login naboshad task natonad sokhta
                        2 => get task by id -> id - taskro dokhil mekunem az ruyi id select karda print mekunem naboshad task not found print mekunem
                        3 => show task -> dar in hama taskhoro az jadval nishon medihem ki az useri login shudagi hastand
                        4 => complete task -> in ham bo id task meshavad agar logged in user b useri task barobar boshad ba'dan 
                        task is_completed=true shavad agar useri task digar boshad ivaz karda nashavad(misol user_id = 1 lekin user_id login shuda 2 shumo dustup nadored)
                        5 => update task -> bo task id taskro megirem va update mekunem title, yo due date va chize ki lozim ba update boshad
                        6 => delete task -> bo task id taski lozimiro ki user_id ba user_id logged in user barobar ast udalit mekunad
                        7 => search task by title -> ba vosita title va metodi like meshavad faqat az khudashro
                        8 => show todays task -> taskhoi ki due_date barobar ba hamin ruz hastand nishon dihad az khudi userro
                        9 => show not completed tasks -> taskhoi is_completed=false az khudi userro nishon dihad
                        10 => show archive tasks(completed tasks) -> hama zadachahoi complete shudagii userro nishon dihad
                        11 => logout  -> logout     
                    """)
                    match choice:
                        case '7':
                            logged_in_user = None
                        case _:
                            print("Choice another option")
        case '3':
            if logged_in_user:
                print(f"ID: {logged_in_user[0]}, USERNAME: {logged_in_user[1]}, EMAIL: {logged_in_user[3]}")
            else:
                print("User not logged in")
        case _:
            print("invalid input")

