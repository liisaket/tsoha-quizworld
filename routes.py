from flask import render_template, request, redirect, session, abort
from app import app
import users
import quizzes

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not users.login(username, password):
            return render_template("index.html", message="Väärä käyttäjätunnus tai salasana, yritä uudelleen!")
        return render_template("index.html")

@app.route("/quizzes")
def available_quizzes():
    if users.user_id():
        all_quizzes = quizzes.get_nmr_of_quizzes()
        available_quizzes = quizzes.get_quizzes(1)
        available_polls = quizzes.get_quizzes(2)
        nmr_quizzes = len(available_quizzes)
        nmr_polls = len(available_polls)
        done_quizzes = len(quizzes.get_done_quizzes())
        return render_template("quizzes.html", all_quizzes=all_quizzes, \
            available_quizzes=available_quizzes, available_polls=available_polls, nmr_quizzes=nmr_quizzes, \
            nmr_polls=nmr_polls, done_quizzes=done_quizzes)
    return render_template("error.html", message="Et ole kirjautunut sisään", route="/")

@app.route("/logout")
def logout():
    if users.user_id():
        users.logout()
        return redirect("/")
    return render_template("error.html", message="Et ole kirjautunut sisään", route="/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]
        if not users.check_username(username):
            return render_template("register.html", message="Käyttäjätunnuksessa tulee olla 1-20 merkkiä")

        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if not users.check_passwords(password1, password2):
            return render_template("register.html", message="Salasanat eroavat")
        if not users.check_password(password1):
            return render_template("register.html", message="Salasana on tyhjä")

        role = request.form["role"]
        if not users.check_role(role):
            return render_template("register.html", message="Tuntematon käyttäjärooli")

        if not users.register(username, password1, role):
            return render_template("register.html", message="Rekisteröinti ei onnistunut")
        return redirect("/")
    
@app.route("/base")
def base():
    if users.user_id():
        if not users.require_role(2):
            return render_template("error.html", message="Sinulla ei ole oikeuksia luoda kyselyitä", route="/")
    return render_template("base.html")

@app.route("/new", methods=["POST"])
def new():
    if users.user_id():
        users.check_csrf()
        if not users.require_role(2):
            return render_template("error.html", message="Sinulla ei ole oikeuksia luoda kyselyitä", route="/")
        topic = request.form["topic"]
        if topic.capitalize() in quizzes.get_topics():
            return render_template("base.html", message=f"Kysely '{topic}' on jo olemassa, koita keksiä uusi aihe!")
        if topic == "" or len(topic) > 20:
            return render_template("base.html", message="Kyselyn aiheessa tulee olla 1-20 merkkiä")
        topic = topic.capitalize()
        quiz_type = int(request.form["quiz_type"])
        nmr_of_questions = int(request.form["nmr_of_questions"])
        nmr_of_choices = int(request.form["nmr_of_choices"])
        return render_template("newquiz.html", topic=topic, quiz_type=quiz_type, questions=nmr_of_questions, choices=nmr_of_choices)
    return render_template("error.html", message="Et ole kirjautunut sisään", route="/")

@app.route("/create", methods=["POST"])
def create():
    if users.user_id():
        users.check_csrf()
        if not users.require_role(2):
            return render_template("error.html", message="Sinulla ei ole oikeuksia luoda kyselyitä", route="/")
        topic = request.form["topic"]
        quiz_type = int(request.form["quiz_type"])
        questions = request.form.getlist("question")
        choices = request.form.getlist("choice")
        nmr_of_choices = int(request.form["choices"])
        nmr_of_questions = int(request.form["nmr_of_questions"])
        correct = request.form.getlist("correct")
        for question in questions:
            if question == "" or len(question) > 50:
                return render_template("newquiz.html", quiz_type=quiz_type, questions=nmr_of_questions, \
                    choices=nmr_of_choices, message="Kysymyksessä tulee olla 1-50 merkkiä")
        for choice in choices:
            if choice == "" or len(choice) > 50:
                return render_template("newquiz.html", quiz_type=quiz_type, questions=nmr_of_questions, \
                    choices=nmr_of_choices, message="Vaihtoehdossa tulee olla 1-50 merkkiä")
        if quiz_type == 1 and nmr_of_questions != len([x for x in correct if x=="True"]):
            return render_template("newquiz.html", quiz_type=quiz_type, questions=nmr_of_questions, \
                choices=nmr_of_choices, message="Oikeita vastauksia tulee olla 1 per kysymys")
        quiz_id = quizzes.create_quiz(topic, quiz_type)
        i = 0
        for question in questions:
            question_id = quizzes.create_question(quiz_id, question)
            for choice in range(int(nmr_of_choices)):
                quizzes.create_choice(question_id, choices[i], correct[i])
                i += 1
        return redirect("/")
    return render_template("error.html", message="Et ole kirjautunut sisään", route="/")

@app.route("/quiz/<int:id>")
def quiz(id):
    if users.user_id():
        topic = quizzes.get_quiz_topic(id)
        if id in [x[1] for x in quizzes.get_done_quizzes()]:
            return render_template("quiz.html", quiz_id=id, topic=topic, message=True)
        quiz_type = quizzes.get_quiz_type(id)
        questions = quizzes.get_questions(id)
        nmr_of_questions = len(questions)
        choices = quizzes.get_choices(questions)
        return render_template("quiz.html", quiz_id=id, quiz_type=quiz_type, topic=topic, questions=questions, choices=choices, \
            nmr_of_questions=nmr_of_questions)
    return render_template("error.html", message="Et ole kirjautunut sisään", route="/")

@app.route("/answer", methods=["POST"])
def answer():
    if users.user_id():
        users.check_csrf()
        quiz_id = request.form["quiz_id"]
        question_ids = request.form.getlist("question")
        choice_ids = [request.form[question] for question in question_ids if question in request.form]
        errormessage = ""
        if not choice_ids:
            errormessage = "Et täyttänyt kyselyä!"
        elif len(choice_ids) != len(question_ids):
            errormessage = "Et täyttänyt kyselyä loppuun asti!"
        if errormessage != "":
            topic = quizzes.get_quiz_topic(quiz_id)
            quiz_type = quizzes.get_quiz_type(quiz_id)
            questions = quizzes.get_questions(quiz_id)
            nmr_of_questions = len(questions)
            choices = quizzes.get_choices(questions)
            return render_template("quiz.html", quiz_id=quiz_id, quiz_type=quiz_type, topic=topic, questions=questions, choices=choices, \
                nmr_of_questions=nmr_of_questions, errormessage=errormessage)
        quizzes.store_user_answers(choice_ids)
        return redirect("/result/" + str(quiz_id))
    return render_template("error.html", message="Et ole kirjautunut sisään", route="/")

@app.route("/result/<int:id>")
def result(id):
    if users.user_id():
        topic = quizzes.get_quiz_topic(id)
        quiz_type = quizzes.get_quiz_type(id)
        undone_quizzes = [x[1] for x in quizzes.get_undone_quizzes()]
        if id in undone_quizzes and quiz_type == 1:
            return render_template("result.html", quiz_type=quiz_type, topic=topic, quiz_id=id, message=True)
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
            message = False
            if id in undone_quizzes:
                message = True
            return render_template("result.html", topic=topic, quiz_type=quiz_type, questions=questions, \
                nmr_of_questions=nmr_of_questions, choices=choices, user_answers=user_answers, quiz_id=id, \
                message=message)
    return render_template("error.html", message="Et ole kirjautunut sisään", route="/")

@app.route("/stats")
def stats():
    if users.user_id():
        time = users.registration_time()
        all_quizzes = quizzes.get_nmr_of_quizzes()
        done_quizzes = len(quizzes.get_done_quizzes())
        available_quizzes = quizzes.get_quizzes(1)
        available_polls = quizzes.get_quizzes(2)
        return render_template("stats.html", time=time, available_polls=available_polls, \
            available_quizzes=available_quizzes, all_quizzes=all_quizzes, done_quizzes=done_quizzes)
    return render_template("error.html", message="Et ole kirjautunut sisään", route="/")

@app.route("/pick", methods=["GET", "POST"])
def pick():
    if users.user_id():
        if users.require_role(2):
            all_quizzes = quizzes.get_all_quizzes()
            if request.method == "GET":
                return render_template("pick.html", list=all_quizzes)
            if request.method == "POST":
                users.check_csrf()
                if "quiz" in request.form:
                    id = request.form["quiz"]
                    return redirect("/edit/" + str(id))
                return render_template("pick.html", list=all_quizzes, message=True)
        return render_template("error.html", message="Sinulla ei ole oikeuksia muokata kyselyitä", route="/")
    return render_template("error.html", message="Et ole kirjautunut sisään", route="/")

@app.route("/edit/<int:id>", methods=["POST", "GET"])
def edit(id):
    if users.user_id():
        if users.require_role(2):
            topic = quizzes.get_quiz_topic(id)
            quiz_type = quizzes.get_quiz_type(id)
            questions = quizzes.get_questions(id)
            choices = quizzes.get_choices(questions)
            message = ""
            if request.method == "GET":
                nmr_of_questions = len(questions)
                nmr_of_choices = len(choices)
                return render_template("edit.html", quiz_id=id, quiz_type=quiz_type, topic=topic, questions=questions, \
                choices=choices, nmr_of_questions=nmr_of_questions, nmr_of_choices=nmr_of_choices)
            if request.method == "POST":
                users.check_csrf()
                newtopic = request.form["newtopic"]
                newquestions = request.form.getlist("newquestion")
                newchoices = request.form.getlist("newchoice")
                nmr_of_choices = int(request.form["nmr_of_choices"])
                nmr_of_questions = int(request.form["nmr_of_questions"])
                newcorrect = request.form.getlist("newcorrect")
                old_questions = quizzes.get_questions(id)
                choice_ids = [x[0] for x in quizzes.get_choices(old_questions)]
                if newtopic == "" or len(topic) > 20:
                    return render_template("edit.html", quiz_id=id, quiz_type=quiz_type, topic=topic, questions=questions, \
                        choices=choices, nmr_of_questions=nmr_of_questions, nmr_of_choices=nmr_of_choices, \
                        message="Kyselyn aiheessa tulee olla 1-20 merkkiä")
                for question in newquestions:
                    if question == "" or len(question) > 50:
                        return render_template("edit.html", quiz_id=id, quiz_type=quiz_type, topic=topic, questions=questions, \
                            choices=choices, nmr_of_questions=nmr_of_questions, nmr_of_choices=nmr_of_choices, \
                            message="Kysymyksessä tulee olla 1-50 merkkiä")
                for choice in newchoices:
                    if choice == "" or len(choice) > 50:
                        return render_template("edit.html", quiz_id=id, quiz_type=quiz_type, topic=topic, questions=questions, \
                            choices=choices, nmr_of_questions=nmr_of_questions, nmr_of_choices=nmr_of_choices, \
                            message="Vaihtoehdossa tulee olla 1-50 merkkiä")
                if quiz_type == 1 and nmr_of_questions != len([x for x in newcorrect if x=="True"]):
                    return render_template("edit.html", quiz_id=id, quiz_type=quiz_type, topic=topic, questions=questions, \
                        choices=choices, nmr_of_questions=nmr_of_questions, nmr_of_choices=nmr_of_choices, \
                        message="Oikeita vastauksia tulee olla 1 per kysymys")
                quiz_id = quizzes.edit_topic(id, newtopic)
                i = 0
                for question in newquestions:
                    question_id = quizzes.edit_question(id, question)
                    for choice in range(int(nmr_of_choices)):
                        quizzes.edit_choice(choice_ids[i], question_id, newchoices[i], newcorrect[i])
                        i += 1
                return redirect("/quizzes")
        return render_template("error.html", message="Sinulla ei ole oikeuksia muokata kyselyitä", route="/")
    return render_template("error.html", message="Et ole kirjautunut sisään", route="/")

@app.route("/remove", methods=["GET", "POST"])
def remove():
    if users.user_id():
        if users.require_role(2):
            all_quizzes = quizzes.get_all_quizzes()
            if request.method == "GET":
                return render_template("remove.html", list=all_quizzes)
            if request.method == "POST":
                users.check_csrf()
                if "quiz" in request.form:
                    quiz = request.form["quiz"]
                    quizzes.remove_quiz(quiz)
                    return redirect("/")
                return render_template("remove.html", list=all_quizzes, message=True)
        return render_template("error.html", message="Sinulla ei ole oikeuksia poistaa kyselyitä", route="/")
    return render_template("error.html", message="Et ole kirjautunut sisään", route="/")

@app.route("/settings")
def settings():
    if users.user_id():
        time = users.registration_time()
        return render_template("settings.html", time=time)
    return render_template("error.html", message="Et ole kirjautunut sisään", route="/")

@app.route("/delete", methods=["GET", "POST"])
def delete():
    if users.user_id():
        if request.method == "GET":
            return render_template("delete.html")
        if request.method == "POST":
            users.check_csrf()
            if "confirmation" in request.form:
                users.delete_user()
                return redirect("/")
            return render_template("delete.html", message=True)
    return render_template("error.html", message="Et ole kirjautunut sisään", route="/")
