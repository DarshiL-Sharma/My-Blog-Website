from datetime import date
from flask import Flask, abort,request, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user , login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from werkzeug.security import generate_password_hash, check_password_hash
from forms import CreatePostForm, RegisterForm
from flask_login import LoginManager
from sqlalchemy import Integer, String, Text, ForeignKey

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    email = mapped_column(String(100), unique=True)
    password = mapped_column(String(100))
    name = mapped_column(String(100))

    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="author")



class BlogPost(db.Model):
    __tablename__ = "blog_posts"

    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String(250), unique=True)
    subtitle = mapped_column(String(250))
    date = mapped_column(String(250))
    body = mapped_column(Text)
    img_url = mapped_column(String(250))

    author_id = mapped_column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post")

class Comment(db.Model):
    __tablename__ = "comments"

    id = mapped_column(Integer , primary_key = True)
    text = mapped_column(String,nullable=False)
    author_id = mapped_column(Integer , ForeignKey("users.id"))
    post_id = mapped_column(Integer ,ForeignKey("blog_posts.id"))

    author = relationship("User", back_populates="comments")
    post = relationship("BlogPost", back_populates="comments")



with app.app_context():
    db.create_all()



@app.route('/register',methods = ["GET","POST"])
def register():
        form = RegisterForm()
        if form.validate_on_submit():
            new_user = User(
                email=form.email.data,
                name=form.name.data,
                password=generate_password_hash(form.password.data)
            )
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("get_all_posts"))
        return render_template("register.html", form=form)


@app.route('/login',methods=["POST","GET"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user  = db.session.execute(
            db.select(User).where(User.email==email)
        ).scalar()

        if not user:
            flash("Email does not Exist")
            return redirect(url_for('login'))

        elif not check_password_hash(user.password,password):
            flash("Incorrect Password")
            return redirect(url_for('login'))

        else:
            login_user(user)
            return redirect(url_for('get_all_posts'))

    return render_template("login.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:post_id>",methods = ["GET","POST"])
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    if request.method == "POST":
        if not current_user.is_authenticated:
            flash("Please Login to Comment")
            return redirect(url_for("login"))

        new_comment = Comment(
            text = request.form.get("comment"),
            author = current_user,
            post = requested_post
        )
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for("show_post",post_id=post_id))
    return render_template("post.html", post=requested_post)


@app.route("/new-post", methods=["GET", "POST"])
@login_required
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@login_required
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


@app.route("/delete/<int:post_id>")
@login_required
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)
