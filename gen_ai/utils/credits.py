from .auth import load_users, save_users, get_user

def check_credits():
    users = load_users()
    return users[get_user()]["credits"] > 0

def deduct_credit():
    users = load_users()
    users[get_user()]["credits"] -= 1
    save_users(users)

def refill_credits(username, amount):
    users = load_users()
    if username in users:
        users[username]["credits"] += amount
        save_users(users)