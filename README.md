Set up folder structure:
portfolio/
│
├── app.py              # Flask application
├── static/             # CSS, images, etc.
│    └── style.css
├── templates/          # HTML files
│    ├── index.html
│    └── contact.html
Create Flask routes in app.py:
/ → shows homepage (index.html).
/contact → shows contact form (contact.html) and handles form submissions.
Design HTML pages:
index.html will display your details.
contact.html will contain a form for name, email, and message.
Add minimal styling in style.css.
