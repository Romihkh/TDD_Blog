class Comment:
    def __init__(self):
        self.text = None
        self.deleted = False

    def add_comment(self, text):
        self.text = text

    def edit_comment(self, new_text):
        self.text = new_text

    def delete_comment(self):
        self.deleted = True
