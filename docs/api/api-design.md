# M2.8 API Design

## 1. Overview

The API design defines the communication contract between the frontend application, backend services, AI processing services, and external clients.

The API follows:

- RESTful architecture
- Secure authentication
- Role-based authorization
- Real-time communication through WebSockets
- Clear request and response contracts


Technology:

- FastAPI
- Pydantic
- JWT Authentication


---

# 2. API Architecture



Frontend Application

    |

    |

 HTTPS API

    |

    |

API Gateway

    |

    |

Business Services

    |

    |

Database / AI Services


---

# 3. Base API Information


## Base URL


Development:


http://localhost:8000/api/v1



Production:


https://domain.com/api/v1



---

# 4. Authentication Requirements


All protected API endpoints require:


HTTP Header:


Authorization: Bearer <JWT_TOKEN>



Authentication provides:

- User identity
- User role
- Access permissions


---

# 5. Authentication API


## POST /auth/login


Purpose:

Authenticate users and generate access tokens.


Request:


```json
{
  "email": "user@example.com",
  "password": "password"
}

Response:

{
  "access_token": "jwt_token",
  "refresh_token": "refresh_token",
  "token_type": "bearer"
}

Authentication:

Public

POST /auth/refresh

Purpose:

Generate a new access token using refresh token.

Request:

{
  "refresh_token": "token"
}

Response:

{
  "access_token": "new_token"
}

Authentication:

Public with valid refresh token

GET /auth/me

Purpose:

Retrieve current authenticated user information.

Response:

{
  "id": "uuid",
  "email": "user@example.com",
  "role": "Admin"
}

Authentication:

Required

6. User Management API
GET /users

Purpose:

Retrieve all system users.

Permissions:

Admin

Response:

[
 {
  "id": "uuid",
  "email": "admin@example.com",
  "role": "Admin"
 }
]
POST /users

Purpose:

Create a new user.

Permissions:

Admin

Request:

{
 "email":"new@example.com",
 "role":"Viewer"
}
PUT /users/{id}

Purpose:

Update user information.

Permissions:

Admin
DELETE /users/{id}

Purpose:

Remove a user account.

Permissions:

Admin
7. Camera Management API
GET /cameras

Purpose:

Retrieve registered cameras.

Response:

[
 {
  "id":"camera_001",
  "name":"Production Camera",
  "status":"online"
 }
]

Authentication:

Required

POST /cameras

Purpose:

Register a new camera.

Request:

{
"name":"Camera A",
"location":"Factory Area A",
"source_type":"RTSP",
"url":"camera_stream_url"
}

Permissions:

Admin
Safety Officer
PUT /cameras/{id}

Purpose:

Update camera configuration.

DELETE /cameras/{id}

Purpose:

Remove camera from system.

Permissions:

Admin
8. Violation Management API
GET /violations

Purpose:

Retrieve safety violations.

Query Parameters:

camera_id

type

date_from

date_to


Response:

[
 {
  "id":"violation_001",
  "type":"Missing Helmet",
  "confidence":0.95,
  "timestamp":"2026-01-01"
 }
]
GET /violations/{id}

Purpose:

Retrieve detailed violation information.

Response:

{
"id":"violation_001",
"camera_id":"camera_001",
"type":"Missing Helmet",
"confidence":0.95,
"snapshot":"path"
}
PATCH /violations/{id}

Purpose:

Update violation status.

Examples:

Reviewed

Resolved

Ignored


Permissions:

Safety Officer
Admin
9. Reports API
GET /reports

Purpose:

Generate safety reports.

Possible filters:

date range

camera

violation type


Response:

{
"total_violations":120,
"compliance_rate":95
}
10. Configuration API
GET /configurations

Purpose:

Retrieve system configuration.

Permissions:

Admin
PUT /configurations/{key}

Purpose:

Update configuration value.

Examples:

confidence_threshold

notification_settings

camera_parameters

11. WebSocket API
Connection

Endpoint:

WS /ws/camera/{camera_id}

Purpose:

Provide real-time camera events.

12. WebSocket Messages
Violation Event

Example:

{
"type":"violation",
"camera_id":"camera_001",
"violation":"Missing Helmet",
"confidence":0.94,
"timestamp":"2026-01-01"
}
Camera Status Event

Example:

{
"type":"camera_status",
"camera_id":"camera_001",
"status":"offline"
}
13. Error Response Format

All errors follow a standard format.

Example:

{
"error":"Validation Error",
"message":"Invalid camera ID",
"status_code":400
}
14. API Security
Authentication

Implemented using:

JWT Access Tokens
Refresh Tokens
Authorization

Implemented using:

Role-Based Access Control (RBAC)

Roles:

Admin

Safety Officer

Viewer

Validation

All incoming requests are validated using:

Pydantic schemas
Type checking
Input validation
Rate Limiting

Protects APIs against:

Excessive requests
Abuse
Automated attacks
CORS

Configured to allow trusted frontend clients only.

15. API Versioning

The API supports versioning:

Example:

/api/v1/users

/api/v2/users

Purpose:

Allow future changes without breaking existing clients.

16. API Design Principles
Consistency

All endpoints follow common naming conventions.

Security

Every sensitive operation requires authentication.

Scalability

Services can evolve independently.

Documentation

API contracts are documented before implementation.