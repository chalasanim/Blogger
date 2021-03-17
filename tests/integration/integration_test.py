from unittest import TestCase
from blog import Blog
from post import Post


class BlogTest(TestCase):



    def test_repr(self):
        blog = Blog("Orange", "Mauli")
        self.assertEqual("Orange  by Mauli and 0 posts",blog.__repr__())

    def test_add_post(self):
        blog = Blog("Orange", "Mauli")
        self.assertEqual([],blog.posts)

        p1 = Post("First Post", "Best Content")
        p2 = Post("Second Post", "Another Best Content")
        blog.add_post(p1,"")
        blog.add_post(p2,"")
        self.assertEqual(2,len(blog.posts))

    def test_json(self):
        blog = Blog("Orange", "Mauli")
        p = Post("First Post", "Best Content")
        blog.add_post(p,"")
        expected = {"author": "Mauli","name": "Orange", "posts":[{"title":"First Post","content":"Best Content"}]}
        self.assertDictEqual(expected, blog.json())




