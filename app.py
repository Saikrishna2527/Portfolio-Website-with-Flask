from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # You can handle form data here
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        # For now, just redirect to home
        return redirect("/")
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
