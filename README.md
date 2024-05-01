# E-commerce App

- [E-commerce App](#e-commerce-app)
  - [Introduction](#introduction)
  - [Local Server Setup](#local-server-setup)
    - [Clone The Repository](#clone-the-repository)
  - [Backend Setup](#backend-setup)
    - [Install Dependencies](#install-dependencies)
    - [Create the Database, Tables and run the Server](#create-the-database-tables-and-run-the-server)
    - [Note](#note)
  - [Frontend Setup](#frontend-setup)
    - [Install Dependencies](#install-dependencies-1)
    - [Run the Server](#run-the-server)
  - [**EndPoints**](#endpoints)
  - [Technologies Used](#technologies-used)
  - [Authors](#authors)
  - [License](#license)

## Introduction

Welcome to the E-Commerce App. This document provides detailed information on setting up the server locally.

---

## Local Server Setup

### Clone The Repository

To get started with the local development environment, clone the repository:

```bash
$ git clone git@github.com:mashm3ll0w/commerce-app.git
$ cd commerce-app
```

## Backend Setup

### Install Dependencies

You can set up the environment using `venv`:

```bash

# cd into the backend directory
$ cd e-commerce-backend

# create Virtual Environment
$ python3 -m venv venv

# Activate Virtual Env
$ source venv/bin/activate

# Install Dependencies
$ pip install -r requirements.txt
```

### Create the Database, Tables and run the Server

```bash
$ python3 manage.py makemigrations

$ python3 manage.py migrate

$ python3 manage.py runserver
```

### Note
Add a `.env` file in the `e-commerce-backend` directory with these fields:
```bash
SECRET_KEY=
DEBUG=
ALLOWED_HOSTS=
CORS_ALLOWED_ORIGINS=
```


## Frontend Setup
### Install Dependencies

Install dependencies using `npm`:

```bash

# cd into the frontend directory
$ cd e-commercefrontend

# Install Dependencies
$ npm install
```

### Run the Server

```bash
$ npm start
```

## **EndPoints**
The backend is served at `http://127.0.0.1:8000`

The frontend is served at `http://127.0.0.1:3000`

## Technologies Used

- Backend Technologies - `Django`, `Django REST-Framework` `Django REST-Framework-JWT`
- Frontend Technologies - `React` `Redux` `Material UI`

## Authors

- [@Charles Swaleh](https://github.com/mashm3ll0w)

## License

MIT License
