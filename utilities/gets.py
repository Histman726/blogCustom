from werkzeug.exceptions import abort

from models.postDB import Post
from models.userDB import User


def get_user(id):
    return User.query.get_or_404(id)


def get_post(id, check_author=True):
    if id is None:
        return

    post = Post.query.get_or_404(id)

    if post is None:
        abort(404, 'La publicación no existe')

    if check_author:
        abort(404, 'Usted no es el autor del post')

    return post

