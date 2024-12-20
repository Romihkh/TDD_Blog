class Author:
    def __init__(self):
        self.name = None
        self.email = None
        self.active = False

    def create_author(self, name, email):
        self.name = name
        self.email = email
        self.active = True

    def update_author(self, name=None, email=None):
        if name is not None:
            self.name = name
        if email is not None:
            self.email = email

    def delete_author(self):
        self.active = False
