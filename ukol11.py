from hashlib import sha256




class Hash:

    password = None  # Class attribute

    def __init__(self, user_name):
        self.user_name = user_name  # Instance attribute
        self.password=Hash.password
        self.password_hash = None

    def hash_it(self):
        self.password_hash = (sha256(self.password.encode('utf-8')).hexdigest())
        print(f"Hash: {self.password_hash}")



# Creating an object of the Hash class



user = Hash('alfa')
user.password='xfdr66de4cscz5'
print('Username:' , user.user_name)
user.hash_it()

