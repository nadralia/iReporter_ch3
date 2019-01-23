-- Table: public.incidents

-- DROP TABLE public.incidents;

CREATE TABLE IF NOT EXISTS incidents (
                incident_id SERIAL PRIMARY KEY NOT NULL,
				createdBy INTEGER REFERENCES users(user_id),
				incident_type VARCHAR(12) NOT NULL,
				status VARCHAR(13) DEFAULT 'drafted', 
				latitude VARCHAR(25) NOT NULL,
				longitude VARCHAR(25) NOT NULL,
				images VARCHAR(100),
				videos VARCHAR(100),
			    comment VARCHAR(255) NOT NULL,
				createdOn TIMESTAMP WITH TIME ZONE DEFAULT now(),
				updatedOn TIMESTAMP WITH TIME ZONE DEFAULT now()
				)