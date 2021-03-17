from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog
from post import Post

class AppTest(TestCase):

    def setUp(self) -> None:
        blog = Blog("Test", "Test Author")
        app.blogs={"Test":blog}


    def test_menu_print_prompt(self):
            with patch('builtins.input',return_value='q') as mocked_menu_prompt:
                 app.menu()
            mocked_menu_prompt.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input',return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_ask_create_blogs(self):
                with patch('builtins.input') as mocked_input:
                    mocked_input.side_effect=('Test','Test Author')
                    app.ask_create_blog()
                self.assertIsNotNone(app.blogs.get("Test"))

    def test_print_blogs(self):
                with patch('builtins.print') as mocked_print:
                    app.print_blogs()
                mocked_print.assert_called_with('- Test by Test Author and 1 posts')

    def test_read_blogs(self):
        with patch('builtins.input',return_value='Test') :
            with patch('app.print_posts') as mocked_blog:
                app.ask_read_blog()
            mocked_blog.assert_called_with(app.blogs["Test"])

    def test_print_posts(self):
        post=Post("post","Test Content")
        app.blogs['Test'].add_post(post,'')
        with patch('app.print_post') as mocked_blog:
            app.print_posts(app.blogs["Test"])
        mocked_blog.assert_called_with(app.blogs["Test"].posts[0])

    def test_print_post_content(self):
        post=Post("Post Title","Post Content")
        expected_print= '''---Post Title ---
 ---Post Content---
  '''
        with patch('builtins.print') as mocked_blog_content:
            app.print_post(post)
        mocked_blog_content.assert_called_with(expected_print)


    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
             with patch('app.ask_create_blog') as mocked_create_blog:
              mocked_input.side_effect=('c', 'Test Blog', 'Test Blog Author', 'q')
              app.menu()
             # self.assertIsNotNone(app.blogs['Test Blog'])
              mocked_create_blog.assert_called()

    def test_ask_create_post(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect=('Test','Test title','Test Content')
            app.ask_create_post()
            self.assertEqual(app.blogs['Test'].posts[0].title,'Test title')
            self.assertEqual(app.blogs['Test'].posts[0].content,'Test Content')



