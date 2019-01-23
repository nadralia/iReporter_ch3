-- Table: public.users

-- DROP TABLE public.users;

CREATE TABLE IF NOT EXISTS users (
                user_id SERIAL PRIMARY KEY NOT NULL,
                firstname VARCHAR (40) NOT NULL,
                lastname VARCHAR (40) NOT NULL,
                othernames VARCHAR(40),
                email VARCHAR(60) UNIQUE NOT NULL,
                username VARCHAR (40) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,
                phonenumber VARCHAR(14) UNIQUE NOT NULL,
                gender VARCHAR(14) NOT NULL,
                is_admin VARCHAR (5) DEFAULT 'false',
                registered TIMESTAMP WITH TIME ZONE DEFAULT now(),
                updatedOn TIMESTAMP WITH TIME ZONE DEFAULT now()
            )