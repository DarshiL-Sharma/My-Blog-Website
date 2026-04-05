# 📝 Flask Blog Website

A full-featured **blog web application** built using Flask that allows users to register, log in, create blog posts, and interact through comments.

This project demonstrates backend development, authentication, database management, and dynamic content rendering.

---

## 🚀 Features

* 🔐 User Authentication (Register/Login/Logout)
* 🔑 Secure password storage using **hashing & salting**
* ✍️ Create, edit, and delete blog posts
* 💬 Comment system for each blog post
* 🧑‍💻 User-specific content (posts linked to authors)
* 🗄️ SQLite database integration
* 📝 Rich text editor using CKEditor
* 🎨 Responsive UI with Bootstrap

---

## 📸 Preview

<img width="1829" height="925" alt="image" src="https://github.com/user-attachments/assets/1619d066-3e1e-4292-88ea-1c43a1dbef06" />

### 🏠 Homepage

![20260405-0515-24 6690600](https://github.com/user-attachments/assets/802795c7-7d0b-4e28-9846-df3050155301)

### 📝 Blog Post Page

![20260405-0518-19 6598012](https://github.com/user-attachments/assets/53d60e24-a9bf-4bd3-a184-ef489eec0b80)

### 🔐 Login / Register

![20260405-0521-34 4180398](https://github.com/user-attachments/assets/98ffa9d3-b5ae-4490-b256-45910e9840a8)

### 📞 Contact 

![20260405-0528-17 0303031](https://github.com/user-attachments/assets/797dc5a5-2f0e-4dff-a06e-351642d5c255)

---

## 🎬 Demo

![20260405-0526-00 6501619](https://github.com/user-attachments/assets/888d4b1a-7728-448f-855d-9143fa2d30e8)

> Tip :- Place your images and GIFs inside an `assets/` folder in your project directory.

---

## 🛠️ Tech Stack

### Backend

* Python
* Flask
* Flask-Login (Authentication)
* Flask-WTF (Forms)
* Flask-CKEditor (Rich Text Editor)

### Database

* SQLite
* SQLAlchemy ORM

### Frontend

* HTML
* CSS
* Bootstrap

---

## 🧠 Key Functionalities Explained

### 🔐 Authentication System

* Users can register with email, username, and password
* Passwords are securely stored using:

  * `generate_password_hash`
  * `check_password_hash`

---

### 📝 Blog System

* Logged-in users can:

  * Create new blog posts
  * Edit existing posts
  * Delete posts
* Each post includes:

  * Title
  * Subtitle
  * Image URL
  * Content (rich text)
  * Author
  * Date

---

### 💬 Comment System

* Only logged-in users can comment
* Comments are linked to:

  * User (author)
  * Blog post

---

### 🗄️ Database Structure

#### User Table

* id
* email
* password (hashed)
* name
<img width="1822" height="257" alt="image" src="https://github.com/user-attachments/assets/e31411da-8c52-43be-8606-90ea4ef2798f" />

#### BlogPost Table

* id
* title
* subtitle
* date
* body
* img_url
* author_id
<img width="1677" height="283" alt="image" src="https://github.com/user-attachments/assets/7619d0ac-485b-439d-86a4-f825aa1ac235" />

#### Comment Table

* id
* text
* author_id
* post_id
<img width="1797" height="260" alt="image" src="https://github.com/user-attachments/assets/f61f7e61-457f-448e-8180-74978a5bc1a0" />

---

## 📂 Project Structure

```
project/
│
├── main.py              # Main Flask application
├── forms.py             # WTForms (Login, Register, Create Post)
├── templates/           # HTML templates
├── static/              # CSS, JS, assets
├── assets/              # Screenshots & GIFs (for README)
├── posts.db             # SQLite database
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/DarshiL-Sharma/flask-blog.git```

```
### 2️⃣ Navigate to Project

```bash
cd My-Blog-Website
```

### 3️⃣ Install Dependencies

```bash
pip install flask flask-bootstrap flask-ckeditor flask-login flask-sqlalchemy werkzeug
```

### 4️⃣ Run the Application

```bash
python main.py
```

### 5️⃣ Open in Browser

```
http://127.0.0.1:5002/
```
---

## 🔮 Future Improvements

* 🧑‍💼 Admin panel for managing users/posts
* ❤️ Like/Bookmark system
* 🔍 Search & filter blogs
* 🌙 Dark mode
* 📷 Image upload instead of URL
* 📧 Email verification

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch
3. Make your changes
4. Submit a pull request

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgements

* Flask Documentation
* Bootstrap Framework
* Open-source community 💙

---

## 👨‍💻 Author

Developed by **Darshil Sharma**
https://github.com/DarshiL-Sharma
