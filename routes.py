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
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]
        if not users.check_username(username):
            return render_template("error.html", message="Käyttäjätunnuksessa tulee olla 1-20 merkkiä", route="/register")

        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if not users.check_passwords(password1, password2):
            return render_template("error.html", message="Salasanat eroavat", route="/register")
        if not users.check_password(password1):
            return render_template("error.html", message="Salasana on tyhjä", route="/register")

        role = request.form["role"]
        if not users.check_role(role):
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
    users.check_csrf()
    if not users.require_role(2):
        return render_template("error.html", message="Sinulla ei ole oikeuksia luoda kyselyitä", route="/")
    topic = request.form["topic"]
    if topic in quizzes.get_topics():
        return render_template("error.html", message=f"Kysely '{topic}' on jo olemassa, kokeile keksiä uusi aihe", route="/base")
    if topic == "" or len(topic) > 20:
        return render_template("error.html", message="Kyselyn aiheessa tulee olla 1-20 merkkiä", route="/base")
    quiz_type = int(request.form["quiz_type"])
    nmr_of_questions = int(request.form["nmr_of_questions"])
    nmr_of_choices = int(request.form["nmr_of_choices"])
    return render_template("newquiz.html", topic=topic, quiz_type=quiz_type, questions=nmr_of_questions, choices=nmr_of_choices)

@app.route("/create", methods=["POST"])
def create():
    users.check_csrf()
    topic = request.form["topic"]
    quiz_type = int(request.form["quiz_type"])
    questions = request.form.getlist("question")
    choices = request.form.getlist("choice")
    nmr_of_choices = int(request.form["choices"])
    nmr_of_questions = int(request.form["nmr_of_questions"])
    correct = request.form.getlist("correct")
    for question in questions:
        if question == "" or len(question) > 100:
            return render_template("error.html", message="Kysymyksessä tulee olla 1-100 merkkiä", route="/base")
    for choice in choices:
        if choice == "" or len(choice) > 50:
            return render_template("error.html", message="Vaihtoehdossa tulee olla 1-50 merkkiä", route="/base")
    if quiz_type == 1 and nmr_of_questions != len([x for x in correct if x=="True"]):
        return render_template("error.html", message="Oikeita vastauksia tulee olla 1 per kysymys", route="/base")
    quiz_id = quizzes.create_quiz(topic, quiz_type)
    i = 0
    for question in questions:
        question_id = quizzes.create_question(quiz_id, question)
        for choice in range(int(nmr_of_choices)):
            quizzes.create_choice(question_id, choices[i], correct[i])
            i += 1
    return redirect("/")

@app.route("/quiz/<int:id>")
def quiz(id):
    topic = quizzes.get_quiz_topic(id)
    quiz_type = quizzes.get_quiz_type(id)
    questions = quizzes.get_questions(id)
    nmr_of_questions = len(questions)
    choices = quizzes.get_choices(questions)
    return render_template("quiz.html", quiz_id=id, quiz_type=quiz_type, topic=topic, questions=questions, choices=choices, \
        nmr_of_questions=nmr_of_questions)

@app.route("/answer", methods=["POST"])
def answer():
    users.check_csrf()
    quiz_id = request.form["quiz_id"]
    question_ids = request.form.getlist("question")
    choice_ids = [request.form[question] for question in question_ids if question in request.form]
    if not choice_ids:
        return render_template("error.html", message="Et täyttänyt kyselyä", route="/quiz/"+str(quiz_id))
    quizzes.store_user_answers(choice_ids)
    return redirect("/result/" + str(quiz_id))

@app.route("/result/<int:id>")
def result(id):
    topic = quizzes.get_quiz_topic(id)
    quiz_type = quizzes.get_quiz_type(id)
    questions = quizzes.get_questions(id)
    nmr_of_questions = len(questions)
    user_answers = quizzes.get_user_answers(id)
    if quiz_type == 1:
        choices = quizzes.get_choices(questions)
        right_answers = quizzes.user_right_answers(id)
        return render_template("result.html", topic=topic, quiz_type=quiz_type, questions=questions, \
            nmr_of_questions=nmr_of_questions, choices=choices, user_answers=user_answers, \
            right_answers=right_answers)
    if quiz_type == 2:
        choices = quizzes.get_poll_choices(id)
        return render_template("result.html", topic=topic, quiz_type=quiz_type, questions=questions, \
            nmr_of_questions=nmr_of_questions, choices=choices, user_answers=user_answers)

@app.route("/stats")
def stats():
    return render_template("stats.html")
