First Set up folder structure:
portfolio/
│
├── app.py              
├── static/          
│    └── style.css
├── templates/      
│    ├── index.html
│    └── contact.html
Next Create Flask routes in app.py:
/ → shows homepage (index.html).
/contact → shows contact form (contact.html) and handles form submissions.
After that Design HTML pages:
index.html will display our details.
contact.html will contain a form for name, email, and message.
Now Add minimal styling in styles.css.
