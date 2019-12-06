conn = sqlite3.connect(DB_NAME)

conn.cursor().execute('CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, author TEXT, content TEXT)')
conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS comments
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        post_id INTEGER,
        message TEXT,
        FOREIGN KEY(post_id) REFERENCES posts(id)
    )
''')
conn.commit()

class DB:

