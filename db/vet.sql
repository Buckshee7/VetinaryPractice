DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS vets;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    img_url VARCHAR(255)
);

CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob VARCHAR(255),
    animal_type VARCHAR(255),
    owner_name VARCHAR(255),
    owner_phone VARCHAR(255),
    treatment_notes TEXT,
    vet_id INT REFERENCES vets(id) ON DELETE SET NULL 
);