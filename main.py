class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def print_details(self):
        return f"first name is {self.fname},last name is {self.lname}"

    @property
    def email(self):
        if self.fname is None or self.lname is None:
            print("email not set, kindly set it using setter")
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self, str1):
        word = str1.split("@")[0]
        self.fname = word.split(".")[0]
        self.lname = word.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


e1 = Employee("sumit", "kumar")
print(e1.email)
