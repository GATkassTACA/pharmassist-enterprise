
from flask import Flask, render_template, request, redirect, url_for, send_file, session
import os
from auth import check_login, load_users, create_user
from ocr import extract_text_from_pdf
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET", "dev_secret")

UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "results"
ALLOWED_EXTENSIONS = {"pdf"}
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route("/")
def index():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("extractor.html", user=session["user"])

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if check_login(username, password):
            session["user"] = username
            return redirect(url_for("index"))
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if session.get("user") != os.getenv("ADMIN_USERNAME"):
        return redirect(url_for("login"))
    message = ""
    if request.method == "POST":
        new_user = request.form["new_username"]
        new_pass = request.form["new_password"]
        create_user(new_user, new_pass)
        message = f"User '{new_user}' created!"
    return render_template("dashboard.html", message=message, users=load_users())

@app.route("/extract", methods=["POST"])
def extract():
    if "user" not in session:
        return redirect(url_for("login"))

    file = request.files["pdf"]
    if file and file.filename.endswith(".pdf"):
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        result_path = os.path.join(RESULT_FOLDER, f"{filename}.txt")
        extract_text_from_pdf(filepath, result_path)
        return send_file(result_path, as_attachment=True)
    return "Invalid file type", 400

if __name__ == "__main__":
    app.run(debug=True)
