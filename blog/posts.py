from datetime import datetime

class Post:
    def __init__(self, title=None, content=None):
        self.title = title
        self.content = content
        self.published = False
        self.published_date = None
        self.deleted = False

    def publish(self):
        if not self.published:
            self.published = True
            self.published_date = datetime.now()

    def edit(self, new_title=None, new_content=None):
        if new_title is not None:
            self.title = new_title
        if new_content is not None:
            self.content = new_content

    def delete(self):
        self.deleted = True
