# M2.6 Deployment Diagram

## 1. Overview

The Deployment Diagram describes the physical deployment topology of the AI PPE Detection & Safety Monitoring Platform.

It defines:

- External access points
- Network communication
- Runtime services
- Infrastructure components
- Storage and monitoring systems


The production architecture is designed for industrial environments where real-time AI processing is required.


---

# 2. Production Deployment Architecture


                Internet

                   |

                   |

                HTTPS

                   |

                   |

          +----------------+

          | Nginx Reverse  |

          | Proxy          |

          +----------------+

                   |

    ---------------------------------

    |               |               |

    ↓               ↓               ↓

+---------------+ +---------------+ +---------------+

| Frontend | | Backend API | | AI Pipeline |

| Container | | Container | | Container |

+---------------+ +---------------+ +---------------+

                    |

                    |

            +---------------+

            | PostgreSQL    |

            | Database      |

            +---------------+

                    |

                    |

            +---------------+

            | Storage       |

            | System        |

            +---------------+


                    |

                    |

            +---------------+

            | Monitoring    |

            | System        |

            +---------------+


---

# 3. External Layer


## Internet Users


Users access the platform through:

- Web browser
- Secure HTTPS connection


Examples:

- Safety Officers
- Administrators
- Managers


Communication:


User

↓

HTTPS

↓

Nginx



---

# 4. Reverse Proxy Layer


## Nginx Reverse Proxy


Purpose:

Provides a secure entry point for all external communication.


Responsibilities:

- HTTPS termination
- Traffic routing
- Request forwarding
- Security filtering
- Load balancing support


Routing:



/api

↓

Backend API

/

↓

Frontend

/ws

↓

WebSocket Service



---

# 5. Frontend Deployment


## Frontend Container


Purpose:

Provides the user interface.


Technology:

- React
- TypeScript
- Vite


Responsibilities:

- Display dashboards
- Show camera monitoring
- Display alerts
- Generate reports


Communication:



Frontend

↓

HTTPS API Requests

↓

Backend API



---

# 6. Backend API Deployment


## Backend Container


Purpose:

Runs application business logic.


Technology:

- FastAPI
- Python


Responsibilities:

- Authentication
- Authorization
- Business operations
- API management
- WebSocket communication


Communicates With:

- Frontend
- AI Pipeline
- Database
- Storage


---

# 7. AI Processing Deployment


## AI Pipeline Container


Purpose:

Provides computer vision processing.


Responsibilities:

- Receive video streams
- Process frames
- Execute AI inference
- Detect PPE violations


Components:



Camera Manager

↓

Frame Processor

↓

YOLO Detection Engine

↓

PPE Matcher

↓

Compliance Engine



Hardware Requirement:

- GPU acceleration recommended
- CUDA-compatible environment


---

# 8. Database Deployment


## PostgreSQL Container


Purpose:

Stores structured application data.


Stores:


Users:

- Accounts
- Roles


Cameras:

- Camera configuration
- Status


Violations:

- Detection events
- Compliance history


Audit Logs:

- User activities


Configurations:

- System settings


Database communication:


Backend API

↓

PostgreSQL



---

# 9. Storage Deployment


## Storage System


Purpose:

Stores unstructured data.


Examples:


- Violation snapshots
- Annotated images
- Generated reports


Storage Options:


Development:


Local File Storage



Production:


S3 Compatible Storage

MinIO

Cloud Object Storage



---

# 10. Monitoring Deployment


## Monitoring System


Purpose:

Observe system health and performance.


Monitors:


Application:

- API availability
- Errors
- Response time


Infrastructure:

- CPU usage
- Memory usage
- GPU utilization


AI Pipeline:

- Processing latency
- Detection performance


Database:

- Connections
- Storage usage


---

# 11. Network Communication


## User → Nginx

Protocol:

HTTPS


Purpose:

Secure user access.


---


## Nginx → Frontend

Protocol:

HTTP Internal Network


Purpose:

Serve frontend application.


---


## Nginx → Backend

Protocol:

HTTP/HTTPS Internal Network


Purpose:

API communication.


---


## Backend → Database

Protocol:

PostgreSQL Protocol


Purpose:

Database operations.


---


## Camera → AI Pipeline

Protocol:

RTSP / Network Streaming


Purpose:

Video transmission.


---


## Backend → Storage

Protocol:

Storage API


Purpose:

Save evidence files and reports.


---

# 12. Production Security Boundaries


The deployment uses separated network zones:



Public Network

  |

  |

Reverse Proxy Zone

  |

  |

Application Network

  |

  |

Data Network



Security controls:

- HTTPS encryption
- Firewall rules
- Network isolation
- Secret management
- Access control


---

# 13. Deployment Scalability


The architecture supports future expansion:


## Additional Cameras

New cameras can connect to AI services.


## Multiple AI Workers

AI containers can be scaled horizontally.


## Multiple Factories

Each factory can have:

- Local edge server
- Central monitoring platform


## Cloud Migration

Services can be moved to cloud infrastructure if required.


---

# 14. Deployment Principles


## Containerization

All services are isolated and portable.


## Reliability

Critical components can be replicated.


## Security

All communication channels are protected.


## Maintainability

Each service can be updated independently.