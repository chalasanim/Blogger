from blog import Blog
from post import Post
blogs=dict() # blogname:BlogObject
MENU_PROMPT = "Enter 'c' to create blog, 'l' to list the blogs,'r' to read the blog 'c' to create a post or 'q' to quit"
Post_Template='''---{} ---
 ---{}---
  '''

def menu():

    #show the user available blogs
    #let user make choice
    #let user do something with the choice
    #eventually exit
    print_blogs()
    selection=input(MENU_PROMPT)

    while selection != 'q':
        if selection=='c':
            ask_create_blog()
        elif selection=='l':
            print_blogs()
        elif selection=='r':
            ask_read_blog()
        elif selection=='p':
            ask_create_post()
        selection = input(MENU_PROMPT)

def ask_create_blog():
    title=input('Enter your blog title : ')
    author=input('Enter author name of the blog ')
    blogs[title]=Blog(title,author)

def ask_read_blog():

    title=input("Enter the blog title you want to read: ")
    print_posts(blogs[title])

def print_posts(blog):
    for post in blog.posts:
        print_post(post)

def print_post(post):
    print(Post_Template.format(post.title,post.content))

def ask_create_post():
    title = input('Enter your blog title : ')
    post = input('Enter author name of the blog ')
    content=input('Enter content')

    if title in blogs:
        blogs[title].add_post(Post(post,content),'')


def print_blogs():
    for key,blog in blogs.items():  # [(blog_name:Blog),(blog_name:Blog)]
        print('- {} by {} and {} posts'.format(blog.name,blog.author,len(blogs)))

