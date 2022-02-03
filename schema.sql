CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role INTEGER,
    created_at TIMESTAMP
);

CREATE TABLE polls (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    poll_id INTEGER REFERENCES polls,
    question TEXT
);

CREATE TABLE choices (
    id SERIAL PRIMARY KEY,
    question_id INTEGER REFERENCES questions,
    choice TEXT,
    correct Boolean
);

CREATE TABLE answers (
    user_id INTEGER REFERENCES users,
    choice_id INTEGER REFERENCES choices
);