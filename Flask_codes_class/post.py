from database import DB
from comment import Comment

class Post:
    def __init__(self, id, name, author, content):
            values = (self.name, self.author, self.content)
            row = db.execute('INSERT INTO posts (name, author, content) VALUES (?, ?, ?)', values)
            return self

    def save(self):
        with DB() as db:
            values = (self.name, self.author, self.content, self.id)
            db.execute('UPDATE posts SET name = ?, author = ?, content = ? WHERE id = ?', values)
            return self

    def delete(self):
        with DB() as db:
            db.execute('DELETE FROM posts WHERE id = ?', (self.id,))

    def comments(self):
        return Comment.find_by_post(self)
