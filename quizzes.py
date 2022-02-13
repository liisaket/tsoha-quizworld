from db import db
import users

def get_quizzes(quiz_type):
    sql = "SELECT topic, id FROM quizzes WHERE quiz_type=:quiz_type"
    result = db.session.execute(sql, {"quiz_type":quiz_type})
    return result.fetchall()

def get_undone_quizzes():
    user = users.user_id()
    sql = "SELECT q.topic, q.id FROM quizzes q WHERE q.id NOT IN \
        (SELECT q.id FROM quizzes q \
        JOIN questions que ON q.id=que.quiz_id \
        JOIN choices c on que.id=c.question_id \
        JOIN answers a ON c.id=a.choice_id \
        JOIN users u ON a.user_id=u.id \
        WHERE u.id=:user)"
    result = db.session.execute(sql, {"user":user})
    return result.fetchall()

def get_done_quizzes():
    user = users.user_id()
    sql = "SELECT DISTINCT q.topic, q.id FROM choices c \
        JOIN answers a ON c.id=a.choice_id \
        JOIN users u ON a.user_id=u.id \
        JOIN questions que ON c.question_id=que.id \
        JOIN quizzes q ON que.quiz_id=q.id \
        WHERE u.id=:user"
    result = db.session.execute(sql, {"user":user})
    return result.fetchall()

def get_topics():
    sql = "SELECT topic FROM quizzes"
    result = db.session.execute(sql)
    return [row[0] for row in result.fetchall()]

def get_nmr_of_quizzes():
    sql = "SELECT COUNT(*) FROM quizzes"
    result = db.session.execute(sql)
    return result.fetchone()[0]

def get_quiz_topic(id):
    sql = "SELECT topic FROM quizzes WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()[0]

def get_quiz_type(id):
    sql = "SELECT quiz_type FROM quizzes WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()[0]

def get_questions(id):
    sql = "SELECT id, content FROM questions where quiz_id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()

def get_choices(questions):
    question_ids = [question[0] for question in questions]
    sql = "SELECT id, content, question_id, correct FROM choices WHERE question_id IN :questions"
    result = db.session.execute(sql, {"questions":tuple(question_ids)})
    return result.fetchall()

def store_user_answers(choice_ids):
    user = users.user_id()
    for choice in choice_ids:
        sql = "INSERT INTO answers (user_id, choice_id) VALUES (:user, :choice)"
        db.session.execute(sql, {"user":user, "choice":choice})
    db.session.commit()

def get_user_answers(id):
    user = users.user_id()
    sql = "SELECT c.id FROM choices c JOIN answers a ON c.id=a.choice_id \
        JOIN users u ON a.user_id=u.id \
        JOIN questions q ON c.question_id=q.id \
        JOIN quizzes qz ON q.quiz_id=qz.id \
        WHERE qz.id=:id AND u.id=:user"
    result = db.session.execute(sql, {"id":id, "user":user})
    return [row[0] for row in result.fetchall()]

def user_right_answers(id):
    user = users.user_id()
    sql = "SELECT COUNT(c.id) FROM choices c \
        JOIN answers a ON c.id=a.choice_id \
        JOIN users u ON a.user_id=u.id \
        JOIN questions q ON c.question_id=q.id \
        JOIN quizzes qz ON q.quiz_id=qz.id \
        WHERE qz.id=:id AND u.id=:user AND c.correct"
    result = db.session.execute(sql, {"id":id, "user":user})
    return result.fetchone()[0]

def get_poll_choices(id):
    sql = "SELECT c.id, c.question_id, c.content, COUNT(a.id) FROM choices c \
        LEFT JOIN answers a ON c.id=a.choice_id \
        LEFT JOIN users u ON a.user_id=u.id \
        LEFT JOIN questions q ON c.question_id=q.id \
        LEFT JOIN quizzes qz ON q.quiz_id=qz.id \
        WHERE qz.id=:id GROUP BY c.id ORDER BY c.id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()

def create_quiz(topic, quiz_type):
    sql = "INSERT INTO quizzes (topic, quiz_type) VALUES (:topic, :quiz_type) RETURNING id"
    result = db.session.execute(sql, {"topic":topic,"quiz_type":quiz_type})
    db.session.commit()
    return result.fetchone()[0]

def create_question(quiz_id, question):
    sql = "INSERT INTO questions (content, quiz_id) VALUES (:content, :quiz_id) RETURNING id"
    result = db.session.execute(sql, {"content":question, "quiz_id":quiz_id})
    db.session.commit()
    return result.fetchone()[0]

def create_choice(question_id, choice, correct):
    sql = "INSERT INTO choices (question_id, content, correct) VALUES (:question_id, :content, :correct)"
    db.session.execute(sql, {"question_id":question_id, "content":choice, "correct":correct})
    db.session.commit()

def delete_quiz():
    pass
