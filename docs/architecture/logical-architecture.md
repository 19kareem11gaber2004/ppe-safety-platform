# M2.1 Logical Architecture

## 1. Overview

The AI PPE Detection & Safety Monitoring Platform is designed as an enterprise-scale intelligent safety system that monitors industrial environments using computer vision and artificial intelligence.

The logical architecture defines the major software layers, responsibilities, and communication boundaries without specifying deployment details or implementation configurations.

The system follows a layered architecture:

- Client Layer
- API Gateway Layer
- Business Services Layer
- AI Processing Layer
- Data Layer
- Infrastructure Layer


---

# 2. High-Level Architecture

+------------------------------------------------+
| Client Layer |
| |
| React Dashboard |
| Camera Monitoring |
| Reports |
| User Management |
| Notifications |
+------------------------------------------------+
+------------------------------------------------+
| API Gateway Layer |
| |
| Authentication |
| Authorization |
| REST APIs |
| WebSocket Communication |
+------------------------------------------------+
+------------------------------------------------+
| Business Services Layer |
| |
| User Service |
| Camera Service |
| Violation Service |
| Report Service |
| Notification Service |
| Audit Service |
| Configuration Service |
+------------------------------------------------+
+------------------------------------------------+
| AI Processing Layer |
| |
| Video Source Manager |
| Frame Processor |
| YOLO Detection Engine |
| PPE Matcher |
| Compliance Engine |
| Annotation Engine |
+------------------------------------------------+
+------------------------------------------------+
| Data Layer |
| |
| PostgreSQL Database |
| File Storage |
| Future Object Storage (S3/MinIO) |
+------------------------------------------------+
+------------------------------------------------+
| Infrastructure Layer |
| |
| Compute Resources |
| Networking |
| Monitoring |
| Security Services |
+------------------------------------------------+


---

# 3. Client Layer

## Purpose

The Client Layer provides the user interaction interface for safety monitoring operations.

## Responsibilities

- Display real-time camera monitoring
- Show PPE compliance status
- Display violation alerts
- Generate safety reports
- Manage system users
- Configure monitoring settings

## Main Components

### Web Dashboard

Provides:

- Live monitoring interface
- Safety statistics
- Violation history
- Reports visualization


### User Interface

Technology:

- React
- TypeScript
- Vite


---

# 4. API Gateway Layer

## Purpose

The API Gateway Layer provides a secure communication entry point between clients and backend services.

## Responsibilities

- Handle client requests
- Authenticate users
- Authorize system operations
- Provide REST API endpoints
- Manage real-time WebSocket communication


## Main Components


### Authentication Module

Responsible for:

- Login validation
- Token generation
- Session management


### API Interface

Responsible for:

- Request handling
- Response formatting
- Input validation


Technology:

- FastAPI
- Pydantic
- JWT


---

# 5. Business Services Layer

## Purpose

The Business Services Layer contains the core application logic and business rules.

## Services


## User Service

Responsibilities:

- User management
- Role assignment
- Account operations


## Camera Service

Responsibilities:

- Register cameras
- Manage camera configuration
- Track camera status


## Violation Service

Responsibilities:

- Store safety violations
- Manage violation lifecycle
- Provide violation history


## Report Service

Responsibilities:

- Generate safety reports
- Aggregate compliance data


## Notification Service

Responsibilities:

- Send real-time alerts
- Manage notification events


## Audit Service

Responsibilities:

- Track user activities
- Maintain security records


## Configuration Service

Responsibilities:

- Manage system settings
- Store operational parameters


---

# 6. AI Processing Layer

## Purpose

The AI Processing Layer performs computer vision analysis and PPE compliance detection.


## Components


## Video Source Manager

Responsibilities:

- Connect to camera sources
- Receive video streams
- Manage camera connections


## Frame Processor

Responsibilities:

- Extract frames
- Prepare images for inference
- Optimize processing pipeline


## YOLO Detection Engine

Responsibilities:

- Detect workers
- Detect PPE equipment
- Generate detection results


## PPE Matcher

Responsibilities:

- Associate PPE objects with workers
- Validate PPE presence


## Compliance Engine

Responsibilities:

- Apply safety rules
- Determine compliance status
- Generate violation events


## Annotation Engine

Responsibilities:

- Add visual indicators
- Generate annotated frames


---

# 7. Data Layer

## Purpose

The Data Layer provides persistent storage for operational and historical information.


## Database

### PostgreSQL

Stores:

- Users
- Cameras
- Violations
- Reports
- Audit logs
- Configurations


## Storage

### Local Storage

Used for:

- Snapshots
- Detection evidence
- Generated reports


### Future Object Storage

Possible:

- Amazon S3
- MinIO


---

# 8. Infrastructure Layer

## Purpose

Provides the technical foundation required to operate the platform.


Responsibilities:

- Compute resources
- Network communication
- System monitoring
- Security controls
- Deployment environment


Includes:

- Servers
- Containers
- GPU resources
- Logging systems
- Monitoring tools


---

# 9. Communication Between Layers


## Client → API Gateway

Communication:

- HTTPS
- WebSocket


Purpose:

- User requests
- Real-time updates


## API Gateway → Business Services

Communication:

- Internal service calls


Purpose:

- Execute business operations


## Business Services → Data Layer

Communication:

- Database queries
- Storage operations


Purpose:

- Persistent data management


## AI Layer → Business Services

Communication:

- Detection events
- Compliance results


Purpose:

- Create safety violations
- Trigger notifications


---

# 10. Architecture Principles

The system follows these principles:

## Separation of Concerns

Each layer has a clear responsibility.


## Scalability

AI processing can scale independently from application services.


## Maintainability

Components are modular and loosely coupled.


## Security by Design

Authentication, authorization, and auditing are integrated into the architecture.


## Future Expansion

The architecture supports:

- Multiple factories
- Multiple cameras
- Cloud deployment
- Advanced AI models