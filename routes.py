from app import app
from flask import render_template, request, redirect, session, abort
import users
import quizzes

@app.route("/")
def index():
    nmr_of_quizzes = quizzes.get_nmr_of_quizzes()
    available_quizzes = quizzes.get_quizzes()
    return render_template("index.html", nmr_of_quizzes=nmr_of_quizzes, available_quizzes=available_quizzes)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not users.login(username, password):
            return render_template("error.html", message="Väärä käyttäjätunnus tai salasana", route="/")
        return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]
        if len(username) < 1 or len(username) > 20:
            return render_template("error.html", message="Käyttäjätunnuksessa tulee olla 1-20 merkkiä", route="/register")

        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat", route="/register")
        if password1 == "":
            return render_template("error.html", message="Salasana on tyhjä", route="/register")

        role = request.form["role"]
        if role not in ("1", "2"):
            return render_template("error.html", message="Tuntematon käyttäjärooli", route="/register")

        if not users.register(username, password1, role):
            return render_template("error.html", message="Rekisteröinti ei onnistunut", route="/register")
        return redirect("/")
    
@app.route("/base")
def base():
    if not users.require_role(2):
        return render_template("error.html", message="Sinulla ei ole oikeuksia luoda kyselyitä", route="/")
    return render_template("base.html")

@app.route("/new", methods=["POST"])
def new():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    if not users.require_role(2):
        return render_template("error.html", message="Sinulla ei ole oikeuksia luoda kyselyitä", route="/")
    topic = request.form["topic"]
    if topic == "" or len(topic) > 20:
        return render_template("error.html", message="Kyselyn aiheessa tulee olla 1-20 merkkiä", route="/base")
    quiz_type = int(request.form["quiz_type"])
    quiz_id = quizzes.create_quiz(topic, quiz_type)
    nmr_of_questions = int(request.form["nmr_of_questions"])
    nmr_of_choices = int(request.form["nmr_of_choices"])
    return render_template("newquiz.html", quiz_id=quiz_id, topic=topic, quiz_type=quiz_type, questions=nmr_of_questions, choices=nmr_of_choices)

@app.route("/create", methods=["POST"])
def create():
    quiz_id = request.form["quiz_id"]
    questions = request.form.getlist("question")
    choices = request.form.getlist("choice")
    nmr_of_choices = request.form["choices"]
    correct = request.form.getlist("correct")
    for question in questions:
        if question == "" or len(question) > 50:
            render_template("error.html", message="Kysymyksessä tulee olla 1-50 merkkiä", route="/newquiz")
    for choice in choices:
        if choice == "" or len(choice) > 50:
            render_template("error.html", message="Vaihtoehdossa tulee olla 1-50 merkkiä", route="/newquiz")
    i = 0
    for question in questions:
        question_id = quizzes.create_question(quiz_id, question)
        for choice in range(int(nmr_of_choices)):
            quizzes.create_choice(question_id, choices[i], correct[i])
            i += 1
    return redirect("/")
