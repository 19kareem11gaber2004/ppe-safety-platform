# M2.3 Component Diagram

## 1. Overview

The component architecture defines the internal modules of the AI PPE Detection & Safety Monitoring Platform and their relationships.

The design follows:

- Modular architecture
- Separation of responsibilities
- One-direction dependencies
- Low coupling between components

The system is divided into:

- Backend Components
- AI Processing Components
- Frontend Components
- Data Components


---

# 2. High-Level Component Architecture

                Client User

                    |

                    |

          Frontend Application

                    |

                    |

              API Gateway

                    |

                    |

          Business Services

                    |

    --------------------------------

    |                              |

    |                              |
    

---

# 3. Backend Component Architecture


## Backend Structure

API Router

 |

 |

Service Layer

 |

 |

Repository Layer

 |

 |

Database Layer


---

# 4. API Router Component


## Responsibility

Provides external communication interfaces.


Responsibilities:

- Receive HTTP requests
- Validate input
- Return responses
- Handle WebSocket connections


Communicates With:

- Service Layer


Does Not:

- Access database directly
- Execute business logic


---

# 5. Service Layer


## Responsibility

Contains application business logic.


Main Services:


## User Service

Responsibilities:

- User management
- Role management
- Authentication operations


---


## Camera Service

Responsibilities:

- Register cameras
- Update camera status
- Manage camera configuration


---


## Violation Service

Responsibilities:

- Create violations
- Update violation status
- Manage violation history


---


## Report Service

Responsibilities:

- Generate safety reports
- Aggregate safety metrics


---


## Notification Service

Responsibilities:

- Send real-time alerts
- Manage notification events


---


## Audit Service

Responsibilities:

- Record system activities
- Track user actions


---


## Configuration Service

Responsibilities:

- Manage system settings
- Store operational configuration


---

# 6. Repository Layer


## Responsibility

Provides database access abstraction.


Responsibilities:

- Execute database operations
- Query entities
- Persist data


Communicates With:

- Database Layer


The repository layer prevents business services from directly depending on database implementation.


---

# 7. Database Component


## PostgreSQL Database


Stores:


Users

- Accounts
- Roles


Cameras

- Camera information
- Connection details


Violations

- Detection events
- Compliance results


Snapshots

- Evidence images


Audit Logs

- System activity


Configurations

- System parameters


---

# 8. AI Processing Components


The AI subsystem processes video streams and generates safety intelligence.


Architecture:

Camera Manager

   |

   |

Video Source

   |

   |

Frame Queue

   |

   |

YOLO Detection Engine

   |

   |

PPE Matcher

   |

   |

Compliance Engine

   |

   |

Violation Service


---

# 9. Camera Manager


## Responsibility

Controls camera connections.


Responsibilities:

- Connect to video sources
- Manage camera sessions
- Monitor camera availability


Input:

- RTSP streams
- IP camera feeds


Output:

- Video frames


---

# 10. Video Source Component


## Responsibility

Provides raw video input.


Responsibilities:

- Receive camera streams
- Decode video
- Forward frames


---

# 11. Frame Queue


## Responsibility

Controls frame processing flow.


Responsibilities:

- Buffer incoming frames
- Manage processing rate
- Prevent pipeline overload


---

# 12. YOLO Detection Engine


## Responsibility

Performs computer vision inference.


Responsibilities:

- Detect workers
- Detect PPE equipment
- Generate detection results


Input:

- Video frames


Output:

- Object detections


---

# 13. PPE Matcher


## Responsibility

Associates PPE equipment with workers.


Responsibilities:

- Match detected PPE objects
- Determine equipment ownership


Example:

Worker → Helmet → Safety Vest


---

# 14. Compliance Engine


## Responsibility

Applies safety rules.


Responsibilities:

- Evaluate PPE compliance
- Identify violations
- Generate compliance decisions


Output:

- Compliance status
- Violation events


---

# 15. Frontend Component Architecture


Structure:

Pages

|

Components

|

Hooks

|

API Client

|

WebSocket Client


---

# 16. Pages Component


## Responsibility

Provides application screens.


Examples:

- Dashboard Page
- Camera Monitoring Page
- Violations Page
- Reports Page
- User Management Page


---

# 17. UI Components


## Responsibility

Reusable interface elements.


Examples:

- Tables
- Charts
- Camera Viewer
- Alert Cards
- Forms


---

# 18. Hooks Layer


## Responsibility

Manages frontend state and communication logic.


Responsibilities:

- Fetch backend data
- Manage application state
- Handle real-time updates


---

# 19. API Client


## Responsibility

Communicates with backend APIs.


Responsibilities:

- Send HTTP requests
- Handle responses
- Manage authentication tokens


---

# 20. WebSocket Client


## Responsibility

Provides real-time communication.


Used For:

- Live camera updates
- Violation alerts
- System notifications


---

# 21. Dependency Direction


The system follows one-way dependencies:

Frontend

↓

API Router

↓

Service Layer

↓

Repository Layer

↓

Database

AI Pipeline

↓

Violation Service

↓

Database


---

# 22. Circular Dependency Prevention


Rules:


## API Layer

Must not directly access database.


## Services

Must not depend on API implementation.


## Repository

Must not contain business rules.


## AI Components

Must communicate through defined service interfaces.


---

# 23. Architecture Benefits


## Maintainability

Components can be modified independently.


## Scalability

AI processing can scale separately.


## Testing

Each component can be tested independently.


## Security

Access responsibilities are clearly separated.