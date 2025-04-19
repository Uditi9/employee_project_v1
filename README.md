# Employee Project

## Setup Instructions

1. Copy `.env_example` to `.env` and update your credentials.
2. Build and run the Docker containers:

```bash
docker-compose up --build
```

3. Apply migrations and generate data:

```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py generate_data
```

4. Access the app:
   - API: http://localhost:8000/api/
   - Swagger UI: http://localhost:8000/swagger/
   - Health Check: http://localhost:8000/health/
   - Performance chart: http://localhost:8000/performance-chart/

## Features

- Synthetic employee data generation (Faker)
- PostgreSQL integration
- REST APIs with filtering, pagination, authentication
- Swagger UI (drf-yasg)
- CSV export endpoint
- Health check endpoint
- view performance chart - /performance-chart/

  ##credentials
username - admin
password - admin
