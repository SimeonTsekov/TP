from flask import Flask
from flask import render_template, request, redirect, url_for
from post import Post
from comment import Comment

app = Flask(__name__)

@@ -19,11 +20,18 @@ def show_post(id):

    return render_template('post.html', post=post)

@app.route('/posts/<int:id>/edit', methods=['GET', 'POST'])
def edit_post(id):
    post = Post.find(id)
    if request.method == 'GET':

    return render_template('edit_post.html', post=post)
    
    elif request.method == 'POST':
        post.name = request.form['name']
        post.author = request.form['author']
        post.content = request.form['content']
        post.save()
        return redirect(url_for('show_post', id=post.id))

@app.route('/posts/new', methods=['GET', 'POST'])
def new_post():
@@ -35,3 +43,18 @@ def new_post():

        return redirect(url_for('list_posts'))

@app.route('/posts/<int:id>/delete', methods=['POST'])
def delete_post(id):
    post = Post.find(id)
    post.delete()

    return redirect(url_for('list_posts'))

@app.route('/comments/new', methods=['POST'])
def new_comment():
    if request.method == 'POST':
        post = Post.find(request.form['post_id'])
        values = (None, post, request.form['message'])
        Comment(*values).create()

        return redirect(url_for('show_post', id=post.id))
