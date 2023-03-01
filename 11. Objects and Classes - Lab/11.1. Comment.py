class Comment:

    def __init__(self, username, content, likes = 0):
        self.username = username
        self.content = content
        self.likes = likes


georgi = Comment("user1", "I like this book")
print(georgi.username)
print(georgi.content)
print(georgi.likes)