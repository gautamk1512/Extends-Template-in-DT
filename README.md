# 🌐 My Awesome Django Site

A simple Django project featuring a responsive Bootstrap UI, dynamic routing, and a functional contact form.

---

## 🔧 Project Features

- ✅ Django 4.x+
- ✅ Bootstrap 5.3.3 for responsive frontend design
- ✅ Template inheritance using `base.html`
- ✅ Pages: `Home`, `About`, `Contact`
- ✅ Carousel and Card section on the homepage
- ✅ Contact form with POST request handling

---

## 📁 Project Structure

```
my_awesome_django_site/
├── manage.py
├── mysite/              # Django settings and URLs
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                # Main app
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── about.html
│   │   └── contact.html
│   ├── views.py
│   ├── urls.py
│   └── forms.py
└── static/              # CSS/JS/Images
```

---

## 🚀 Getting Started

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/my-awesome-django-site.git
cd my-awesome-django-site
```

### Step 2: Create and Activate a Virtual Environment

```bash
python -m venv venv

# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 3: Install Django

```bash
pip install django
```

### Step 4: Apply Migrations

```bash
python manage.py migrate
```

### Step 5: Run the Development Server

```bash
python manage.py runserver
```

### Step 6: Open the Site in Your Browser

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📬 Contact Form

The Contact page includes a form that uses the POST method. It’s connected to Django’s `forms.py` and `views.py` to handle submissions. You can further expand it by saving form data to the database or sending email notifications.

---

## 🎨 UI Highlights

- Clean Bootstrap 5 layout with responsive design
- Carousel section for featured content
- Cards section for displaying services or features
- Consistent navigation using `base.html` and template inheritance

---

## 🚧 Future Enhancements (Optional)

- 💾 Save contact form submissions to the database
- 👤 Add user registration and login
- 🚀 Deploy to Render, Vercel, or Heroku
- 🧪 Add unit tests for views and forms

---

## 📄 License

MIT License

> You are free to use, modify, and distribute this project for personal or commercial use.

---

**Made with ❤️ using Django & Bootstrap**
