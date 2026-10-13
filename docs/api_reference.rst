API Reference
=============

This section documents the REST API endpoints available in the News Capstone application.

Authentication
--------------

The API uses JWT (JSON Web Token) authentication. Users must obtain a token before accessing protected endpoints.

Obtain Token
~~~~~~~~~~~~

**POST** ``/api/token/``

Request Body:

.. code-block:: json

   {
       "username": "your_username",
       "password": "your_password"
   }

Response:

.. code-block:: json

   {
       "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
       "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
   }

Article Endpoints
-----------------

List Articles
~~~~~~~~~~~~~

**GET** ``/api/articles/``

Returns a list of all approved articles.

Headers:

.. code-block:: http

   Authorization: Bearer <your_access_token>

Response:

.. code-block:: json

   [
       {
           "id": 1,
           "title": "Sample Article",
           "content": "Article content here...",
           "author": "username",
           "created_at": "2026-10-14T12:00:00Z"
       }
   ]

Create Article
~~~~~~~~~~~~~~

**POST** ``/api/articles/``

Creates a new article (requires authentication).

Headers:

.. code-block:: http

   Authorization: Bearer <your_access_token>
   Content-Type: application/json

Request Body:

.. code-block:: json

   {
       "title": "New Article",
       "content": "Article content..."
   }

Approve Article
~~~~~~~~~~~~~~~

**POST** ``/api/approve/<article_id>/``

Approves an article and triggers email notifications to subscribers.

Headers:

.. code-block:: http

   Authorization: Bearer <your_access_token>

Models
------

Article
~~~~~~~

.. autoclass:: news.models.Article
   :members:
   :undoc-members:
   :show-inheritance:

Newsletter
~~~~~~~~~~

.. autoclass:: news.models.Newsletter
   :members:
   :undoc-members:
   :show-inheritance:

Publisher
~~~~~~~~~

.. autoclass:: news.models.Publisher
   :members:
   :undoc-members:
   :show-inheritance:

Serializers
-----------

ArticleSerializer
~~~~~~~~~~~~~~~~~

.. autoclass:: news.serializers.ArticleSerializer
   :members:
   :undoc-members:

Views
-----

ArticleViewSet
~~~~~~~~~~~~~~

.. autoclass:: news.views.ArticleViewSet
   :members:
   :undoc-members:
   