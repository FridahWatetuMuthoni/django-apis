# DJANGO APIS

## Git configuration

```sh
git config --global user.name "Your Name"
git config --global user.email "yourname@email.com"
git config --global init.defaultBranch main
```

## World Wide Wide

The internet is a system of interconnected computer networks that has existed since 1960.

## HTTP VERBS

CRUD => Create:POST, Read:GET, Update:UPDATE/PUT, Delete:DELETE

## CLIENT AND SERVER TCP CONNECTION

After the browser has the IP address for a given domain, it needs a way to set up a consistent connection with the desired server. This happens via the Transmission Control Protocol (TCP) which provides reliable, ordered, and error-checked delivery of bytes between two application.To establish a TCP connection between two computers, a three-way “handshake” occurs between the client and server:

1. The client sends a SYN asking to establish a connection.
2. The server responds with a SYN-ACK acknowledging the request and passing a connection parameter.
3. The client sends an ACK back to the server confirming the connection

## HTTP

HTTP is a request-response protocol between two computers that have an existing TCP connection. The computer making the requests is known as the client while the computer responding is known as the server. Typically a client is a web browser but it could also be an iOS app or really any internet-connected device. A server is a fancy name for any computer optimized to work over the internet. All we really need to transform a basic laptop into a server is some special software and a persistent internet connection.

1. 2xx Success - the action requested by the client was received, understood, and accepted
2. 3xx Redirection - the requested URL has moved
3. 4xx Client Error - there was an error, typically a bad URL request by the client
4. 5xx Server Error - the server failed to resolve a request

## static files configuration

```sh
mkdir static
python -m pip install whitenoise==6.0.0

```

```python

# django_project/settings.py

INSTALLED_APPS = [
...
"whitenoise.runserver_nostatic", # new
"django.contrib.staticfiles",
]

MIDDLEWARE = [
"django.middleware.security.SecurityMiddleware",
"django.contrib.sessions.middleware.SessionMiddleware",
"whitenoise.middleware.WhiteNoiseMiddleware", # new
...
]

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"] # new
STATIC_ROOT = BASE_DIR / "staticfiles" # new
STATICFILES_STORAGE ="whitenoise.storage.CompressedManifestStaticFilesStorage" # new

```

```sh

python manage.py collectstatic

```

## DEPLOYMENT CHECKLIST

1. install Gunicorn46 as the production web server
2. create a requirements.txt file
3. create a runtime.txt file
4. update the ALLOWED_HOSTS configuration
5. create a Procfile for Heroku
