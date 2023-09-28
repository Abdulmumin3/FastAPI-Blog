# FastAPI Blog API

The FastAPI Blog API is a web application that provides CRUD (Create, Read, Update, Delete) operations for managing information about blogs and Users. It is built using FastAPI and SQLAlchemy and Alembic for migrations and provides the following endpoints:

- `POST: http://localhost:8000/create-blog-posts`: Add new blogs to the database.
- `GET: http://localhost:8000/blog-posts`: Get all blogs from the database.
- `GET: http://localhost:8000/blog/{id}`: Retrieve a blog's information based on their unique id.
- `PUT: http://localhost:8000/update/{id}`: Update a blog's data by their id.
- `DELETE: http://localhost:8000/delete/{id}`: Delete a blog's data based on the entered id.
- `GET: http://localhost:8000/blog/{id}`: Retrieve a blog's information based on their unique id.
- `PUT: http://localhost:8000/update/{id}`: Update a blog's data by their id.
- `DELETE: http://localhost:8000/delete/{id}`: Delete a blog's data based on the entered id.

Users

- `POST: http://localhost:8000/create-user`: Add new users to the database.
- `GET: http://localhost:8000/user/{id}`: Retrieve a user's information based on their unique id.
- `GET: http://localhost:8000/users`: Get all users from the database
- `DELETE: http://localhost:8000/user/{id}`: Delete a user's data based on the entered id.

## Getting Started

To run the FastAPI blog API on your local machine, follow these steps:

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/your-repo.git

   ```

2. Change to the project directory:

   ```bash
   cd your-repo

   ```

3. Create a virtualenv with any env tool of your choice

4. Install the required Python packages:

   ```bash
   pip install -r requirements.txt

   ```

Usage

1. Start the FastAPI application:

   ```bash
   uvicorn app:app --reload

   ```

2. Access the API using the provided endpoints:

- To use the swagger documentation: http://localhost:8000/docs
- To add a new blog: POST: http://localhost:8000/create-blog-posts
- To get all blogs: POST: http://localhost:8000/blog-posts
- To get a blog by id: GET: http://localhost:8000/blog/{user_id}
- To update a blog's data by id: PUT: http://localhost:8000/update/{user_id}
- To delete a blog by id: DELETE: http://localhost:8000/delete/{id}

Users

- To add a new user: POST: http://localhost:8000/create-user
- To get all users: GET: http://localhost:8000/users
- To get a user by id: PUT: http://localhost:8000/user/{id}
- To delete a blog by id: DELETE: http://localhost:8000/user/{id}

## Example 1

    POST: http://localhost:8000/create-blog-posts
    JSON: {
        "title": "1st Post",
        "body": "Hello World",
        "published": true,
        "created_at": datetime,
        "updated_at": datetime

    }

### Response

    {
        "title": "1st Post",
        "body": "Hello World",
        "published": true,
        "created_at": "2023-09-28T10:42:57.933Z",
        "updated_at": "2023-09-28T10:42:57.933Z"
    }

## Example 2

    GET: http://localhost:8000/blog/2afeb3c8-8d59-4883-8c82-8a04cf4c474d

### Response

    {
    "title": "1st Post",
    "body": "Hello World",
    "published": true,
    "created_at": "2023-09-28T10:46:10.104Z",
    "updated_at": "2023-09-28T10:46:10.104Z",
    "author": {
      "name": "string",
      "email": "string",
      "posts": []
      }
    }

## Users:

## Example 1

    POST: http://localhost:8000/create-blog-posts
    JSON: {
        "name": "string",
        "email": "string",
        "password": "string"
    }

### Response

    {
        "name": "string",
        "email": "string",
        "password": "string"
    }

## Example 2

    GET: http://localhost:8000/blog/2afeb3c8-8d59-4883-8c82-8a04cf4c474d

### Response

    {
        "name": "string",
        "email": "string",
        "posts": []

    }

## API Endpoints

### POST /create-blog-posts

    Use this endpoint to add new blogs to the database. Send a POST request with JSON data containing the blog's information .

### GET /blogs-post

    Retrieve all blogs from the database.

### GET /blog/{id}

    Retrieve a blog's information based on their unique id. Replace {id} in the URL with the blog's actual id.

### PUT /update/{id}

    Update a blog's data by their id. Replace {id} in the URL with the blog's actual id. Send a PUT request with JSON data containing the updated information.

### DELETE /blog/{id}

    Delete a blog's data based on the entered id. Replace {id} in the URL with the blog's actual id.

### Acknowledgments

- FastAPI: https://fastapi.tiangolo.com/
- SQLAlchemy: https://www.sqlalchemy.org/
- Feel free to customize this README to include your specific project details, such as repository links, installation instructions, and any additional information about your project's usage, contributors, or deployment instructions.
  GET /api/{id}
  Retrieve a blog's information based on their unique id. Replace {id} in the URL with the blog's actual id.
  PUT /api/{id}
  Update a blog's data by their id. Replace {id} in the URL with the blog's actual id. Send a PUT request with JSON data containing the updated information.
  DELETE /api/{id}
  Delete a blog's data based on the entered id. Replace {id} in the URL with the blog's actual id./{user_id}`: Delete a blog's data based on the entered id.
