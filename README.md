# AI Interviewer System

An AI-powered Django web application that automates technical interviews by generating interview questions from job descriptions, evaluating candidate answers using an LLM, and managing candidate workflows with authentication, admin approval, and email notifications.

This project also supports **Single Sign-On (SSO)** using **Keycloak**, integrated with Django through **Authlib**, with Keycloak running locally using **Docker**.

---

## Overview

The AI Interviewer System is designed to simulate and automate technical interview rounds. It generates questions based on a job description, evaluates answers using an AI model, calculates candidate performance, and determines whether the candidate is qualified or disqualified.

The application includes:

- AI-based interview question generation
- Automated answer evaluation
- Multi-step interview flow
- Final qualification decision
- User authentication and admin approval
- OTP-based password reset
- Email notifications
- Keycloak SSO integration

---

## Features

### AI Interview Features
- Generates interview questions dynamically from the job description
- Evaluates candidate answers using an AI model
- Assigns scores based on answer quality and relevance
- Supports multi-step interview rounds
- Calculates the final result using average score

### Result Logic
- **Average Score ≥ 3** → Qualified
- **Average Score < 3** → Disqualified

### Authentication Features
- User registration
- Admin approval for account activation
- Session-based login
- OTP-based password reset
- Keycloak Single Sign-On (SSO) using Authlib

### Admin Features
- Activate or deactivate users
- Delete users
- Monitor registered users
- Review candidate results

### Notification Features
- Email-based OTP verification
- Email notification for interview results

---

## Technology Stack

**Backend**
- Python
- Django

**AI / LLM**
- Google Gemini API
- LangChain

**Database**
- SQLite

**Frontend**
- HTML
- CSS

**Authentication**
- Django session authentication
- Keycloak SSO
- Authlib
- OpenID Connect (OIDC)

**Other Services**
- SMTP email service
- Docker (for running Keycloak locally)

---

## Project Structure

```bash
AI_Interviewer/
│
├── AI_Interviewer/         # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── users/                  # Main Django app
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── templates/              # HTML templates
├── media/                  # Uploaded files
├── db.sqlite3              # SQLite database
├── manage.py               # Django management script
├── README.md               # Project documentation
└── req.txt                 # Python dependencies
```
-------
## How It Works
1. User Authentication

* Users can access the system either through the normal login flow or via Keycloak SSO.

* After login:

    - Django creates a user session
    - The user is redirected into the application
2. Interview Flow
* Candidate enters a job description
* The AI generates a technical interview question
* Candidate submits an answer
* The AI evaluates the answer and assigns a score
* The process repeats for multiple questions
* The system calculates the average score
* Final result is shown as Qualified or Disqualified

3. Email Notifications
* OTP is sent for password reset
* Interview results can be sent by email

------
## SSO with Keycloak

This project supports Single Sign-On (SSO) using Keycloak as the identity provider and Authlib for Django integration.

**Authentication Flow**
- User clicks login with SSO
- Django redirects to Keycloak
- Keycloak authenticates the user
- Django receives the callback
- User details are stored in session
- User is redirected into the application
-----

## Running Keycloak with Docker

You can run Keycloak locally using Docker:
```bash
docker run -d --name keycloak ^
  -p 8080:8080 ^
  -e KC_BOOTSTRAP_ADMIN_USERNAME=admin ^
  -e KC_BOOTSTRAP_ADMIN_PASSWORD=admin123 ^
  quay.io/keycloak/keycloak:latest ^
  start-dev
```
### Open Keycloak Admin Console
```bash 
http://localhost:8080 
```
Example Keycloak Setup

Create:

* Realm: sso-demo
* Client: ai-interviewer-client

Add the following in Keycloak client settings:

Valid Redirect URIs
```bash
http://127.0.0.1:8000/auth/callback/
http://localhost:8000/auth/callback/
```
Web Origins
```bash

http://127.0.0.1:8000
http://localhost:8000
```

Valid Post Logout Redirect URIs

```bash

http://127.0.0.1:8000/
http://localhost:8000/

```
------
## Environment Variables

Store secrets and configuration in a .env file placed in the same folder as manage.py.

Example:

* SECRET_KEY=your-django-secret-key
* DEBUG=True
* ALLOWED_HOSTS=127.0.0.1,localhost

* KEYCLOAK_CLIENT_ID=ai-interviewer-client
* KEYCLOAK_CLIENT_SECRET=your-keycloak-client-secret
* KEYCLOAK_SERVER_METADATA_URL=http://localhost:8080/realms/sso-demo/.well-known/openid-configuration
* KEYCLOAK_SCOPE=openid profile email

* CSRF_TRUSTED_ORIGINS=http://127.0.0.1:8000,http://localhost:8000

-----

## Local Setup
1. Clone the Repository
```bash
git clone https://github.com/Friendlysiva143/AI_Interviewer.git
cd AI_Interviewer
```
2. Create Virtual Environment
```bash
python -m venv venv
```
3. Activate Virtual Environment

Windows
```bash
venv\Scripts\activate
```
Linux / Mac

source venv/bin/activate
4. Install Dependencies
```bash
pip install -r req.txt
```
5. Apply Database Migrations
```bash
python manage.py migrate
```
6. Run Django Server

```bash
python manage.py runserver

```

Open in browser:
```bash
http://127.0.0.1:8000/

```

7. Start Keycloak with Docker

Run Keycloak separately using Docker, then configure the realm and client.

### Main Functional Flow
* User registers on the platform
* Admin activates the user account
* User logs in to the system or uses SSO
* Candidate enters the job description
* The AI generates a technical interview question
* Candidate submits an answer
* AI evaluates the answer and assigns a score
* The process repeats for multiple questions
* The system calculates the average score
* Candidate receives the final result

Example Evaluation

Example Question

What is the difference between a list and a tuple in Python?

Example Output: 

{
  "score": 4,
  "qualified": true
}


## Future Improvements
* Deploy Keycloak on a public server for production SSO
* Replace SQLite with PostgreSQL for production
* Add detailed interview analytics dashboard
* Add role-based access control
* Add interview history tracking
* Improve UI responsiveness
* Add video/audio interview support
* Add REST APIs for integration

Security Note

For production deployment:

* do not hardcode secrets in source code
* store secrets in environment variables
* use HTTPS
* configure trusted origins properly
* host Keycloak on a public server
* update callback and logout URLs for production domain

**Author**

Siva Prasad

GitHub: https://github.com/sivaprasadkandena/


**License**

This project is for learning, academic, and portfolio purposes.