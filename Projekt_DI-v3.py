from hashlib import sha256


class File:

    name="passwd.txt"

    def __init__(self) -> None:

        self.file_name = File.name

        self.x = None
        self.file_open = None
        self.password_verify = None
        self.password_hash_verify = None
        self.password = None
        self.password_hash = None
        self.password_input = None
        self.row_to_write = None
        self.list = None
        self.file_name_open = None
        self.user_name_input = None
        self.file_write = None




    def file_op(self):
        try:
            self.file_write = open(self.file_name, "x")
            self.file_write.write(f"name,password\n")
            self.file_write.close()
        except FileExistsError:
            file_write = open(self.file_name, "a")




    def file_ck(self):
        self.user_name_input = input('Enter username to create: ')
        self.file_name_open = open(self.file_name, "r")

        for row in self.file_name_open:
            self.list = row.split(',')

            if self.user_name_input == (self.list[0].rstrip('\n')):
                print('User already exists: ' + self.list[0])
                exit()






    def hash_pw(self):

        self.password_input = input('Enter password to create: ')
        send_to_another_class_child=Sha(password_input=self.password_input, password_hash=self.password_hash)
        self.password_hash=send_to_another_class_child.hash_it()




    def file_wr(self):
        self.row_to_write = (self.user_name_input + ',' + self.password_hash)

        self.file_write = open(self.file_name, "a")
        self.file_write.write(f"{self.row_to_write}\n")
        self.file_write.close()

        print("Username and Hash have been writen. Let's do a test!")
        print()





    def hash_ck(self):
        self.password_verify = input('Login simulation - enter password for "' + self.user_name_input + '": ')

        send_to_another_class_child = Sha(password_input=self.password_verify, password_hash=self.password_hash_verify)
        self.password_hash_verify = send_to_another_class_child.hash_it()
        print(f"Hash check: {self.password_hash_verify}")

        self.file_open = open(self.file_name, "r")
        for row in self.file_open:
            self.list=row.split(',')
            if self.password_hash_verify==(self.list[1].rstrip('\n')) and self.user_name_input==(self.list[0].rstrip('\n')):
                self.x=1

        if self.x==1:
            print()
            print("Access granted for username/hash:")
            print(self.list[0], self.list[1])
        else:
            print()
            print("Login failed - incorrect password")
            print(self.list[0], self.list[1])


class Sha(File):

    def __init__(self, password_input: str, password_hash: str) -> None:
        super().__init__()

        self.password_hash = password_hash
        self.password_input= password_input

    def hash_it(self):

        self.password_hash = (sha256(self.password_input.encode('utf-8')).hexdigest())
        return self.password_hash

#########################################################################

f=File()
f.file_op()
f.file_ck()
f.hash_pw()
f.file_wr()
f.hash_ck()

#########################################################################











