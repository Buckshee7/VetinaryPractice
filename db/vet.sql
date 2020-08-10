DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS vets;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    img_url VARCHAR(255)
);

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    phone varchar(255),
    registered BOOLEAN
);

CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    img_url VARCHAR(255),
    dob VARCHAR(255),
    animal_type VARCHAR(255),
    owner_id INT REFERENCES owners(id),
    vet_id INT REFERENCES vets(id) ON DELETE SET NULL 
);