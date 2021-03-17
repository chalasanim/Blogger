from unittest import TestCase


class Blog(TestCase):
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.posts = []

    def __repr__(self):
        return f'{self.name}  by {self.author} and {len(self.posts)} posts'

    def json(self):
        return {
            "name": self.name,
            "author": self.author,
            "posts": [post.json() for post in self.posts],
        }

    def add_post(self, post, reader):
        title = post.title
        content = post.content

        print(f"New Title of the Blog post is  {title}")
        print(f"Content of the Blog Post is {content}")

        if reader == "Rishi":
            print("English Post for Rishi")
        elif reader == "kumar":
            print("Tamil Post for Kumar")
        else:
            print("Telugu Post for Malli")

        self.posts.append(post)





