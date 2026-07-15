# M2.2 Physical Architecture

## 1. Overview

The physical architecture describes where system components are deployed and how infrastructure resources communicate.

This design defines:

- Development environment
- Production environment
- Hardware requirements
- Runtime components
- Deployment boundaries


The platform follows a containerized architecture where frontend, backend, AI processing, and database services run as independent components.


---


---

# 3. Development Environment


## Purpose

The development environment provides a local workspace for building and testing the platform.


## Developer Machine


Components:

- Source Code Repository
- Docker Compose Environment
- Local Database
- Local AI Models
- Test Camera Sources


Architecture:



---

# 4. Development Components


## Frontend Container

Responsibilities:

- Run React application
- Provide development dashboard
- Communicate with backend APIs


Technology:

- React
- TypeScript
- Vite


---

## Backend API Container


Responsibilities:

- Provide REST APIs
- Handle authentication
- Execute business logic
- Manage communication with database


Technology:

- FastAPI
- Python


---

## AI Processing Container


Responsibilities:

- Run computer vision pipeline
- Execute object detection
- Process video frames


Technology:

- Python
- YOLO Model
- Deep Learning Framework


---

## Database Container


Responsibilities:

- Store application data
- Manage relational information


Technology:

- PostgreSQL


---

# 5. Production Environment


## Purpose

The production environment represents deployment inside an industrial facility.

The system operates on factory infrastructure with dedicated computing resources for real-time AI processing.


Architecture:



---

# 6. Production Components


# Camera Infrastructure


Responsibilities:

- Capture workplace video
- Provide real-time streams
- Send data to processing server


Supported Sources:

- IP Cameras
- RTSP Streams
- Industrial Cameras


---

# Edge / Server Machine


Purpose:

Provides local computation close to factory operations.


Responsibilities:

- Run AI inference
- Host application services
- Manage camera connections


Requirements:

- Multi-core CPU
- Sufficient RAM
- GPU acceleration for AI inference
- Network connectivity


---

# Container Platform


Responsibilities:

- Package applications
- Isolate services
- Simplify deployment
- Enable scaling


Possible Technologies:

- Docker
- Kubernetes


---

# Reverse Proxy


Technology:

Nginx


Responsibilities:

- HTTPS termination
- Route incoming traffic
- Protect backend services


---

# 7. Network Communication


## Camera → AI Service

Protocol:

- RTSP
- Network Streaming


Purpose:

Send video streams for analysis.


---

## Frontend → Backend

Protocol:

- HTTPS
- WebSocket


Purpose:

- API requests
- Real-time alerts


---

## Backend → Database

Protocol:

- PostgreSQL connection


Purpose:

Store and retrieve application data.


---

## Backend → Storage

Purpose:

Store:

- Violation snapshots
- Reports
- Evidence files


---

# 8. Hardware Requirements


## Minimum Production Hardware


### CPU

Multi-core server processor


### Memory

Recommended:

- 16GB RAM minimum
- 32GB+ for multiple cameras


### GPU

Recommended:

- NVIDIA GPU
- CUDA support


Purpose:

Accelerate AI inference.


### Storage

Required for:

- Database files
- Video snapshots
- Reports


---

# 9. Deployment Environments Comparison


| Feature | Development | Production |
|---|---|---|
| Location | Developer Machine | Factory Server |
| Deployment | Docker Compose | Docker/Kubernetes |
| Database | Local PostgreSQL | Production PostgreSQL |
| Cameras | Test Sources | Industrial Cameras |
| AI Processing | Development Model | Optimized Model |
| Security | Local Configuration | HTTPS + Secrets Management |
| Monitoring | Basic Logs | Full Monitoring System |


---

# 10. Scalability Considerations


The architecture supports future expansion:


## Multiple Cameras

Additional cameras can be connected without redesigning the system.


## Multiple Factories

Each factory can operate with independent edge servers.


## Cloud Integration

Future migration can support:

- Cloud storage
- Central monitoring
- Fleet management


## AI Scaling

AI processing can scale independently from application services.


---

# 11. Physical Architecture Principles


## Container Isolation

Each service runs independently.


## High Availability

Critical services can be replicated.


## Security

Network access is controlled through secure communication channels.


## Performance

AI processing occurs close to camera sources to reduce latency.
