DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS items;

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role TEXT NOT NULL
);

CREATE TABLE items(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    description TEXT,
    status TEXT NOT NULL,
    price NUMERIC(8,2) NOT NULL,
    quantity INTEGER NOT NULL
);