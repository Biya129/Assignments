class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def update_info(self, name, email):
        self.name = name
        self.email = email

    def get_details(self):
        return f"Name: {self.name}, Email: {self.email}"


