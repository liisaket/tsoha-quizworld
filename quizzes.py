from db import db
import users

def get_quizzes():
    sql = "SELECT topic, id, quiz_type FROM quizzes"
    result = db.session.execute(sql)
    return result.fetchall()

def get_nmr_of_quizzes():
    sql = "SELECT COUNT(*) FROM quizzes"
    result = db.session.execute(sql)
    return result.fetchone()[0]

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
