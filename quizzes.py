from db import db

def get_quizzes():
    sql = "SELECT topic, id, quiz_type FROM quizzes"
    result = db.session.execute(sql)
    return result.fetchall()

def get_nmr_of_quizzes():
    sql = "SELECT COUNT(*) FROM quizzes"
    result = db.session.execute(sql)
    return result.fetchone()[0]
