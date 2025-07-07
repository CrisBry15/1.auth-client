What does it do?

This microservice is responsible for registering the client or organizer; both handle POST requests. 
It allows registration and login to the system; all information is sent to the MySQL database.

### Design Patterns Used:
- **Application Factory Pattern**: Modular Flask app creation with factory function
- **Blueprint Pattern**: Organized route management using Flask Blueprints
- **Configuration Pattern**: Environment-based settings management
- **Repository Pattern (Simplified)**: Direct database operations in controller functions
- **Layered Architecture**: Clear separation of concerns across presentation, application, business logic, and data access layers

## Communication Protocol

### REST API Protocol:
- **HTTP Methods**: GET, POST for different operations
- **Data Format**: JSON for request/response payloads
- **Authentication**: Bearer token in Authorization header
- **Content-Type**: application/json
- **Status Codes**: Standard HTTP status codes (200, 201, 400, 401, 409, 500)

### API Endpoints:
- `GET /auth/` - Health check endpoint
- `POST /auth/register` - User registration with JSON payload
- `POST /auth/login` - User authentication returning JWT token
- `GET /auth/protected` - Protected resource requiring JWT 

## Architectural Design

### Layered Architecture:
```
┌─────────────────────────────────────┐
│        Presentation Layer           │
│  (HTML Templates + Static Files)    │
├─────────────────────────────────────┤
│         Application Layer           │
│  (Routes + Controllers)             │
├─────────────────────────────────────┤
│      Business Logic Layer           │
│  (Utils + Models)                   │
├─────────────────────────────────────┤
│      Data Access Layer              │
│  (MySQL Database)                   │
└─────────────────────────────────────┘

## Framework

### Technology Stack:
- **Web Framework**: Flask 3.1.1 (Python)
- **Database**: MySQL with mysql-connector-python
- **Authentication**: Flask-JWT-Extended for JWT tokens
- **Security**: bcrypt for password hashing
- **Frontend**: Bootstrap 5.3.0, HTML5, CSS3, Vanilla JavaScript
- **Containerization**: Docker
- **Testing**: pytest
- **Configuration**: python-dotenv for environment variables
- **CORS**: Flask-CORS for cross-origin requests