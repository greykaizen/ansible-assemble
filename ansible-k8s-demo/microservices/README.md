# Microservices

This directory contains the Python Flask microservices for the demo.

## Services

### app1 - User Management Service
- **Port:** 8080
- **Purpose:** User management API
- **Endpoints:**
  - `GET /` - Service information
  - `GET /health` - Health check
  - `GET /info` - Service details
  - `GET /users` - List all users
  - `GET /users/<id>` - Get user by ID
  - `POST /users` - Create new user

### app2 - Product Catalog Service
- **Port:** 8081
- **Purpose:** Product catalog API
- **Endpoints:**
  - `GET /` - Service information
  - `GET /health` - Health check
  - `GET /info` - Service details
  - `GET /products` - List all products
  - `GET /products/<id>` - Get product by ID
  - `GET /products/<id>/stock` - Get product stock
  - `POST /products` - Create new product

## Building Images

### Using the Build Script

```bash
./scripts/build-images.sh
```

### Manual Build

```bash
# Set Minikube Docker environment
eval $(minikube docker-env)

# Build app1
cd microservices/app1
docker build -t app1:latest .

# Build app2
cd ../app2
docker build -t app2:latest .
```

## Testing Locally

### Run app1 locally

```bash
cd microservices/app1
pip install -r requirements.txt
python app.py
```

Then visit: http://localhost:8080

### Run app2 locally

```bash
cd microservices/app2
pip install -r requirements.txt
python app.py
```

Then visit: http://localhost:8081

## Docker Images

The images are built using Minikube's Docker daemon so they're available to the Kubernetes cluster without pushing to a registry.

## Dependencies

- Python 3.11+
- Flask 3.0.0
- Gunicorn 21.2.0

