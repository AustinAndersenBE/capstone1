# Vocab Project

This Flask web application assists users in learning new vocabulary words. It features user registration and login, vocabulary API endpoints, and interactive sentence creation, deletion, and upvoting.

## Main Tools Used

- Flask
- bcrypt
- Flask-SQLAlchemy
- Flask-WTF
- Jinja2
- WTForms

## Features

### User Features

- **User Registration and Login:** Allows users to create an account and log in.

### Vocabulary Features

- **Vocabulary API Endpoints:** Users can access vocabulary words through API endpoints.
- **Sentence Creation and Deletion:** Users can create and delete sentences using the vocabulary words.
- **Upvoting Sentences:** Users can upvote sentences created by others.

## Setup

To set up this project, ensure you have Python, Flask, and PostgreSQL installed.

1. **Clone the repository.**

2. **Install Dependencies:**

pip install -r requirements.txt

3. **Set Up the Database:**

createdb vocab_project


4. **Run the Server.**

## API Endpoints

- `GET /api/vocab/<level>`: Returns 7 random words from the database at the specified level.
- `GET /api/definitions/<word_id>`: Returns the definitions of a word.
- `GET /api/vocab_words`: Returns all vocabulary words.

## Routes

- `GET, POST /login`: User login page.
- `GET, POST /register`: User registration page.
- `GET /`: Home page.
- `GET /learn`: Learn page.
- `GET /sentences`: Sentences page.
- `GET, POST /sentences/new`: Sentence creation page.
- `POST /upvote/<int:sentence_id>`: Upvote a sentence.
- `POST /delete_sentence/<int:sentence_id>`: Delete a sentence.

## External API Integration

This project integrates with the [Dictionary API](https://dictionaryapi.dev/) to provide definitions for the vocabulary words.

### API Endpoint

- `https://api.dictionaryapi.dev/api/v2/entries/en/{word}`

## Database Models

- **User:** Represents a user.
- **Vocab:** Represents a vocabulary word.
- **Definition:** Represents a definition of a vocabulary word.
- **Sentence:** Represents a sentence.
- **SentenceVocab:** Relationship between a sentence and a vocabulary word.
- **SentenceUpvotes:** Relationship between a sentence and a user.

## Forms

- **RegistrationForm:** For user registration.
- **LoginForm:** For user login.
- **SentenceForm:** For sentence creation.

## Helpers

- **authenticate_user:** Authenticates a user.
- **create_user:** Creates a new user.

## Configuration

Environment variables:

- `DATABASE_URL`: URL of the PostgreSQL database.
- `SECRET_KEY`: Secret key for Flask sessions.
