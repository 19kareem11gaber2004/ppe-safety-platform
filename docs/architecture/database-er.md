# M2.7 Database ER Diagram

## 1. Overview

The Database Entity Relationship (ER) Design defines the structure of the platform database before implementation.

The database design focuses on:

- User management
- Camera management
- PPE violation tracking
- Evidence storage
- System auditing
- Configuration management


Database Technology:

- PostgreSQL


---

# 2. Entity Relationship Overview



+-------------+
| Users |
+-------------+
|
|
| 1
|
| *
+-------------+
| Audit Logs |
+-------------+

+-------------+
| Cameras |
+-------------+
|
|
| 1
|
| *
+-------------+
| Violations |
+-------------+
|
|
| 1
|
| *
+-------------+
| Snapshots |
+-------------+

+----------------+
| Configurations |
+----------------+



---

# 3. Entity Definitions


# 3.1 Users Entity


## Purpose

Stores system users and their access roles.


## Attributes


| Field | Type | Description |
|---|---|---|
| id | UUID | Unique user identifier |
| email | VARCHAR | User email address |
| password_hash | VARCHAR | Encrypted password |
| role | VARCHAR | User permission role |
| created_at | TIMESTAMP | Account creation time |


## Roles


Supported roles:


### Admin

Full system access.


### Safety Officer

Responsible for:

- Monitoring cameras
- Reviewing violations
- Generating reports


### Viewer

Read-only access.


---

# 3.2 Cameras Entity


## Purpose

Stores connected camera information.


## Attributes


| Field | Type | Description |
|---|---|---|
| id | UUID | Camera identifier |
| name | VARCHAR | Camera name |
| location | VARCHAR | Physical location |
| source_type | VARCHAR | Camera source type |
| url | VARCHAR | Stream address |
| status | VARCHAR | Current camera status |


## Example



Camera:

ID:
CAM-001

Location:
Production Area A

Status:
Online



---

# 3.3 Violations Entity


## Purpose

Stores detected PPE safety violations.


## Attributes


| Field | Type | Description |
|---|---|---|
| id | UUID | Violation identifier |
| camera_id | UUID | Related camera |
| worker_id | UUID | Detected worker reference |
| type | VARCHAR | Violation type |
| confidence | FLOAT | AI confidence score |
| timestamp | TIMESTAMP | Detection time |


## Examples


Violation Types:


- Missing Helmet
- Missing Vest
- Missing Gloves


---

# 3.4 Snapshots Entity


## Purpose

Stores evidence images related to violations.


## Attributes


| Field | Type | Description |
|---|---|---|
| id | UUID | Snapshot identifier |
| violation_id | UUID | Related violation |
| path | VARCHAR | Image storage path |
| created_at | TIMESTAMP | Creation time |


Purpose:

Provides visual evidence for safety review.


---

# 3.5 Audit Logs Entity


## Purpose

Tracks user and system activities.


## Attributes


| Field | Type | Description |
|---|---|---|
| id | UUID | Log identifier |
| user_id | UUID | User performing action |
| action | VARCHAR | Performed action |
| timestamp | TIMESTAMP | Action time |


Examples:



User Login

Camera Updated

Configuration Changed

User Created



---

# 3.6 Configurations Entity


## Purpose

Stores dynamic system configuration values.


## Attributes


| Field | Type | Description |
|---|---|---|
| id | UUID | Configuration identifier |
| key | VARCHAR | Configuration name |
| value | TEXT | Configuration value |


Examples:



Detection Confidence Threshold

Notification Settings

Camera Parameters



---

# 4. Relationships


## Users → Audit Logs


Relationship:

One-to-Many


Explanation:


One user can create multiple audit records.



Users

1

|

|

Audit Logs



---

## Cameras → Violations


Relationship:

One-to-Many


Explanation:


One camera can generate multiple violation events.



Cameras

1

|

|

Violations



---

## Violations → Snapshots


Relationship:

One-to-Many


Explanation:


One violation can contain multiple evidence snapshots.



Violations

1

|

|

Snapshots



---

# 5. Database Constraints


## Primary Keys


Each entity contains a unique identifier:


Examples:


users.id

cameras.id

violations.id



---

## Foreign Keys


Relationships are enforced through foreign keys:


Examples:



violations.camera_id

↓

cameras.id

snapshots.violation_id

↓

violations.id

audit_logs.user_id

↓

users.id



---

# 6. Indexing Strategy


Recommended indexes:


## Users

Index:


email


Purpose:

Fast authentication lookup.


---

## Cameras

Indexes:


location

status



Purpose:

Fast camera filtering.


---

## Violations

Indexes:


camera_id

timestamp

type



Purpose:

Fast reporting and analytics.


---

# 7. Future Database Extensions


The current design supports future expansion.


## Workers Entity


Future table:


Workers

id

employee_code

department

created_at



Purpose:

Track individual worker compliance.


---

## PPE Equipment Entity


Future table:


PPE_Items

id

name

category

required



Purpose:

Support multiple PPE types.


---

## Factories Entity


Future table:



Factories

id

name

location



Purpose:

Support multiple industrial sites.


---

# 8. Migration Considerations


The database should support:


## Version Control

Database changes managed through migrations.


Example:

- Alembic
- PostgreSQL migration tools


---

## Data Backup


Production requires:

- Scheduled backups
- Recovery procedures
- Backup verification


---

## Scalability


Future support:


- Partitioning large violation tables
- Historical data archiving
- Read replicas
- Distributed storage


---

# 9. Database Design Principles


## Data Integrity

Relationships are enforced using constraints.


## Security

Sensitive information is protected.


## Performance

Indexes optimize frequent queries.


## Extensibility

The schema supports future features and multiple factories.