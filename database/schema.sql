CREATE TYPE status_type AS ENUM (
    'pending',
    'in_progress',
    'completed',
    'deleted'
);



CREATE TABLE todo (
    id SERIAL PRIMARY KEY,
    title Text UNIQUE NOT NULL,
    description Text UNIQUE NOT NULL,
    start_date TIMESTAMP,
    end_date TIMESTAMP,
    status status_type DEFAULT'pending',
   
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
    user_id Int,
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
    status status_type DEFAULT'pending',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
    CONSTRAINT fk_todo
        FOREIGN KEY (todo_id) 
        REFERENCES todo (id)
        ON DELETE CASCADE

);









