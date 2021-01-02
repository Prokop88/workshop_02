import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username", help="username")
parser.add_argument("-p", "--password", help="password(min 8 characters)")
parser.add_argument("-n", "--new_pass", help="new password(min 8 characters)", action="store_true")
parser.add_argument("-l", "--list", help="list", action="store_true")
parser.add_argument("-d", "--delete", help="delete", action="store_true")
parser.add_argument("-e", "--edit", help="edit", action="store_true")

args = parser.parse_args()
print(args.username)