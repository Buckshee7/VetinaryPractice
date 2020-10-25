# VeterinaryPractice
Full stack administration site for vetinary practice

## Purpose/Brief
"A veterinary practice has approached you to build a web application to help them manage their animals and vets. A vet may look after many animals at a time. An animal is registered with only one vet."

#### MVP

- The practice wants to be able to register / track animals. Important information for the vets to know is -
  - Name
  - Date Of Birth (use a VARCHAR initially)
  - Type of animal
  - Contact details for the owner
  - Treatment notes
- Be able to assign animals to vets
- CRUD actions for vets / animals

#### Extensions achieved
- Mark owners as being registered/unregistered with the Vet. unregistered owners won't be able to add any more animals.
- If an owner has multiple animals we don't want to keep updating contact details separately for each pet. Extend your application to reflect that an owner can have many pets and to more sensibly keep track of owners' details (avoiding repetition / inconsistencies)
- Assigning treatments, a more comprehensive way of maintaining treatment notes over time.

## Prerequisites / Technologies used
**Flask:** Use package manager pip3 to install Flask

```bash
pip3 install flask
```

**Psycopg2:** Use package manager pip3 to install Psycopg2

```bash
pip3 install psycopg2
```

**Datetime:** This module is built-in the pythons default module library

## Set-Up
Create database

```bash
dropdb vet
createdb vet
```

Set-up database tables

```bash
python3 db/vet.sql
```

Seed database if required

```bash
python3 console.py
```

Run flask
```bash
flask run
```
