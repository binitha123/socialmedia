1. Create a MySQL database:
  Create a new MySQL database and update the DATABASES configuration in settings.py
2. Apply database migrations:

    python manage.py makemigrations
    python manage.py migrate
3. Create a app

4. Run the development server:

    python manage.py runserver
Access the application:
Visit http://127.0.0.1:8000 in your web browser to access the application.


5. User Registration and Login:

Use browser to make POST requests to the http://127.0.0.1:8000/api/register/ endpoint to register new users.
Use browser to make POST requests to the http://127.0.0.1:8000/api/login/ endpoint to log in users.
User Profile Management:

Use Postman to make GET, PUT, and PATCH requests to the http://127.0.0.1:8000/api/profiles/<profile_id>/ .

Use Postman to make POST requests to the http://127.0.0.1:8000/api/posts/ endpoint to create new posts.
Use Postman to make POST requests to the http://127.0.0.1:8000/api/comments/ endpoint to add comments to posts.
Follow and Unfollow Users:

Use Postman to make POST requests to the http://127.0.0.1:8000/api/relationships/ endpoint to follow other users.
Search Functionality