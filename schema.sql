CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role INTEGER,
    created_at TIMESTAMP
);

CREATE TABLE quizzes (
    id SERIAL PRIMARY KEY,
    topic TEXT,
    quiz_type INTEGER
);

CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    quiz_id INTEGER REFERENCES quizzes,
    content TEXT
);

CREATE TABLE choices (
    id SERIAL PRIMARY KEY,
    question_id INTEGER REFERENCES questions,
    content TEXT,
    correct Boolean
);

CREATE TABLE answers (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    choice_id INTEGER REFERENCES choices
);