# Flask CI/CD App

A simple Python Flask REST API built for a CI/CD pipeline demo using Jenkins and Kubernetes.

## Project Structure

```
flask-cicd-app/
├── app/
│   ├── __init__.py      # App factory
│   └── routes.py        # API endpoints
├── tests/
│   └── test_app.py      # Unit tests
├── run.py               # Entry point
├── requirements.txt     # Dependencies
├── Dockerfile           # Container build
└── README.md
```

## API Endpoints

| Method | Endpoint            | Description          |
|--------|---------------------|----------------------|
| GET    | `/`                 | Welcome message      |
| GET    | `/health`           | Health check         |
| GET    | `/api/greet/<name>` | Greet by name        |

## Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Start the app
python run.py
```

## Run Tests

```bash
pytest tests/
```

## Run with Docker

```bash
docker build -t flask-cicd-app .
docker run -p 5000:5000 flask-cicd-app
```
