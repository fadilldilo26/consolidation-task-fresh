Welcome to News Capstone Documentation!
========================================

This project consolidates version control, containerization, and comprehensive documentation using Sphinx and Docker.

The News Capstone application is a Django-based REST API that allows users to manage news articles, including creating, editing, and approving content. It features user authentication, email notifications, and a robust API for external integrations.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api_reference

Project Overview
================

Features
--------

- **User Authentication**: Secure login and registration using JWT tokens.
- **Article Management**: Create, edit, and approve news articles.
- **Email Notifications**: Automatic email alerts when articles are approved.
- **REST API**: Full API access for external applications.
- **Docker Support**: Easy deployment using Docker and Docker Compose.
- **MySQL Database**: Production-ready database configuration.

Tech Stack
----------

- **Backend**: Django 4.2 + Django REST Framework
- **Database**: MySQL 8.0
- **Documentation**: Sphinx
- **Containerization**: Docker & Docker Compose
- **Python**: 3.12

Getting Started
===============

Prerequisites
-------------

- Docker and Docker Compose installed
- Git installed

Installation
------------

1. Clone the repository::

   git clone https://github.com/faadhil126/consolidation-task-fresh.git
   cd consolidation-task-fresh

2. Switch to the container branch::

   git checkout container

3. Build and run the application::

   docker-compose up --build

4. Open your browser and navigate to::

   http://localhost:8000

Running Migrations
------------------

If the database is empty, run migrations::

   docker-compose run --rm web python manage.py migrate

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`