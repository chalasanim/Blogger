from unittest import TestCase
from post import Post
class PostTest(TestCase):

    def setUp(self) -> None:
       pass

    def test_create_post(self):
        p=Post("First Post","Best Content")
        self.assertEqual("First Post",p.title)
        self.assertEqual("Best Content",p.content)

    def test_json(self):
        p=Post("First Post","Best Content")
        expected={"title":"First Post","content":"Best Content"}
        self.assertDictEqual(expected,p.json())








