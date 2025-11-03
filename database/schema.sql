CREATE TYPE status_type AS ENUM (
    'pending',
    'in progress',
    'completed',
    'deleted'
);



CREATE TABLE todo (
    id SERIAL PRIMARY KEY,
    title Text UNIQUE NOT NULL,
    description Text UNIQUE NOT NULL,
    start_date TIMESTAMP,
    end_date TIMESTAMP,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
    CONSTRAINT fk_user
        FOREIGN KEY (user_id) 
        REFERENCES user (id)
        ON DELETE CASCADE
);



CREATE TABLE user (
    id SERIAL PRIMARY KEY,
    name Text,
    email Text UNIQUE,
    password Text,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now()
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT now(),

);


CREATE TABLE sub-todo (
    id SERIAL PRIMARY KEY,
    title Text UNIQUE NOT NULL,
    description Text UNIQUE NOT NULL,
    start_date TIMESTAMP,
    end_date TIMESTAMP,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT now(),

);









