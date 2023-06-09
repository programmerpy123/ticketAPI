
# TicketAPI

TicketAPI is a RESTful API that provides endpoints for managing event tickets.

## Getting Started

To get started with this project, clone the repository to your local machine:

```bash
git clone https://github.com/programmerpy123/ticketAPI.git
```

After cloning the repository, navigate to the project directory and install the required dependencies:

```bash
cd ticketAPI
pip install -r requirements.txt
```

Next, run the database migrations to create the necessary tables:

```bash
python manage.py migrate
```

Finally, start the development server:

```bash
python manage.py runserver
```

## Endpoints

The following endpoints are available in the API:

### `/api/tickets/`

- `GET`: Get a list of all tickets
- `POST`: Create a new ticket

### `/api/tickets/{id}/`

- `GET`: Get details for a specific ticket
- `PUT`: Update a specific ticket
- `DELETE`: Delete a specific ticket

## Authentication

Some endpoints, such as creating and updating tickets, require authentication. To authenticate, include an `Authorization` header with a token obtained from the `/api/token/` endpoint.

For example:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"username":"user1", "password":"password123"}' http://localhost:8000/api/token/
```

This will return a JSON object containing an access token and a refresh token. Include the access token in the `Authorization` header for authenticated requests:

```bash
curl -H "Authorization: Bearer <access_token>" http://localhost:8000/api/tickets/
```

## Contributing

Contributions to this project are welcome! If you find a bug or have a feature request, please open an issue. If you'd like to contribute code, please fork the repository and submit a pull request.
