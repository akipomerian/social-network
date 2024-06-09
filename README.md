# social-network
Social network app
# Social Network API

## Setup

1. Clone the repository
2. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```
3. Configure the database settings in `settings.py`
4. Apply migrations
    ```bash
    python manage.py migrate
    ```
5. Create a superuser
    ```bash
    python manage.py createsuperuser
    ```
6. Run the server
    ```bash
    python manage.py runserver
    ```

## Docker Setup

1. Build and run containers
    ```bash
    docker-compose up --build
    ```

## API Endpoints

- **Signup:** `POST /api/register/`
- **Login:** `POST /api/login/`
- **Search Users:** `GET /api/users/search/?query=keyword`
- **Friend Requests:**
  - **Send Request:** `POST /api/friendrequests/`
  - **Accept/Reject Request:** `PUT /api/friendrequests/:id/`
  - **List Pending Requests:** `GET /api/friendrequests/`
- **List Friends:** `GET /api/friends/`
