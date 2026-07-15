# M2.5 Data Flow Diagram

## 1. Overview

The Data Flow Diagram (DFD) describes how information moves through the AI PPE Detection & Safety Monitoring Platform.

It defines:

- Data sources
- Data processing stages
- AI analysis flow
- Data storage locations
- User-facing outputs

The main data lifecycle:
Camera Input

↓

Video Processing

↓

AI Detection

↓

PPE Analysis

↓

Compliance Decision

↓

Violation Event

↓

Database Storage

↓

Dashboard / Reports


---

# 2. High-Level Data Flow



+----------------+
| Industrial |
| Camera |
+----------------+

    |

    |
    | Video Stream
    ↓

+----------------+
| Camera Manager |
+----------------+

    |

    |
    | Video Frames
    ↓

+----------------+
| Frame |
| Processor |
+----------------+

    |

    |
    | Processed Frames
    ↓

+----------------+
| YOLO Detection |
| Engine |
+----------------+

    |

    |
    | Detection Results
    ↓

+----------------+
| PPE Matcher |
+----------------+

    |

    |
    | PPE Status
    ↓

+----------------+
| Compliance |
| Engine |
+----------------+

    |

    |
    | Violation Event
    ↓

+----------------+
| Violation |
| Service |
+----------------+

    |

    |
    ↓

+----------------+
| PostgreSQL |
| Database |
+----------------+

    |

    |

    ↓

+----------------+
| Dashboard |
| Reports |
+----------------+


---

# 3. Input Data

## 3.1 Camera Data

Source:

Industrial Cameras


Data Type:

- Video streams
- Frames
- Camera metadata


Examples:


Camera ID

Location

Timestamp

Video Frame

Resolution


Purpose:

Provide real-time workplace monitoring data.

---

# 4. Processing Data Flow


## 4.1 Video Acquisition


Component:

Camera Manager


Responsibilities:

- Connect to camera sources
- Receive video streams
- Maintain camera status


Input:


RTSP/IP Camera Stream



Output:


Raw Video Frames



---

## 4.2 Frame Processing


Component:

Frame Processor


Responsibilities:

- Extract frames
- Resize images
- Normalize input
- Prepare AI input


Input:

Raw frames


Output:

AI-ready frames


---

## 4.3 AI Detection


Component:

YOLO Detection Engine


Responsibilities:

Analyze frames and detect:

- Workers
- Helmets
- Safety vests
- Gloves
- Other PPE equipment


Input:

Processed image frames


Output:

Detection results:



Object Type

Bounding Box

Confidence Score

Position


---

# 5. PPE Analysis Flow


## PPE Matcher


Purpose:

Associate detected PPE objects with workers.


Example:



Worker 001

Helmet ✓

Vest ✓

Gloves ✗



Output:

Worker safety status.


---

# 6. Compliance Decision Flow


## Compliance Engine


Purpose:

Apply safety rules.


Input:

Detection results


Processing:


Detection Result

Safety Rules

=

Compliance Decision



Output:


Compliant:



Worker 001

Status: SAFE



Violation:



Worker 002

Missing Helmet

Status: VIOLATION


---

# 7. Violation Event Data


When a violation occurs, the system generates an event.


Stored information:



Violation ID

Camera ID

Worker ID

Violation Type

Confidence Score

Timestamp

Snapshot Reference


---

# 8. Data Storage Flow


## PostgreSQL Database


Stores structured information:


### Users


User accounts

Roles

Permissions



### Cameras


Camera configuration

Location

Status



### Violations


Detection events

Compliance results

History



### Audit Logs


User actions

System changes



---

## File Storage


Stores:


- Violation snapshots
- Annotated images
- Generated reports


Future Support:

- S3
- MinIO


---

# 9. Dashboard Data Flow


The dashboard receives processed information from backend services.


Flow:



Database

↓

Backend Services

↓

API Gateway

↓

Frontend Dashboard



Displayed information:


## Live Monitoring

- Camera streams
- Detection overlays


## Alerts

- Active violations
- Safety warnings


## Reports

- Compliance statistics
- Historical analysis


---

# 10. Data Ownership


| Data | Owner Component |
|---|---|
| Camera Streams | Camera Manager |
| Video Frames | AI Processing Layer |
| Detection Results | AI Engine |
| Compliance Rules | Compliance Engine |
| Violations | Violation Service |
| User Data | User Service |
| Audit Records | Audit Service |
| Reports | Report Service |


---

# 11. Data Security Considerations


The system protects data through:


## Transmission Security

- HTTPS communication
- Secure camera connections


## Access Control

- Role-based permissions
- Authorized dashboard access


## Storage Protection

- Database access control
- Encrypted sensitive data
- Backup strategy


---

# 12. Data Flow Principles


## Real-Time Processing

The system processes camera streams with minimum latency.


## Data Separation

Operational data and AI processing data are logically separated.


## Traceability

Every violation can be traced back to:

- Camera source
- Detection result
- Timestamp
- Evidence snapshot


## Scalability

The data pipeline supports additional cameras and future factories.