import hashlib, argparse

parser = argparse.ArgumentParser(description="sha256 identity verification tool")

def hash(input_string):
    return hashlib.sha256(input_string.encode()).hexdigest()

def create_master_key(passwords):
    password_list = []
    for password in passwords:
        password_list.append(hash(password))
    return ":".join(password_list)

def verify(master, password):
    hashes = master.split(':')
    password_hash = hash(password)
    for hash_obj in hashes:
        if hash_obj == password_hash:
            return True
    return False

parser.add_argument('--verify', nargs=2, metavar=('MASTER', 'PASSWORD'), help='Verify identity with master key and password')
parser.add_argument('--keygen', nargs='+', metavar='VALUE', help='Generate a key from the password list')

args = parser.parse_args()

if args.verify:
    master, password = args.verify
    print(str(verify(master, password)))
elif args.keygen:
    print(create_master_key(args.keygen))
else:
    print('SHA256 Identity Verifier\n\nOptions:\n--verify {master_key} {password}  Verify identity with a generated key and a password.\n  Example: python script.py --verify master>
