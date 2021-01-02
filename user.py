import argparse
from psycopg2 import connect, OperationalError
from psycopg2.errors import UniqueViolation

from clcrypto import check_password
from models import User

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username", help="username")
parser.add_argument("-p", "--password", help="password(min 8 characters)")
parser.add_argument("-n", "--new_pass", help="new password(min 8 characters)", action="store_true")
parser.add_argument("-l", "--list", help="list", action="store_true")
parser.add_argument("-d", "--delete", help="delete", action="store_true")
parser.add_argument("-e", "--edit", help="edit", action="store_true")

args = parser.parse_args()
print(args.username)


def create_user(cur, username, password):
    """
    function create user
    :param cur:
    :param username: str
    :param password: str
    :return:
    """
    if len(password) < 8:
        print("password is to short, must have 8 characters")
    else:
        try:
            user = User(username=username, password=password)
            user.save_to_db(cur)
            print("user create")
        except UniqueViolation as err:
            print("user already exist ! ", err)

def delete_user(cur, username, password):
    user = User.load_user_by_username(cur, username)
    if not user:
        print("user not exist")
    elif check_password(password, user.hashed_password):
        user.delete(cur)
        print("user create")
    elif:
        print("incorrect password")