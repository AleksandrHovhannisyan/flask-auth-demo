# Flask authentication demo

This is a toy project that explores authenticating users with the Flask micro-framework. I coded this by following Miguel Grinberg's excellent [Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world), parts 1–5.

## Getting Started

Prerequisites:

- Python 3

Installation:

1. Run `source env/bin/activate` to enter the virtual environment.
2. Run `pip install` to install the project dependencies.
3. Run `source devcert.sh` to generate a self-signed certificate (for HTTPS).
4. Run `python -m app` to start the Flask server on `localhost:5000`.

## Routes/Views

- `/`: index route with log-in and registration links.
- `/login`: allows users to log in with valid credentials.
- `/register`: allows users to create a new account.
- `/dashboard`: restricted view that requires login.
- `/logout`: logs out the user, clearing their persistent remember-me cookie.
